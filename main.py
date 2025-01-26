# ==================== imports ====================
import datetime
import json
from pathlib import Path

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
    return diccionario

# ==================== 2 ====================
def clasificar_archivos(diccionario, config, extensions):   #
    # Comprimimos los archivos mas grandes de 50MB (predeterminado, se cambia en config)
    if config["compresion"]["comprimir archivos"]: # Comprobamos la configuración para hacer o no la compresión de archivos
        # Comprobamos uno a uno cada elemento de la carpeta
        for elemento in carpeta_a_ordenar.rglob("*"):
            if elemento.is_file() and carpeta_programa.name not in str(elemento):# Comprobamos que elemento sea un archivo y que no esté en la carpeta del proyecto
                if elemento.stat().st_size >= (config["compresion"]["tamaño en MB"]*1000000):   # Multiplicamos por 1*10^6 para expresarlo en bytes
                    nuevo_nombre = elemento.with_suffix(".zip")
                    with zip.ZipFile(elemento.with_suffix(".zip"), "w") as archivo_comprimido:
                        archivo_comprimido.write(elemento, arcname=elemento.name)
                    elemento.unlink()
            

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
    clasificar_archivos(diccionario_carpetas_true, configuracion, extensiones)
    # 3. Creamos las carpetas y movemos los archivos
    movimiento_carpetas()
    # 4. Eliminamos las carpetas vacías
    eliminar_carpetas_vacias()
    # 5. Registramos los cambios
    registro_logs()


if __name__ == "__main__":
    main()