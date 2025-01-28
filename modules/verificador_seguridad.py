def verificador_seguridad(ruta, carpetas_intocables):   # Función que verifica que la ruta no se encuentra en la lista de carpetas intocables
    
    for i, parte in enumerate(ruta.parts):
        if parte == carpetas_intocables[0]:
            carpeta_ruta = ruta.parts[i+1]
            break
    # Verificamos si la carpeta/archivo que se está analizando forma parte de la lista de carpetas intocables
    for nombre_carpeta in carpetas_intocables[1:]:
        if nombre_carpeta == carpeta_ruta: return False
    return True
    # True si es seguro, False si es una ruta intocable