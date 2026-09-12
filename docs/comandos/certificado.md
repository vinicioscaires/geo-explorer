# 🏆 Comando /certificado

**Arquivo:** `comandos/certificado.md`  
**Hint:** `/certificado <seu-nome> <tecnologia>`

## O que faz

Gera um certificado épico e comemorativo em Markdown para o explorador que concluiu uma trilha. Usa os dados reais da trilha do `dados/geo_trilhas.json`.

## Parâmetros

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `nome` | string | Sim | Nome do explorador (ex: "Ada Lovelace") |
| `tecnologia` | string | Sim | Tecnologia da trilha concluída (ex: Python) |

## Campos gerados automaticamente

| Campo | Origem |
|---|---|
| Nível | `nivel` da trilha no JSON |
| Horas de Jornada | `duracao_horas` da trilha |
| XP Conquistado | `xp_total` da trilha |
| Badges | `badges` da trilha |
| Recompensa | `recompensa_final` da trilha |
| ID do Certificado | `GEO-` + 10 caracteres aleatórios |
| URL | `https://geo-explorer.dev/certificado/<ID>` |
| Data | Data atual `DD/MM/AAAA` |

## Exemplos

```
/certificado "Ada Lovelace" Python
/certificado "Alan Turing" IA
/certificado "Grace Hopper" Java
```
