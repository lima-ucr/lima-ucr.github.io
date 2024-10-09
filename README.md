Este es la documentación de la página web del LIMA.
En este se detallla cómo se pueden crear páginas nuevas para añadir, como compilar los documentos, entre otras cosas.

Primeramente, el root contiene varios archivos y carpetas. En este se encuentra mayoritariamente los html de las páginas. La carpeta docs contiene los archivos .rst, estos archivos son la base de la página, en estos se describe el contenido que va a tener la página, cómo se van a ver estos cóntenidos, entre otras cosas...



------------------------------------------------------------
-- ¿Cómo creo un archivo nuevo y lo incluyo en la página? --
------------------------------------------------------------

Para crear una nueva sub página de la página web, se debe crear un archivo .rst dentro de la carpeta docs. Para el ejemplo, se va a crear un archivo ficticio llamado "Ejemplo.rst".

Una vez creado este archivo, lo primordial es darle un título, esto es necesario para poder incluir el archivo en el arbol de archivos de la página. Para este ejemplo, nuestro archivo va a ser una subpágina de la página de Documentaciòn y tutoriales.

Para que el archivo tenga un título, se puede hacer de la siguiente manera:

// Dentro del archivo Ejemplo.rst

Este es el título de la página Ejemplo
======================================

//

Se debe escribir el título, y debajo de este poner la lìnea de ===========,  
esta última linea es la que le da la cualidad de tìtulo. Este título es el que la herramienta sphinx utiliza en el arbol de archivos de la página para presentarlo como el nombre de la página en cuestión, sin esto, la página le da un nombre genérico.

Una vez creado el archivo y haberle dado un título, se puede proceder a inlcuir la información deseada.

Para añadir el archivo a la página, se debe introducir en alguno de los toctrees, los cuales están dentro de algunos de los archivos .rst, los cuales va a poder encontrar en la carpeta de docs. Los toctree tienen la siguiente forma:

.. toctree::
   :maxdepth: 1
   :caption: Contenido:
   :glob:

Aquí es donde se puede indicar a sphinx que añada al archivo en algun lugar en específico, pero antes de esto, se va a dar un ejemplo visual de cómo está la estructura de la página en este momento:

index
    Proyectos
    About Us
    Tutoriales
        OpenLane

Y queremos que Ejemplo.rst se encuentre en:

index
    Proyectos
    About Us
    Tutoriales y Documentación
        OpenLane
        Ejemplo.rst

Para lograr esto, se va a tomar el nombre del archivo que queremos incluir en el toctree; en este caso, es el toctree de tutoriales, por lo que nos dirigimos al archivo tutoriales.rst, y buscamos el toctree. Una vez encontrado, se va a modificar de la siguiente manera:

.. toctree::
   :maxdepth: 1
   :caption: Contenido:
   :glob:

   OpenLane
   Ejemplo

Note que, para añadir el archivo, no se utiliza el título, sino que se usa el nombre del archivo, en este caso "Ejemplo.rst" y se añade sin el .rst

Una vez hecho este cambio, la página tendrá la siguiente forma

index
    Proyectos
    About Us
    Tutoriales y Documentación
        OpenLane
        Este es el título de la página Ejemplo

Por lo que, en resumen, el nombre del archivo lo usamos para añadirlo en el toctree, y el título es el cómo va a aparecer en la página.







------------------------------
-- ¿Cómo compilo la página? --
------------------------------

Primeramente, para compilar es necesario tener instalado sphinx, python, y el tema. El tema es indispensable para que la herramienta sphinx pueda compilar. El tema que se está utilizando para esta página se llama "Read the Docs", y la forma para instalarlo es:
sudo apt install python3-sphinx-rtd-theme


Una vez ya se tiene intalado Sphinx, Python y el tema RTD, se puede compilar la página. Para compilar la página y que esta tenga como resultado los html, se puede utilizar la siguiente linea de código:

sphinx-build  -b html XXXX YYYY

Donde XXXX es el nombre del directorio donde se encuentran los archivos .rst, y YYYY es el directorio donde se van a guardar los archivos html compilados, así como las imágenes necesarias. Típicamente se va a utilizar la siguiente línea de código:

sphinx-build  -b html docs newPage

Esto debido a que los archivos .rst siempre debería guardarse en el directorio docs, y los archivos creados generalmente, por orden, se guardan en newPage, pero esta última no necesariamente siempre tiene que ser ese directorio.





----------------------------------------
Hasta aquí llega este tutorial, le deseo mucha suerte en su camino, saludos :)