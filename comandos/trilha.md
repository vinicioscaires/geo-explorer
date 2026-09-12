---
description: Exibe o plano de exploração de uma trilha do Geo-Explorer
argument-hint: <tecnologia>
---

O explorador quer consultar a trilha de **$1** no Geo-Explorer.

Leia o arquivo `dados/geo_trilhas.json` na raiz do projeto e localize a trilha cuja propriedade `tecnologia` corresponda (de forma aproximada, ignorando maiúsculas/minúsculas) ao valor informado: **$1**.

Se não encontrar nenhuma trilha correspondente, liste todas as tecnologias disponíveis no arquivo e convide o explorador a escolher uma.

Se encontrar, apresente o plano de exploração no seguinte formato Markdown:

---

# 🗺️ Trilha de Exploração — {nome da trilha}

> _{tema da trilha}_

**Plataforma:** Geo-Explorer  
**Tecnologia:** {tecnologia}  
**Nível:** {nivel}  
**Módulos:** {numero_de_modulos}  
**XP Total:** {xp_total} XP  
**Duração Estimada:** {duracao_horas} horas  

---

## 🧭 Módulos da Jornada

Gere uma lista numerada com {numero_de_modulos} módulos progressivos e temáticos para a tecnologia {tecnologia} no nível {nivel}. Use o tema "{tema}" como inspiração para dar nomes criativos a cada módulo. Cada módulo deve ter:
- Nome temático do módulo
- Descrição objetiva do que será aprendido (1 linha)
- Estimativa de duração em horas

---

## ⚔️ Missões Especiais

Liste as missões especiais da trilha, cada uma com uma breve descrição do desafio que representa:
{missoes_especiais}

---

## 🏅 Badges da Jornada

Liste as badges em formato de checklist (não marcadas):
{badges}

---

## 💡 Habilidades Desenvolvidas

Liste as habilidades que o explorador dominará ao concluir esta trilha:
{habilidades}

---

## 🎁 Recompensa Final

> 🏆 {recompensa_final}

---

> 🧭 Ao concluir todos os módulos, use `/certificado <seu nome> <tecnologia>` para gerar seu certificado de explorador!  
> ⚔️ Quer testar seus conhecimentos? Use `/desafio <tecnologia> <nivel>` para receber uma missão de código!
