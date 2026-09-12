# ⚔️ Comando /desafio

**Arquivo:** `comandos/desafio.md`  
**Hint:** `/desafio <tecnologia> <nivel>`

## O que faz

Gera uma missão de código única, com narrativa temática inspirada na trilha correspondente. O tipo de missão é escolhido aleatoriamente a cada chamada.

## Parâmetros

| Parâmetro | Tipo | Obrigatório | Valores aceitos |
|---|---|---|---|
| `tecnologia` | string | Sim | Qualquer tecnologia (ex: Python, Java, DevOps) |
| `nivel` | string | Sim | `Iniciante`, `Intermediário`, `Avançado` |

## Tipos de missão (aleatório)

Algoritmo · Estrutura de Dados · API/Integração · Lógica · Mini-Projeto · Refatoração · Caça ao Bug

## XP por nível

| Nível | XP disponível | Tempo estimado |
|---|---|---|
| Iniciante | 300–500 XP | 20–30 min |
| Intermediário | 600–900 XP | 45–60 min |
| Avançado | 1000–1500 XP | 90–120 min |

## Exemplos

```
/desafio Python Iniciante
/desafio JavaScript Intermediário
/desafio DevOps Avançado
```
