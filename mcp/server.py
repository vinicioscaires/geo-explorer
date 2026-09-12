#!/usr/bin/env python
"""
Geo-Explorer MCP Server
-----------------------
Expõe as três ferramentas do Geo-Explorer para que outros clientes MCP
possam acessar os recursos da plataforma.

Ferramentas disponíveis:
  - geo_trilha       → retorna os dados completos de uma trilha
  - geo_desafio      → retorna metadados de um desafio para uma tecnologia/nível
  - geo_certificado  → gera um certificado de explorador

Arquivo de dados: dados/geo_trilhas.json (relativo à raiz do projeto)
"""

import json
import os
import random
import string
from datetime import datetime

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# ── Caminhos ─────────────────────────────────────────────────────────────────

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(BASE_DIR, "dados", "geo_trilhas.json")

# ── Helpers ───────────────────────────────────────────────────────────────────

def _carregar_dados() -> dict:
    with open(JSON_PATH, encoding="utf-8") as f:
        return json.load(f)


def _buscar_trilha(tecnologia: str, dados: dict) -> dict | None:
    if not tecnologia or not isinstance(tecnologia, str):
        return None
    termo = tecnologia.strip().lower()
    for t in dados["trilhas"]:
        if termo in t["tecnologia"].lower() or termo in t["nome"].lower():
            return t
    return None


def _gerar_id() -> str:
    chars = string.ascii_uppercase + string.digits
    return "GEO-" + "".join(random.choices(chars, k=10))


# ── Servidor MCP ──────────────────────────────────────────────────────────────

server = Server("geo-explorer")


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="geo_trilha",
            description=(
                "Retorna os dados completos de uma trilha do Geo-Explorer "
                "a partir do nome da tecnologia (ex: Python, React, DevOps)."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "tecnologia": {
                        "type": "string",
                        "description": "Nome da tecnologia ou da trilha (busca parcial, case-insensitive).",
                    }
                },
                "required": ["tecnologia"],
            },
        ),
        types.Tool(
            name="geo_desafio",
            description=(
                "Retorna os metadados de um desafio do Geo-Explorer: "
                "XP disponível, dificuldade, tempo estimado e casos de teste de exemplo, "
                "com base na tecnologia e nível informados."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "tecnologia": {
                        "type": "string",
                        "description": "Nome da tecnologia (ex: Python, JavaScript).",
                    },
                    "nivel": {
                        "type": "string",
                        "description": "Nível do desafio: Iniciante, Intermediário ou Avançado.",
                        "enum": ["Iniciante", "Intermediário", "Avançado"],
                    },
                },
                "required": ["tecnologia", "nivel"],
            },
        ),
        types.Tool(
            name="geo_certificado",
            description=(
                "Gera um certificado de explorador do Geo-Explorer com ID único, "
                "dados reais da trilha (XP, badges, recompensa) e URL de verificação."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "nome": {
                        "type": "string",
                        "description": "Nome completo do explorador.",
                    },
                    "tecnologia": {
                        "type": "string",
                        "description": "Tecnologia ou trilha concluída.",
                    },
                },
                "required": ["nome", "tecnologia"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:

    try:
        dados = _carregar_dados()
    except FileNotFoundError:
        return [types.TextContent(type="text", text=f"Erro: arquivo de dados não encontrado em {JSON_PATH}")]

    # ── geo_trilha ────────────────────────────────────────────────────────────
    if name == "geo_trilha":
        tecnologia = arguments.get("tecnologia", "")
        trilha = _buscar_trilha(tecnologia, dados)
        if not trilha:
            nomes = [t["tecnologia"] for t in dados["trilhas"]]
            return [types.TextContent(
                type="text",
                text=f"Trilha '{tecnologia}' não encontrada. Tecnologias disponíveis: {', '.join(nomes)}",
            )]
        return [types.TextContent(type="text", text=json.dumps(trilha, ensure_ascii=False, indent=2))]

    # ── geo_desafio ───────────────────────────────────────────────────────────
    elif name == "geo_desafio":
        tecnologia = arguments.get("tecnologia", "")
        nivel      = arguments.get("nivel", "Iniciante")
        trilha     = _buscar_trilha(tecnologia, dados)

        xp_ranges = {"Iniciante": (300, 500), "Intermediário": (600, 900), "Avançado": (1000, 1500)}
        xp = random.randint(*xp_ranges.get(nivel, (300, 500)))

        estrelas = {"Iniciante": "⭐☆☆☆☆", "Intermediário": "⭐⭐⭐☆☆", "Avançado": "⭐⭐⭐⭐⭐"}
        tempos   = {"Iniciante": "30 minutos", "Intermediário": "1 hora", "Avançado": "2 horas"}

        desafio = {
            "titulo":    f"Missão de Código — {tecnologia} | Nível: {nivel}",
            "tecnologia": tecnologia,
            "nivel":      nivel,
            "tema":       trilha["tema"] if trilha else "Aventura",
            "xp":         xp,
            "dificuldade": estrelas.get(nivel, "⭐☆☆☆☆"),
            "tempo":       tempos.get(nivel, "30 minutos"),
            "missoes_especiais": trilha["missoes_especiais"] if trilha else [],
        }
        return [types.TextContent(type="text", text=json.dumps(desafio, ensure_ascii=False, indent=2))]

    # ── geo_certificado ───────────────────────────────────────────────────────
    elif name == "geo_certificado":
        nome       = arguments.get("nome", "")
        tecnologia = arguments.get("tecnologia", "")

        if not nome or not tecnologia:
            return [types.TextContent(type="text", text="Erro: 'nome' e 'tecnologia' são obrigatórios.")]

        trilha = _buscar_trilha(tecnologia, dados)
        if not trilha:
            return [types.TextContent(type="text", text=f"Trilha '{tecnologia}' não encontrada.")]

        cert_id = _gerar_id()
        certificado = {
            "id":         cert_id,
            "explorador": nome,
            "trilha":     trilha["nome"],
            "tecnologia": trilha["tecnologia"],
            "nivel":      trilha["nivel"],
            "tema":       trilha["tema"],
            "horas":      trilha["duracao_horas"],
            "xp":         trilha["xp_total"],
            "badges":     trilha["badges"],
            "recompensa": trilha["recompensa_final"],
            "data":       datetime.today().strftime("%d/%m/%Y"),
            "url":        f"https://geo-explorer.dev/certificado/{cert_id}",
        }
        return [types.TextContent(type="text", text=json.dumps(certificado, ensure_ascii=False, indent=2))]

    return [types.TextContent(type="text", text=f"Ferramenta desconhecida: {name}")]


# ── Entry point ───────────────────────────────────────────────────────────────

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
