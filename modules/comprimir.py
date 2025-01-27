def comprimir(config, carpeta_a_ordenar, carpeta_programa):   #
    # Comprobamos uno a uno cada elemento de la carpeta
    for elemento in carpeta_a_ordenar.rglob("*"):
        if elemento.is_file() and carpeta_programa.name not in str(elemento):# Comprobamos que elemento sea un archivo y que no esté en la carpeta del proyecto
            if elemento.stat().st_size >= (config["compresion"]["tamaño en MB"]*1000000):   # Multiplicamos por 1*10^6 para expresarlo en bytes
                nuevo_nombre = elemento.with_suffix(".zip")
                with zip.ZipFile(nuevo_nombre, "w") as archivo_comprimido:
                    archivo_comprimido.write(elemento, arcname=elemento.name)
                elemento.unlink()
