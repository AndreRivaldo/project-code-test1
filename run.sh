#!/usr/bin/env bash
set -euo pipefail

# Crear y activar venv si no existe
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate

# Instalar dependencias
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

# Ejecutar el script de ejemplo
python semana_3/ejercicio_4.py
