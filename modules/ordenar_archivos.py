def ordenar_archivos(lista_path, extensions, diccionario):  # Clasifica lista path en diccionario y devuelve diccionario
    for root, nombre_root in lista_path.items():
        encontrada_extension = False
        for nombre_carpeta in diccionario:
            if nombre_carpeta != "Otros":
                if root.suffix in extensions[nombre_carpeta]:
                    diccionario[nombre_carpeta].update({root:nombre_root})
                    encontrada_extension = True
                    break
        if encontrada_extension == False: diccionario["Otros"].update({root:nombre_root})
    return diccionario