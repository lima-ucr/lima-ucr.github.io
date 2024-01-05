Integración de macros
######################
.. contents:: Contenidos
    :depth: 3

Descripción:
*********************

``VERILOG_FILES_BLACKBOX``
=============================
Archivos Verilog en caja negra donde se ignora la implementación. Útil para macros pre-endurecidos que incorpora a el diseño, utilizadas durante la  síntesis y opensta. ``/// sta-blackbox`` se puede agregar a un archivo para
omitir ese archivo mientras se ejecuta sta. Esto tratara como caja negra todos los módulos definidos dentro de ese archivo. Se recomienda proporcionar un net-list a nivel de compuertas siempre que sea posible para completar sta.

``EXTRA_LEFS``
=============================
Especifica archivos LEF de macros pre-endurecidos utilizados en el diseño actual. Utilizados durante placement y routing.

``EXTRA_LIBS``
=============================
Especifica archivos LEF de macros pre-endurecidos utilizados en el diseño actual. Utilizados durante analisis de temporizacion. (opcional)

``EXTRA_GDS_FILES``
=============================
Especifica archivos GDS de macros ppre-endurecidos utilizados en el diseño actual. Utilizados durante la salida tape-out.