from pathlib import Path
directorio = Path("carpeta pruebas/carpeta1 copy")


for elemento in carpeta_a_ordenar.rglob("*"):
        if elemento.is_file() and carpeta_programa.name not in str(elemento):