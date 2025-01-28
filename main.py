# ==================== imports ====================
import logging
import json
import sys
from pathlib import Path
from modules.renombrar_path import renombrar_path
from modules.ordenar_archivos import ordenar_archivos
from modules.comprimir import comprimir
from modules.verificador_seguridad import verificador_seguridad

# ==================== Paths ====================
carpeta_programa = Path(__file__).parent
carpeta_a_ordenar = carpeta_programa.parent
carpetas_intocables = [carpeta_a_ordenar.name, carpeta_programa.name]   # Lista con carpetas que no van a ser ordenadas/eliminadas/etc

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
        logging.critical("Ha ocurrido un error al cargar los datos")
        sys.exit()
    
    return diccionario_configuracion, diccionario_extensiones

def crear_diccionario(config):   #
    diccionario = {}
    carpetas = config["carpetas"]
    for clave, valor in carpetas.items():
        if valor:
            diccionario.update({clave:{}})
    diccionario.update({"Otros": {}})
    return diccionario

# ==================== 2 ====================
def clasificar_archivos(diccionario, config, extensions):   #
    # Comprimimos los archivos mas grandes de 50MB (predeterminado, se cambia en config)
    if config["compresion"]["comprimir archivos"]: # Comprobamos la configuración para hacer o no la compresión de archivos
        archivos_comprimidos = comprimir(config, extensions, carpeta_a_ordenar, carpetas_intocables)
        if len(archivos_comprimidos) == 0: logging.info("No se comprimieron archivos")
        else:
            for nombre_archivo in archivos_comprimidos: logging.info(f"Archivo comprimido: {nombre_archivo}")
    # Almacenamos los Path de todos los archivos en un diccionario
    lista_path = {}
    for elemento in carpeta_a_ordenar.rglob("*"):
        if verificador_seguridad(elemento, carpetas_intocables): # Comprobamos que 'elemento' no esté en la carpeta del proyecto
            if elemento.is_file():
                lista_path.update({elemento:""})
    # Renombramos los Path si hay repetidos y seguimos la configuración para el formato
    lista_path = renombrar_path(config, lista_path)
    # Ordenamos los archivos y los añadimos al diccionario
    diccionario = ordenar_archivos(lista_path, extensions, diccionario)
    
    return diccionario 

# ==================== 3 ====================
def movimiento_carpetas(diccionario):   #
    # Creamos las carpetas y movemos los archivos
    for nombre_carpeta, diccionario_path in diccionario.items():
        if len(diccionario_path) > 0: # Evitamos crear una carpeta que se vaya a quedar vacía
            # Creamos la carpeta
            carpeta = Path(f"{carpeta_a_ordenar}/{nombre_carpeta}")
            carpeta.mkdir(exist_ok=True)    # Crea la carpeta a no ser que ya exista
            # Añadimos la carpeta a intocable para que no se modifique nada de ellas ya
            carpetas_intocables.append(carpeta.name)
            # Introducimos los archivos correspondientes en la carpeta
            for root in diccionario_path:
                ruta_completa = ""
                for parte in root.parts[1:]:
                    ruta_completa += "/"+parte
                    if parte == carpeta_a_ordenar.name: break
                # Movemos el archivo
                root.replace(f"{ruta_completa}/{nombre_carpeta}/{diccionario_path[root]}")
    

# ==================== 4 ====================
def eliminar_carpetas_vacias(carpeta):   #
    global eliminado
    for elemento in carpeta.iterdir():
        if verificador_seguridad(elemento, carpetas_intocables):  # Comprobamos que no se esté mirando algun elemento de las carpetas intocables
            if not elemento.is_dir(): # Si encontramos un archivo, detenemos el programa
                raise FileExistsError
            elif elemento.is_dir():
                try: elemento.rmdir()
                except OSError: # Si hubiera una carpeta dentro de la carpeta usamos la funcion de manera recursiva
                    eliminado = False
                    eliminar_carpetas_vacias(elemento)

# ==================== MAIN ====================
def main():
    # 0. Configuramos el logging para registrar los cambios
    logging.basicConfig(filename="log.log", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s", encoding="utf-8")
    logging.info("Iniciando programa")
    
    # 1. Cargar configuración
    logging.debug("Cargando configuración...")
    configuracion, extensiones = cargar_datos()
    diccionario_carpetas_true = crear_diccionario(configuracion)
    logging.debug("Proceso completado!")
    
    # 2. Clasificamos archivos
    logging.debug("Clasificando archivos...")
    diccionario_carpetas_true = clasificar_archivos(diccionario_carpetas_true, configuracion, extensiones)
    logging.debug("Proceso completado!")
        
    # 3. Creamos las carpetas y movemos los archivos
    logging.debug("Creando carpetas y moviendo archivos...")
    movimiento_carpetas(diccionario_carpetas_true)
    logging.debug("Proceso completado!")
    
    # 4. Eliminamos las carpetas vacías
    logging.debug("Eliminando carpetas vacías...")
    global eliminado
    eliminado = False
    while eliminado == False:
        eliminado = True
        try: eliminar_carpetas_vacias(carpeta_a_ordenar)
        except FileExistsError:
            print("hay un archivo dentro de una carpeta que se queria eliminar, error") 
            break
    logging.debug("Proceso completado!")

if __name__ == "__main__":
    main()
    logging.info("Programa finalizado")
