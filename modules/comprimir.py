import zipfile as zip
from modules.verificador_seguridad import verificador_seguridad

def comprimir(config, extensions, carpeta_a_ordenar, carpetas_intocables):   #
    # Comprobamos uno a uno cada elemento de la carpeta
    archivos_comprimidos = []
    for elemento in carpeta_a_ordenar.rglob("*"):
        if elemento.is_file() and verificador_seguridad(elemento, carpetas_intocables):# Comprobamos que elemento sea un archivo y que no esté en la carpeta del proyecto
            if elemento.stat().st_size >= (config["compresion"]["tamaño en MB"]*1000000) and elemento.suffix not in extensions["Archivos comprimidos"]:   # Multiplicamos por 1*10^6 para expresarlo en bytes
                nuevo_nombre = elemento.with_suffix(".zip")
                with zip.ZipFile(nuevo_nombre, "w") as archivo_comprimido:
                    archivo_comprimido.write(elemento, arcname=elemento.name)
                    archivos_comprimidos.append(nuevo_nombre.name)
                elemento.unlink()
    return archivos_comprimidos