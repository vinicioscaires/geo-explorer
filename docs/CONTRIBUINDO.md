# 🤝 Contribuindo com o Geo-Explorer

## Pré-requisitos

- IBM Bob instalado
- Python 3.10+
- Git

## Como rodar os testes

```bash
python testes/executar_testes.py
```

## Como adicionar uma nova trilha

1. Abra `dados/geo_trilhas.json`
2. Adicione um novo objeto no array `trilhas` seguindo o schema em `docs/ARQUITETURA.md`
3. Incremente o campo `total_trilhas`
4. Rode os testes: `python testes/executar_testes.py`

## Como editar um comando

1. Edite o arquivo em `comandos/<nome>.md`
2. Execute o script de sincronização:
   ```bash
   python scripts/sync_comandos.py
   ```
   Isso espelha automaticamente para `.bob/commands/`

## Níveis válidos

| Valor | Dificuldade |
|---|---|
| `Iniciante` | ⭐☆☆☆☆ |
| `Intermediário` | ⭐⭐⭐☆☆ |
| `Avançado` | ⭐⭐⭐⭐⭐ |

## Temas narrativos disponíveis

Aventura, Fantasia, Ficção Científica, Mistério, Medieval, Arqueologia, Cyberpunk, Mitologia, Natureza, Marítimo — e quaisquer outros que você imaginar!
