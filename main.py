# ==================== imports ====================
import datetime
import json
from pathlib import Path
from modules.comprimir import comprimir
from modules.renombrar_path import renombrar_path

# ==================== Paths ====================
carpeta_programa = Path(__file__).parent
carpeta_a_ordenar = carpeta_programa.parent

# ==================== 1 ====================
def cargar_datos():   #
    try:
        # Leemos el archivo de configuración
        with open("config.json", "r", encoding="utf-8") as archivo:
            diccionario_configuracion = json.load(archivo)
            del diccionario_configuracion["renombre de archivos"]["_ejemplo"]
        # Leemos el archivo de extensiones
        with open("extensiones.json", "r", encoding="utf-8") as archivo:
            diccionario_extensiones = json.load(archivo)
    except:
        print("Ha ocurrido un error leyendo los archivos config o extensiones")
    
    return diccionario_configuracion, diccionario_extensiones

def crear_diccionario(config):   #
    diccionario = {}
    carpetas = config["carpetas"]
    for clave, valor in carpetas.items():
        if valor:
            diccionario.update({clave:[]})
    diccionario.update({"Otros": []})
    return diccionario

# ==================== 2 ====================
def clasificar_archivos(diccionario, config, extensions):   #
    # Comprimimos los archivos mas grandes de 50MB (predeterminado, se cambia en config)
    if config["compresion"]["comprimir archivos"]: # Comprobamos la configuración para hacer o no la compresión de archivos
        comprimir(config, carpeta_a_ordenar, carpeta_programa)
    # Almacenamos los Path de todos los archivos en el array
    lista_path = []
    for elemento in carpeta_a_ordenar.rglob("*"):
        if elemento.is_file() and carpeta_programa.name not in str(elemento):# Comprobamos que elemento sea un archivo y que no esté en la carpeta del proyecto
            lista_path.append(elemento)
    # Renombramos los Path si hay repetidos y seguimos la configuración para el formato
    renombrar_path(config, lista_path) 
    # Ordenamos los archivos y los añadimos al diccionario
    for elemento in lista_path:
        encontrado = False
        for nombre_carpeta, lista_extensiones in extensions.items():
            if elemento.suffix in lista_extensiones:
                diccionario[nombre_carpeta].append(elemento)
                encontrado = True
                break
        if encontrado == False: diccionario["Otros"].append(elemento)
        

    return diccionario

# ==================== 3 ====================
def movimiento_carpetas(diccionario):   #
    
    pass

# ==================== 4 ====================
def eliminar_carpetas_vacias():   #
    
    pass

# ==================== 5 ====================
def registro_logs():   #
    
    pass

# ==================== MAIN ====================
def main():
    # 1. Cargar configuración
    configuracion, extensiones = cargar_datos()
    diccionario_carpetas_true = crear_diccionario(configuracion)
    # 2. Clasificamos archivos
    diccionario_carpetas_true = clasificar_archivos(diccionario_carpetas_true, configuracion, extensiones)
    # 3. Creamos las carpetas y movemos los archivos
    movimiento_carpetas()
    # 4. Eliminamos las carpetas vacías
    eliminar_carpetas_vacias()
    # 5. Registramos los cambios
    registro_logs()


if __name__ == "__main__":
    main()