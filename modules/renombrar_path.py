def renombrar_path(config, lista_path):   #
    # Creamos un diccionario para saber que archivos tienen el mismo nombre y cuantas veces se repiten
    diccionario_repetidos = {} # nombre_archivo: lista con rutas con ese nombre
    for elemento in lista_path:
        if elemento.name not in diccionario_repetidos:
            diccionario_repetidos.update({elemento.name: [elemento]})
        else:
            diccionario_repetidos[elemento.name].append(elemento)
    # Cambiamos los nombre de los archivos repetidos solo a los repetidos
    lista_path = {}
    decorador_izq  = config["renombre de archivos"]["left"]
    decorador_dcho = config["renombre de archivos"]["right"]
    for path_repetidos_lista in diccionario_repetidos.values():
        for i, root in enumerate(path_repetidos_lista, start=1):
            if len(path_repetidos_lista) > 1:   # Para solo cambiar el nombre de los repetidos
                nuevo_nombre_ruta = f"{root.stem}{decorador_izq}{i}{decorador_dcho}{root.suffix}"
                lista_path.update({root:nuevo_nombre_ruta})
            else: # En el caso de que no se repita la ruta es la misma
                lista_path.update({root:root.name})
            
    
    return lista_path