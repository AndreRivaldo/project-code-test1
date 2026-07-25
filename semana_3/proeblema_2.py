import argparse
import numpy as np


def generar_imagen_prueba(shape=(100, 100), seed=42):
    """Genera una imagen en escala de grises sintética con ruido base."""
    rng = np.random.default_rng(seed)
    alto, ancho = shape
    y, x = np.indices((alto, ancho), dtype=np.float32)
    imagen = 90 + 0.4 * x + 0.2 * y + rng.normal(0, 12, size=(alto, ancho))
    imagen = np.clip(imagen, 0, 255).astype(np.uint8)
    return imagen, rng


def introducir_defectos(imagen, rng):
    """Inserta cuatro defectos sintéticos en la imagen para demostración."""
    imagen_defectuosa = imagen.copy()

    # 1. Pixeles muertos: valores extremos permanentes.
    coords_muertos = rng.choice(imagen.size, size=40, replace=False)
    filas, columnas = np.unravel_index(coords_muertos, imagen.shape)
    imagen_defectuosa[filas, columnas] = np.where(rng.integers(0, 2, size=40) == 0, 0, 255)

    # 2. Pixeles calientes: valores muy altos respecto a los vecinos.
    coords_calientes = rng.choice(imagen.size, size=25, replace=False)
    filas, columnas = np.unravel_index(coords_calientes, imagen.shape)
    imagen_defectuosa[filas, columnas] = np.clip(imagen[filas, columnas] + 80, 0, 255)

    # 3. Ruido sal y pimienta: píxeles aislados extremos.
    coords_ruido = rng.choice(imagen.size, size=20, replace=False)
    filas, columnas = np.unravel_index(coords_ruido, imagen.shape)
    imagen_defectuosa[filas, columnas] = np.where(rng.integers(0, 2, size=20) == 0, 0, 255)

    # 4. Región de bajo contraste: bloque de 10x10 casi uniforme.
    alto, ancho = imagen.shape
    inicio_fila = rng.integers(0, alto - 10)
    inicio_col = rng.integers(0, ancho - 10)
    valor_promedio = int(np.mean(imagen[inicio_fila : inicio_fila + 10, inicio_col : inicio_col + 10]))
    imagen_defectuosa[
        inicio_fila : inicio_fila + 10,
        inicio_col : inicio_col + 10,
    ] = np.full((10, 10), valor_promedio, dtype=np.uint8)

    return imagen_defectuosa


def detectar_pixeles_muertos(imagen):
    """Detecta pixeles con valores extremos (0 o 255)."""
    return np.argwhere((imagen == 0) | (imagen == 255))


def corregir_pixeles_muertos(imagen):
    """Reemplaza pixeles muertos por el valor mediano de su vecindario."""
    imagen_corr = imagen.copy()
    for fila, col in np.argwhere((imagen_corr == 0) | (imagen_corr == 255)):
        vecindario = imagen_corr[max(0, fila - 1) : min(imagen.shape[0], fila + 2), max(0, col - 1) : min(imagen.shape[1], col + 2)]
        valores = vecindario[(vecindario != 0) & (vecindario != 255)]
        if valores.size == 0:
            reemplazo = int(np.median(imagen_corr))
        else:
            reemplazo = int(np.median(valores))
        imagen_corr[fila, col] = reemplazo
    return imagen_corr


def detectar_pixeles_calientes(imagen, diferencia=50):
    """Detecta pixeles mucho más brillantes que sus vecinos."""
    posiciones = []
    for fila in range(1, imagen.shape[0] - 1):
        for col in range(1, imagen.shape[1] - 1):
            vecindario = imagen[fila - 1 : fila + 2, col - 1 : col + 2].ravel()
            vecindario = np.delete(vecindario, 4)
            if imagen[fila, col] - np.median(vecindario) > diferencia:
                posiciones.append((fila, col))
    return posiciones


def corregir_pixeles_calientes(imagen, posiciones):
    """Reemplaza pixeles calientes por la mediana de sus vecinos."""
    imagen_corr = imagen.copy()
    for fila, col in posiciones:
        vecindario = imagen_corr[fila - 1 : fila + 2, col - 1 : col + 2].ravel()
        vecindario = np.delete(vecindario, 4)
        imagen_corr[fila, col] = int(np.median(vecindario))
    return imagen_corr


def detectar_ruido_sal_pimienta(imagen, rango_medio=(80, 180)):
    """Detecta píxeles extremos aislados rodeados de valores medios."""
    posiciones = []
    bajo, alto = rango_medio
    for fila in range(1, imagen.shape[0] - 1):
        for col in range(1, imagen.shape[1] - 1):
            valor = imagen[fila, col]
            if valor not in (0, 255):
                continue
            vecindario = imagen[fila - 1 : fila + 2, col - 1 : col + 2].ravel()
            vecindario = np.delete(vecindario, 4)
            if np.all((vecindario >= bajo) & (vecindario <= alto)):
                posiciones.append((fila, col))
    return posiciones


def corregir_ruido_sal_pimienta(imagen, posiciones):
    """Reemplaza el ruido sal-pimienta por la mediana del vecindario."""
    imagen_corr = imagen.copy()
    for fila, col in posiciones:
        vecindario = imagen_corr[fila - 1 : fila + 2, col - 1 : col + 2].ravel()
        vecindario = np.delete(vecindario, 4)
        imagen_corr[fila, col] = int(np.median(vecindario))
    return imagen_corr


def detectar_regiones_bajo_contraste(imagen, ventana=(10, 10), umbral=30):
    """Detecta ventanas de 10x10 con rango menor a 30."""
    alto_ventana, ancho_ventana = ventana
    posiciones = []
    for fila in range(0, imagen.shape[0] - alto_ventana + 1):
        for col in range(0, imagen.shape[1] - ancho_ventana + 1):
            bloque = imagen[fila : fila + alto_ventana, col : col + ancho_ventana]
            if np.ptp(bloque) < umbral:
                posiciones.append((fila, col))
    return posiciones


def corregir_regiones_bajo_contraste(imagen, posiciones, ventana=(10, 10)):
    """Promedia cada región de bajo contraste para corregirla."""
    imagen_corr = imagen.copy()
    alto_ventana, ancho_ventana = ventana
    for fila, col in posiciones:
        bloque = imagen_corr[fila : fila + alto_ventana, col : col + ancho_ventana]
        remplazo = int(np.mean(bloque))
        imagen_corr[fila : fila + alto_ventana, col : col + ancho_ventana] = remplazo
    return imagen_corr


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detección y corrección de defectos en sensores de imagen con NumPy.")
    parser.add_argument("--seed", type=int, default=42, help="Semilla para generar la imagen de prueba.")
    parser.add_argument("--alto", type=int, default=100, help="Altura de la imagen sintética.")
    parser.add_argument("--ancho", type=int, default=100, help="Ancho de la imagen sintética.")
    args = parser.parse_args()

    if args.alto < 10 or args.ancho < 10:
        raise ValueError("El alto y el ancho deben ser mayores o iguales a 10.")

    imagen_base, rng = generar_imagen_prueba((args.alto, args.ancho), seed=args.seed)
    imagen_defectuosa = introducir_defectos(imagen_base, rng)

    pixeles_muertos = detectar_pixeles_muertos(imagen_defectuosa)
    pixeles_calientes = detectar_pixeles_calientes(imagen_defectuosa)
    ruido_sal_pimienta = detectar_ruido_sal_pimienta(imagen_defectuosa)
    regiones_bajo_contraste = detectar_regiones_bajo_contraste(imagen_defectuosa)

    imagen_corr = corregir_pixeles_muertos(imagen_defectuosa)
    imagen_corr = corregir_pixeles_calientes(imagen_corr, pixeles_calientes)
    imagen_corr = corregir_ruido_sal_pimienta(imagen_corr, ruido_sal_pimienta)
    imagen_corr = corregir_regiones_bajo_contraste(imagen_corr, regiones_bajo_contraste)

    print("Análisis de defectos detectados:")
    print(f"- Pixeles muertos: {len(pixeles_muertos)}")
    print(f"- Pixeles calientes: {len(pixeles_calientes)}")
    print(f"- Ruido sal y pimienta: {len(ruido_sal_pimienta)}")
    print(f"- Regiones de bajo contraste: {len(regiones_bajo_contraste)}")
    print("\nImagen corregida generada con éxito.")
    print(f"Rango original: [{int(imagen_base.min())}, {int(imagen_base.max())}]")
    print(f"Rango corregido: [{int(imagen_corr.min())}, {int(imagen_corr.max())}]")
