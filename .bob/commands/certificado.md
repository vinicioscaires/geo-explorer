---
description: Gera um certificado de explorador para quem concluiu uma trilha do Geo-Explorer
argument-hint: <seu-nome> <tecnologia>
---

O explorador completou uma jornada e merece seu certificado no Geo-Explorer.

**Nome do explorador:** $1  
**Trilha concluída:** $2

Leia o arquivo `dados/geo_trilhas.json` e localize a trilha correspondente a **$2**. Use os dados reais (nível, XP total, badges, habilidades, recompensa final, duracao_horas). Caso a trilha não seja encontrada, crie valores plausíveis e temáticos.

Gere um certificado épico e comemorativo em Markdown, seguindo o formato abaixo:

---

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            🌍  CERTIFICADO DE EXPLORADOR  🌍                          ║
║                                                                      ║
║                     G E O - E X P L O R E R                         ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

# 📜 Certificado de Explorador

**O Geo-Explorer** — plataforma de exploração e aprendizagem — certifica que o(a) explorador(a)

---

## 🧭 $1

concluiu com bravura e dedicação a trilha:

---

# 🗺️ $2

---

**Nível:** {nivel da trilha}  
**Horas de Jornada:** {duracao_horas} horas  
**XP Conquistado:** {xp_total} XP  
**Data de Conclusão:** {data de hoje no formato DD/MM/AAAA}  

---

## 🏅 Badges Conquistadas

Liste todas as badges da trilha como itens marcados com ✅:

- ✅ {badge 1}
- ✅ {badge 2}
- ✅ {badge N}

---

## 🎁 Recompensa Desbloqueada

> 🏆 {recompensa_final da trilha}

---

## 💡 Habilidades Dominadas

Liste as habilidades da trilha como competências conquistadas pelo explorador $1, de forma celebratória e motivacional.

---

## 🌟 Avaliação da Jornada

Escreva uma avaliação épica e motivacional de 3 a 4 frases sobre a conquista de $1, conectando o tema da trilha com o impacto real da tecnologia $2 no mercado de trabalho. Use linguagem inspiradora, digna de um verdadeiro explorador.

---

**🔑 ID do Certificado:** `GEO-{gere um código alfanumérico aleatório de 10 caracteres em maiúsculas}`  
**🔗 Verificação:** `https://geo-explorer.dev/certificado/{mesmo código}`  
**🗓️ Emitido em:** {data de hoje no formato DD/MM/AAAA}  

---

```
  ____________________________________________
 |                                            |
 |   Assinado pelo Conselho Geo-Explorer      |
 |   Válido para fins de portfólio            |
 |   Este é um certificado fictício           |
 |   gerado com IBM Bob 🤖                     |
 |____________________________________________|
```

---

> 🎉 Parabéns, **$1**! Sua jornada em **$2** está marcada na história do Geo-Explorer!  
> ⚔️ Pronto para o próximo desafio? Use `/desafio $2 Avançado` e vá além dos limites!
