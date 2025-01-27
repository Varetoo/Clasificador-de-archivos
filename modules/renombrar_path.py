def renombrar_path(config, lista_path):   #
    # Creamos un diccionario para saber que archivos tienen el mismo nombre y cuantas veces se repiten
    diccionario_repetidos = {}
    for elemento in lista_path:
        if elemento.name not in diccionario_repetidos:
            diccionario_repetidos.update({elemento: 1})
        else:
            diccionario_repetidos[elemento] += 1
    # Cambiamos los nombre de los archivos repetidos solo a los repetidos
    for clave, valor in diccionario_repetidos.items():
        if valor > 1:   # Para solo cambiar el nombre de los repetidos
            for i in range(valor):
                lista_path.remove(clave)
                nombre, extension = clave.split(".")
                decorador_izq  = config["renombre de archivos"]["left"]
                decorador_dcho = config["renombre de archivos"]["right"]
                nuevo_nombre = nombre+decorador_izq+str(i+1)+decorador_dcho +"."+extension
                lista_path.append(nuevo_nombre)