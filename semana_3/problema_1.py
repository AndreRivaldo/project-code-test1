import argparse
import sys
import numpy as np

def todos_contra_profesor(num_students: int, fichas: int, seed: int | None = None) -> bool:
    """Simula el juego "Todos contra el profesor".

    Args:
        num_students: Número de estudiantes.
        fichas: Cantidad inicial de fichas para cada jugador.
        seed: Semilla opcional para reproducibilidad.

    Returns:
        True si los estudiantes ganan (el profesor llega a cero fichas);
        False si pierde al menos un estudiante primero.
    """
    if num_students <= 0:
        raise ValueError("El número de estudiantes debe ser mayor que cero.")
    if fichas <= 0:
        raise ValueError("La cantidad de fichas debe ser mayor que cero.")

    rng = np.random.default_rng(seed)
    student_fichas = np.full(num_students, fichas, dtype=int)
    prof_fichas = fichas

    while True:
        prof_roll = rng.integers(1, 7)
        student_rolls = rng.integers(1, 7, size=num_students)

        # Cada estudiante pierde una ficha si el profesor saca mayor.
        student_losses = prof_roll > student_rolls
        student_fichas -= student_losses.astype(int)

        # El profesor pierde una ficha por cada estudiante que saque mayor.
        prof_losses = np.count_nonzero(student_rolls > prof_roll)
        prof_fichas -= prof_losses

        if prof_fichas <= 0:
            return True
        if np.any(student_fichas <= 0):
            return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simula el juego 'Todos contra el profesor' usando NumPy."
    )
    parser.add_argument(
        "num_students",
        nargs="?",
        type=int,
        help="Número de estudiantes en el juego.",
    )
    parser.add_argument(
        "fichas",
        nargs="?",
        type=int,
        help="Cantidad de fichas inicial por jugador.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Semilla opcional para reproducibilidad.",
    )
    args = parser.parse_args()

    if args.num_students is None or args.fichas is None:
        try:
            args.num_students = int(input("Ingrese el número de estudiantes: "))
            args.fichas = int(input("Ingrese la cantidad de fichas inicial por jugador: "))
        except ValueError:
            print("Por favor ingrese valores enteros válidos.")
            sys.exit(1)
        except EOFError:
            print("No se recibieron datos de entrada. Ejecute el script con argumentos o en modo interactivo.")
            sys.exit(1)

    resultado = todos_contra_profesor(args.num_students, args.fichas, args.seed)
    if resultado:
        print("Resultado: los estudiantes ganan 5 décimas en el examen.")
    else:
        print("Resultado: los estudiantes pierden 1 décima en el examen.")
