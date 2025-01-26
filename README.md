CLASIFICADOR DE ARCHIVOS
Este mini-proyecto está enfocado en automatizar una tarea del día a día de manera fácil y sencilla.
Al ejecutar el script se organiza todo el contenido de la carpeta deseada dependiendo de su extensión en diferentes carpetas.

Funcionamiento principal del programa:
1. Crea las carpetas en las que se clasificarán los archivos (Si no existen ya).
2. Archivo por archivo se comprueban las extensiones.
2.1. Si el nombre de un archivo se repite, va renombrando los archivos.
     Antes: archivo.txt, archivo.txt, archivo.txt. Después: archivo(1).txt, archivo(2).txt, archivo(3).txt.
2.2. Si un archivo es muy grande lo convierte en un comprime a .zip para ahorrar espacio
3. Se almacenan los archivos en sus carpetas correspondientes.
4. Se guardan los cambios en el archivo log.txt

El script es configurable y se puede ajustar más a tus necesidades desde el archivo config