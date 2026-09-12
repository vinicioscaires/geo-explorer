#!/usr/bin/env python3
"""
scripts/sync_comandos.py

Sincroniza comandos/ → .bob/commands/
Execute após editar qualquer arquivo em comandos/.

Uso:
    python scripts/sync_comandos.py
"""

import shutil
from pathlib import Path

ROOT  = Path(__file__).parent.parent
SRC   = ROOT / "comandos"
DEST  = ROOT / ".bob" / "commands"

DEST.mkdir(parents=True, exist_ok=True)

arquivos = list(SRC.glob("*.md"))
for md in arquivos:
    shutil.copy2(md, DEST / md.name)
    print(f"  ✅ {md.name} → .bob/commands/")

print(f"\n{len(arquivos)} comando(s) sincronizado(s).")
