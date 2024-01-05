General
#####################
.. contents:: Contenidos
    :depth: 3

Descripción:
*****************

``PDK``
===================
Especifica el kit en el proceso de diseño (PDK). (Predeterminado: ``sky130A``)

``DESIGN_NAME``
===================
El nombre del módulo de nivel superior del diseño.

``VERILOG_FILES``
===================
La ruta de los archivos Verilog del diseño, proporcionada como una matriz de archivos en JSON o una lista de archivos delimitada por espacios en blanco en Tcl. Los archivos se evalúan en orden, es decir, si el archivo B depende del archivo A,
el archivo A debe aparecer primero.

``CLOCK_PERIOD``
===================
El período de reloj utilizado para los relojes en el diseño, unidades en nanosegundos.

``CLOCK_PORT``
===================
El nombre del puerto de reloj del diseño.

``CLOCK_NET``
===================
El nombre de la red de entrada al búfer del reloj raíz. (Predeterminado: ``CLOCK_PORT``)

``STD_CELL_LIBRARY``
======================
Especifica la biblioteca de celdas estándar que se utilizará en el PDK especificado. (Predeterminado: ``sky130_fd_sc_hd``)

``STD_CELL_LIBRARY_OPT``
==========================
Especifica la biblioteca de celdas estándar que se utilizará durante las optimizaciones de cambio de tamaño. (Predeterminado: ``STD_CELL_LIBRARY``)

``PDK_ROOT``
===================
Especifica la ruta de la carpeta del PDK. Busca un config.tcl en el directorio ``$::env(PDK_ROOT)/$::env(PDK)/libs.tech/openlane/ `` y tiene al menos una configuración de biblioteca de celdas estándar definida en ``$::env(PDK_ROOT)/ $::env(PDK)/libs.tech/openlane/$::env(STD_CELL_LIBRARY)``.

``DIODE_PADDING``
===================
Número de sitios al pad izquierdo ``DIODE_CELL`` durante la colocación detallada. (Predeterminado: `2` sitios)

``MERGED_LEF``
===================
Apunta a ``merged.lef``, que es una fusión de varios archivos LEF, incluyendo la tecnología lef, las celdas lef, los archivos lef personalizados y los archivos IO lef.

``NO_SYNTH_CELL_LIST``
=======================
Especifica el archivo que contiene la lista de celdas de no uso que se excluirá del archivo de la biblioteca durante la síntesis. Si no está definida, se busca esta ruta ``$::env(PDK_ROOT)/$::env(PDK)/libs.tech/openlane/$::env(STD_CELL_LIBRARY)/no_synth.cells`` y si no se encuentra, entonces la biblioteca original se utilizará tal como está.

``DRC_EXCLUDE_CELL_LIST``
=========================
Especifica el archivo que contiene la lista de celdas de no uso que se excluirá del archivo de la biblioteca durante la síntesis y las optimizaciones de tiempo. Si no está definida, se busca esta ruta ``$::env(PDK_ROOT)/$::env(PDK)/libs.tech/openlane/$::env(STD_CELL_LIBRARY)/drc_exclude.cells`` y si no se encuentra, entonces la biblioteca original se utilizará tal como está. En otras palabras, ``DRC_EXCLUDE_CELL_LIST`` contiene la única lista de celdas excluidas en las optimizaciones de tiempo.

``BASE_SDC_FILE``
===================
Especifica el archivo SDC base que se utiliza durante el flujo. Es el archivo SDC predeterminado utilizado para ``PNR_SDC_FILE`` y ``SIGNOFF_SDC_FILE``. (Predeterminado: ``$::env(OPENLANE_ROOT)/scripts/base.SDC``)

``PNR_SDC_FILE``
===================
Especifica el archivo SDC utilizado durante todas las etapas de implementación (PnR). Lo utilizan herramientas en el flujo y durante el STA realizado en estas etapas. No se utiliza durante la etapa de signoff. (Predeterminado: ``$::env(BASE_SDC_FILE)``)