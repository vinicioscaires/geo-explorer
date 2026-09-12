# 🗺️ Comando /trilha

**Arquivo:** `comandos/trilha.md`  
**Hint:** `/trilha <tecnologia>`

## O que faz

Busca a trilha em `dados/geo_trilhas.json` com busca **case-insensitive e parcial** e apresenta um plano de exploração temático com módulos, missões especiais, badges e recompensa final.

## Parâmetros

| Parâmetro | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `tecnologia` | string | Sim | Tecnologia desejada (ex: Python, react, java) |

## Comportamento

- Busca case-insensitive: `python`, `PYTHON` e `Python` encontram a mesma trilha
- Busca parcial: `java` encontra JavaScript e Java — o Bob escolhe o mais relevante
- Se não encontrar: lista todas as 12 tecnologias disponíveis
- O Bob usa o tema da trilha para dar nomes criativos aos módulos

## Exemplos

```
/trilha Python
/trilha react
/trilha cloud
/trilha IA
```
