from pathlib import Path

diccionario = {
    "Documentos": [".txt", ".pdf"],
    "Video": [".vid", ".mp4"]
}

diccionario_final = {
    "Documentos": [],
    "Video": 
}

archivo = Path("archivo.txt")

for nombre_carpeta, lista_extensiones in diccionario.items():
    if archivo.suffix in lista_extensiones:
        diccionario_final[nombre_carpeta].append()