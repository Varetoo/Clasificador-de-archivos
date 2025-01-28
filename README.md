CLASIFICADOR DE ARCHIVOS
Este mini-proyecto está enfocado en automatizar una tarea del día a día de manera fácil y sencilla.
Al ejecutar el script [main.py] se organiza todo el contenido de la carpeta donde se encuentre la carpeta del programa dependiendo de su extensión.

Funcionamiento principal del programa:
1. Se carga la configuración del arcchivo config.json.
2. Se clasifican los archivos según sus extensiones en las carpetas cuya configuración esté en true.
3. Se crean las carpetas mencionadas anteriormente y se reordenan todos los archivos.
4. Se eliminan las carpetas que no correspondan al programa y que estén vacías.
Extra. Los cambios que haya efectuado el programa se guardarán en el archivo log.

El script es configurable y se puede ajustar más a tus necesidades desde el archivo config.
     Hay 4 apartados configurables desde el archivo:
     "carpetas": Se coloca true/false según se quiera o no tener la posibilidad de que se alamacenen ese tipo de arhivos en esa carpeta, si se encuentra en false, los arhcivos correspondientes a esa carpeta se alamcenarán en una carpeta llamada "Otros"
     
     "renombre de archivos": Cuando dos arhivos o más tienen el mismo nombre, son renombrados añadiendo un numero que indica que hay mas de un archivo con el mismo nombre, es decir si hay más de un archivo con el nombre ejemplo.txt, se renombrarán como: ejemplo{1}.txt, ejemplo{2}.txt, ...
     En los apartados left y right se pueden modificar el aspecto de los decoradores ->{}.
     
     "carpeta logs": true/false si quieres o no que haya un archivo.log que registre los cambios del programa
     
     "compresion": 
          "comprimir archivos": true/false si quieres que el porgrama comprima o no los archivos que superen el limite asignado en;
          "tamaño en MB": numero entero del tamaño en MB que debe ser superado para que se compriman los archivos siempre y cuando esté activada la configuarión anterior.