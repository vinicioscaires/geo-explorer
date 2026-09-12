# 🏗️ Arquitetura do Geo-Explorer

## Visão Geral

```
┌─────────────────────────────────────────────────┐
│               Explorador (IBM Bob)               │
│    /trilha     /desafio     /certificado          │
└──────────────────┬──────────────────────────────┘
                   │ Slash Commands
┌──────────────────▼──────────────────────────────┐
│             .bob/commands/                       │
│   trilha.md   desafio.md   certificado.md        │
│   (instruções de prompt para o IBM Bob)          │
└──────────────────┬──────────────────────────────┘
                   │ Leitura de dados
┌──────────────────▼──────────────────────────────┐
│           dados/geo_trilhas.json                 │
│   12 trilhas temáticas · fonte de verdade        │
└─────────────────────────────────────────────────┘
```

## Componentes

### 1. Slash Commands (`.bob/commands/`)
Arquivos Markdown com instruções de prompt interpretadas pelo IBM Bob. A fonte de verdade dos comandos fica em `comandos/` e é espelhada em `.bob/commands/`.

### 2. Dados (`dados/`)
`geo_trilhas.json` é a única fonte de dados do projeto. Todos os comandos leem deste arquivo. Cada trilha possui tema narrativo, módulos, missões especiais, badges e recompensa final.

### 3. Testes (`testes/`)
- **unitarios/** — validam lógica isolada de cada comando
- **fluxo/** — simulam a jornada completa de um explorador
- **saidas/** — exemplos de saída gerados pelos comandos

## Fluxo por Comando

```
/trilha Python
  └─► Bob lê .bob/commands/trilha.md
        └─► Bob lê dados/geo_trilhas.json
              └─► Localiza "Jornada do Código Selvagem"
                    └─► Gera plano temático formatado

/desafio Python Iniciante
  └─► Bob lê .bob/commands/desafio.md
        └─► Bob lê dados/geo_trilhas.json (para o tema)
              └─► Gera missão de código narrativa

/certificado "Ada Lovelace" Python
  └─► Bob lê .bob/commands/certificado.md
        └─► Bob lê dados/geo_trilhas.json
              └─► Gera certificado épico com dados reais da trilha
```

## Schema do JSON

```json
{
  "id": 1,
  "nome": "Nome Temático da Trilha",
  "tecnologia": "Python",
  "nivel": "Iniciante | Intermediário | Avançado",
  "tema": "Aventura | Fantasia | Ficção Científica | ...",
  "numero_de_modulos": 8,
  "xp_total": 9600,
  "duracao_horas": 64,
  "badges": ["Badge 1", "Badge 2", "Badge 3"],
  "habilidades": ["habilidade 1", "habilidade 2"],
  "missoes_especiais": ["Missão 1", "Missão 2", "Missão 3"],
  "recompensa_final": "Nome da Recompensa Épica",
  "ativa": true
}
```
