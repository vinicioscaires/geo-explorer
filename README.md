# 🌍 Geo-Explorer

> Plataforma fictícia de exploração e aprendizagem em tecnologia, desenvolvida com **IBM Bob**.

---

## 🧭 Sobre o Projeto

O **Geo-Explorer** transforma o aprendizado em uma aventura. Cada trilha é uma jornada temática — com módulos, missões especiais, badges e recompensas — tornando o caminho até a maestria técnica épico e motivador.

Três comandos principais movem a plataforma:

| Comando | Descrição |
|---|---|
| `/trilha <tecnologia>` | Exibe o plano de exploração de uma trilha |
| `/desafio <tecnologia> <nivel>` | Gera uma missão de código temática |
| `/certificado <nome> <tecnologia>` | Emite o certificado de explorador |

**Exemplos:**
```
/trilha Python
/desafio JavaScript Intermediário
/certificado "Ada Lovelace" React
```

---

## 🗺️ Trilhas Disponíveis

| # | Trilha | Tecnologia | Nível | XP |
|---|--------|------------|-------|----|
| 1 | Jornada do Código Selvagem | Python | Iniciante | 9.600 |
| 2 | Fronteiras do Front-End | JavaScript | Iniciante | 10.800 |
| 3 | O Castelo do TypeScript | TypeScript | Intermediário | 13.500 |
| 4 | Templo de React | React | Intermediário | 14.200 |
| 5 | Ruínas do Node.js | Node.js | Intermediário | 12.800 |
| 6 | Galáxia Java | Java | Intermediário | 15.600 |
| 7 | A Fortaleza dos Dados | SQL | Iniciante | 8.400 |
| 8 | Nuvem Sem Fronteiras | Cloud Computing | Avançado | 19.600 |
| 9 | Labirinto do DevOps | DevOps | Avançado | 18.200 |
| 10 | Oráculo da Inteligência Artificial | IA | Avançado | 22.500 |
| 11 | Floresta do Flutter | Flutter | Iniciante | 10.800 |
| 12 | Oceano da Segurança | Cibersegurança | Avançado | 20.300 |

---

## 📁 Estrutura do Projeto

```
geo-explorer/
├── dados/                    # Fonte de dados fictícios
│   └── geo_trilhas.json      # 12 trilhas temáticas
├── comandos/                 # Definições dos slash commands (fonte)
│   ├── trilha.md
│   ├── desafio.md
│   └── certificado.md
├── docs/                     # Documentação
│   ├── comandos/             # Docs de cada comando
│   ├── ARQUITETURA.md
│   └── CONTRIBUINDO.md
├── testes/                   # Suítes de testes
│   ├── unitarios/            # Testes por comando
│   ├── fluxo/                # Testes de integração
│   └── saidas/               # Exemplos de saída gerados
├── scripts/                  # Utilitários
├── assets/                   # Recursos estáticos
├── .bob/                     # Configuração IBM Bob
│   └── commands/             # Slash commands ativos
└── README.md
```

---

## 🧪 Testes

```bash
python testes/executar_testes.py
```

---

## 🤖 Desenvolvido com IBM Bob

O Geo-Explorer foi criado inteiramente com o apoio do **IBM Bob** — IA assistente para desenvolvimento de software.
