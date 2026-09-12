# 🌍 Geo-Explorer

> Plataforma fictícia de exploração e aprendizagem em tecnologia, desenvolvida inteiramente com **IBM Bob**.

---

## 📖 O que é o Geo-Explorer

O **Geo-Explorer** transforma o aprendizado em tecnologia em uma aventura épica. Cada trilha é uma jornada temática — com módulos progressivos, missões especiais, badges e recompensas — tornando o caminho até a maestria técnica motivador e imersivo.

A plataforma foi criada como um desafio prático de desenvolvimento assistido por IA, usando o **IBM Bob** como parceiro de desenvolvimento em todas as etapas: ideação, criação de dados, definição dos slash commands, escrita dos testes e automação.

Três comandos principais movem a plataforma, todos operando diretamente dentro do IBM Bob:

| Comando | Descrição |
|---|---|
| `/trilha <tecnologia>` | Exibe o plano completo de exploração de uma trilha |
| `/desafio <tecnologia> <nivel>` | Gera uma missão de código temática e narrativa |
| `/certificado <nome> <tecnologia>` | Emite um certificado épico de explorador |

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

## ⚙️ Como executar o projeto

### Pré-requisitos

- [IBM Bob](https://www.ibm.com/products/bob) instalado e configurado
- [Python 3.10+](https://www.python.org/) (apenas para rodar os testes)
- Nenhuma dependência externa — a plataforma usa somente a biblioteca padrão do Python

### Instalação

#### 1. Crie seu repositório no GitHub

1. Acesse [github.com](https://github.com) e faça login na sua conta
2. Clique em **"New"** (botão verde no canto superior esquerdo) ou acesse [github.com/new](https://github.com/new)
3. Preencha os campos:
   - **Repository name:** `geo-explorer`
   - **Description:** `Plataforma fictícia de exploração e aprendizagem em tecnologia — IBM Bob`
   - Marque **Public**
   - **Não** marque "Add a README file" (já temos um)
4. Clique em **"Create repository"**
5. Copie a URL do seu repositório — será algo como `https://github.com/seu-usuario/geo-explorer.git`

#### 2. Clone este repositório e aponte para o seu

```bash
# Clone o repositório original
git clone https://github.com/vinicioscaires/geo-explorer.git
cd geo-explorer

# Troque o remote para apontar para o SEU repositório
git remote set-url origin https://github.com/SEU-USUARIO/geo-explorer.git

# Suba o projeto para o seu GitHub
git push --set-upstream origin master
```

> 💡 Substitua `SEU-USUARIO` pelo seu nome de usuário do GitHub.

Nenhum `pip install` é necessário. O projeto não possui dependências externas.

### Estrutura do projeto

```
geo-explorer/
├── dados/                    # Fonte de dados fictícios
│   └── geo_trilhas.json      # 12 trilhas temáticas (fonte de verdade)
├── comandos/                 # Definições dos slash commands (fonte)
│   ├── trilha.md
│   ├── desafio.md
│   └── certificado.md
├── .bob/
│   └── commands/             # Slash commands ativos no IBM Bob
│       ├── trilha.md
│       ├── desafio.md
│       └── certificado.md
├── docs/                     # Documentação
│   ├── ARQUITETURA.md
│   ├── CONTRIBUINDO.md
│   └── comandos/
├── testes/                   # Suítes de testes
│   ├── unitarios/            # Testes por comando
│   ├── fluxo/                # Testes de integração (jornada completa)
│   ├── saidas/               # Exemplos de saída gerados
│   ├── executar_testes.py    # Runner principal
│   └── resultados.txt        # Relatório do último run
├── scripts/                  # Utilitários
└── assets/                   # Recursos estáticos
```

---

## 🧭 Como usar os comandos

Os comandos são **slash commands do IBM Bob**. Para usá-los, abra o IBM Bob no workspace do projeto e digite os comandos no chat.

### `/trilha <tecnologia>`

Exibe o plano completo de exploração de uma trilha: módulos progressivos com nomes temáticos, missões especiais, badges, habilidades desenvolvidas e recompensa final.

```
/trilha Python
/trilha TypeScript
/trilha "Cloud Computing"
```

A busca é **case-insensitive** e aceita nome parcial da tecnologia ou da trilha.

---

### `/desafio <tecnologia> <nivel>`

Gera uma missão de código única e narrativa. Inclui: tipo de missão, tempo estimado, dificuldade em estrelas, XP disponível, narrativa temática imersiva, entrada/saída esperada, pistas progressivas, casos de teste e critérios de vitória.

```
/desafio Python Iniciante
/desafio JavaScript Intermediário
/desafio DevOps Avançado
```

Níveis válidos: `Iniciante` · `Intermediário` · `Avançado`

XP por nível:
- Iniciante → 300–500 XP
- Intermediário → 600–900 XP
- Avançado → 1.000–1.500 XP

---

### `/certificado <nome> <tecnologia>`

Emite um certificado épico em Markdown com dados reais da trilha: nível, horas de jornada, XP conquistado, badges, recompensa desbloqueada, avaliação motivacional e ID único verificável.

```
/certificado "Ada Lovelace" Python
/certificado "Alan Turing" Java
/certificado "Grace Hopper" DevOps
```

O certificado inclui:
- ID no formato `GEO-XXXXXXXXXX`
- URL de verificação: `https://geo-explorer.dev/certificado/{ID}`
- Data de emissão no formato `DD/MM/AAAA`

---

## 🧪 Como executar os testes

### Rodar todos os testes

```bash
python testes/executar_testes.py
```

O runner descobre automaticamente todos os testes nas pastas `testes/unitarios/` e `testes/fluxo/`, exibe o resultado no terminal e salva um relatório detalhado em `testes/resultados.txt`.

### Rodar um arquivo específico

```bash
# Testes unitários do comando /trilha
python -m unittest testes/unitarios/test_trilha.py -v

# Testes unitários do comando /desafio
python -m unittest testes/unitarios/test_desafio.py -v

# Testes unitários do comando /certificado
python -m unittest testes/unitarios/test_certificado.py -v

# Teste de fluxo completo (jornada do explorador)
python -m unittest testes/fluxo/test_jornada_explorador.py -v
```

### Resultado atual

```
============================================================
  RELATÓRIO DE TESTES — GEO-EXPLORER
============================================================

  Total de testes : 122
  ✅ Aprovados    : 122
  ❌ Falhas       : 0
  💥 Erros        : 0
  📊 Cobertura    : 100.0%
  Meta >= 70%    : ATINGIDA ✅
============================================================
```

### Cobertura por módulo

| Arquivo de teste | Classes de teste | Total de testes |
|---|---|---|
| `test_trilha.py` | 5 — Carregamento, Busca, Estrutura, Formatação, Integridade JSON | 36 |
| `test_desafio.py` | 5 — Campos, Regras de Negócio, Tipos de Missão, Entrada/Saída, Desafio Lendário | 18 |
| `test_certificado.py` | 6 — Geração, Cálculos, Badges/Recompensa, ID/URL, Data, Entradas Inválidas | 30 |
| `test_jornada_explorador.py` | 4 — Etapa 1 (Trilha), Etapa 2 (Desafio), Etapa 3 (Certificado), Etapa 4 (Consistência) | 38 |
| **Total** | **20 classes** | **122 testes** |

---

## 🔧 Melhorias realizadas

Durante o desenvolvimento do Geo-Explorer com o IBM Bob, diversas melhorias foram incorporadas em relação a uma abordagem inicial mais simples:

### 1. Arquitetura orientada a dados
A fonte de verdade (`dados/geo_trilhas.json`) centraliza todas as informações das 12 trilhas. Os três comandos leem desse único arquivo, garantindo consistência total — o mesmo XP, badges e recompensa aparecem na trilha, no desafio e no certificado sem discrepâncias.

### 2. Busca tolerante a variações
A função `buscar_trilha` aceita qualquer combinação de maiúsculas/minúsculas e busca tanto no campo `tecnologia` quanto no campo `nome` da trilha. Isso permite que o usuário digite `/trilha java` ou `/trilha Galáxia Java` e obtenha o mesmo resultado.

### 3. Validação de entradas inválidas
Todos os comandos tratam entradas nulas, vazias ou inexistentes de forma explícita, retornando `None` em vez de lançar exceções — comportamento validado por testes dedicados na classe `TestEntradasInvalidas`.

### 4. Testes de fluxo end-to-end
Além dos testes unitários por comando, foi criado um teste de jornada completa (`test_jornada_explorador.py`) que simula o fluxo real de um explorador — `/trilha` → `/desafio` → `/certificado` — e valida a **consistência dos dados entre os três comandos**. Isso garante que a tecnologia, o nível, o XP e os badges sejam coerentes em toda a jornada.

### 5. Runner de testes com relatório
O arquivo `testes/executar_testes.py` foi criado com descoberta automática de testes, exibição formatada no terminal e geração de relatório persistido em `testes/resultados.txt`, facilitando auditorias futuras.

### 6. IDs únicos e verificáveis no certificado
Cada certificado gerado recebe um ID único no formato `GEO-XXXXXXXXXX` (10 caracteres alfanuméricos aleatórios) e uma URL de verificação associada. Os testes validam o formato, o tamanho e a unicidade entre certificados gerados sequencialmente.

### 7. Separação entre comandos fonte e comandos ativos
Os arquivos em `comandos/` são a fonte de desenvolvimento (onde edições acontecem). Os arquivos em `.bob/commands/` são os que o IBM Bob usa diretamente. O script `scripts/sync_comandos.py` mantém as duas pastas sincronizadas.

---

## 📚 O que aprendi durante o desafio

Mediante a tudo o que foi passado tive certeza que deveria ter começado mais cedo na minha vida, gostei muito do Bob e pretendo evoluir e aprender ainda mais. Dá pra criar coisas incríveis e no geral o curso foi ótimo. Aprendi a delegar prompts, ordens, funções e descobri um mundo de novas POSSIBILIDADES QUE NEM IMAGINAVA.

---

## 🤖 Desenvolvido com IBM Bob

O Geo-Explorer foi criado inteiramente com o apoio do **IBM Bob** — IA assistente para desenvolvimento de software da IBM.

> Repositório: [github.com/vinicioscaires/geo-explorer](https://github.com/vinicioscaires/geo-explorer)
