# project-code-test1

Este proyecto contiene las prácticas y entregas de python de mi magister de IA

## Entorno y ejecución

Se recomienda usar un entorno virtual para instalar dependencias (por ejemplo, `numpy`).

Pasos básicos:

1. Crear y activar el entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Actualizar herramientas de empaquetado e instalar dependencias:

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install numpy
```

3. Ejecutar un script de ejemplo (desde la raíz del proyecto):

```bash
.venv/bin/python semana_3/ejercicio_4.py
```

Notas:
- Si tu Python está gestionado por Homebrew y pip falla con PEP 668, usa el entorno virtual anterior o `python -m pip install --user <paquete>`.
- Añade `.venv/` a tu `.gitignore` para evitar subir el entorno virtual al repositorio.

Archivos útiles añadidos:

- `requirements.txt`: lista las dependencias del proyecto. Instálalas con:

```bash
python -m pip install -r requirements.txt
```

- `run.sh`: script helper que crea/activa `.venv`, instala dependencias y ejecuta `semana_3/ejercicio_4.py`.

Para usar `run.sh`:

```bash
chmod +x run.sh
./run.sh
```