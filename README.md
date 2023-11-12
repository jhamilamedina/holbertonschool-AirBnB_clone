

Introducción:

AirBnB clone - The console 

Proyecto de equipo para construir un clone [AirBnB](https://www.airbnb.com/)
Este es el Primer Proyecto en grupo en las cuales vamos a utilizar diferentes funciones
y conceptos nuevos.

Primer paso: escriba un intérprete de comandos para administrar sus objetos AirBnB.

Este es el primer paso hacia la creación de su primera aplicación web completa: el clon de AirBnB. Este primer paso es muy importante porque utilizará lo que cree durante este proyecto con todos los demás proyectos siguientes: plantillas HTML/CSS, almacenamiento de bases de datos, API, integración front-end...

Cada tarea está vinculada y le ayudará a:

Implemente una clase principal (llamada BaseModel) para encargarse de la inicialización, serialización y deserialización de sus instancias futuras.
cree un flujo simple de serialización/deserialización: Instancia <-> Diccionario <-> Cadena JSON <-> archivo
crear todas las clases utilizadas para AirBnB (Usuario, Estado, Ciudad, Lugar) que heredan de BaseModel
Cree el primer motor de almacenamiento abstracto del proyecto: almacenamiento de archivos.
crear todas las pruebas unitarias para validar todas nuestras clases y motor de almacenamientio

La Consola realizará la siguiente tarea:
  - Crea un nuevo objeto
  - Recuperar un objeto de un archivo
  - Realizar operaciones sobre objetos
  - Destruir un objeto


* Storage:
  En este proyecto todas ls clases son manejadas por un motor de almacenamiento("Storage" engine) en
  la Clase FileStorage 

INSTALACIÓN:
git clone https://github.com/jhamilamedina/holbertonschool-AirBnB_clone.git
Cambia al AirBnB directorio y ejecute el comando:
... bash
 ./console.py
...

EJECUCIÓN:
En el modo interactivo
...bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
