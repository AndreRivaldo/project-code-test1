#!/usr/bin/env bash
set -euo pipefail

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

echo "Ejecutando ejercicios no interactivos de semana_3..."
.venv/bin/python semana_3/ejercicio_3.py
.venv/bin/python semana_3/ejercicio_4.py
.venv/bin/python semana_3/ejercicio_6.py
.venv/bin/python semana_3/ejercicio_7.py

cat <<'EOF'
Nota: los siguientes ejercicios son interactivos y se deben ejecutar manualmente:
- .venv/bin/python semana_3/ejercicio1.py
- .venv/bin/python semana_3/ejercicio_2.py
- .venv/bin/python semana_3/ejercicio_8.py
EOF
