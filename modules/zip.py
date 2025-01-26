from pathlib import Path
import zipfile as zip




carpeta = Path("carpeta_prueba")
for archivo in carpeta.iterdir():
    if archivo.stat().st_size >= 30000:
        nuevo_nombre = f"{carpeta}/{archivo.stem}-comprimido.zip"
        with zip.ZipFile(nuevo_nombre, "w") as archivo_comprimido:
            archivo_comprimido.write(archivo, arcname=archivo.name)
        archivo.unlink()
