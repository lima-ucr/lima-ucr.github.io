Síntesis lógica
###############

.. contents:: Contenidos
    :depth: 3

Configuración por defecto:
*****************************************

Revisando la ruta ``~/OpenLane/configuration/synthesis.tcl`` se encuentra la siguiente información en este archivo:

.. figure:: ../img/def/synth_var.png
  :name: synth_def
  :scale: 80 %
  :align: center

  Configuración por defecto de las variables de síntesis.

Descripción y ejemplos:
*****************************************

``SYNTH_CLOCK_UNCERTAINTY``
============================
Especifica un valor para la incertidumbre del reloj para el análisis de temporización. (Predeterminado: `0.25`) 

Al aumentarlo al doble de su valor por defecto (`0.5`) vemos que primeramente el cambio se aprecia en los reportes
de sta de la siguiente manera:

.. figure:: ../img/synthesis/sta_min_CLOCK_UNCERTAINTY.png
  :name: sta_min_CLOCK_UNCERTAINTY
  :scale: 80 %
  :align: center

  Reporte sta min de la tapa de síntesis.

De donde comparando ambos reportes (mínimo y máximo) vemos que para el caso mínimo este delay se suma; mientras que para
el caso máximo este delay se resta. Produciendo así aumento en el tiempo de hold y disminución el tiempo de setup respectivamente.

Se observa que el tiempo de hold puede aumentar tanto al punto de no cumplir para ciertos caminos. Lo cual se observa en la siguiente imagen:

.. figure:: ../img/synthesis/sta_CLOCK_UNCERTAINTY.png
  :name: sta_CLOCK_UNCERTAINTY
  :scale: 80 %
  :align: center

  Reporte sumatoria sta de la tapa de síntesis.

``SYNTH_CLOCK_TRANSITION``
============================
Especifica un valor para el tiempo de transición/desplazamiento del reloj para el análisis de temporización. (Predeterminado: `0.15`)

Al aumentarlo al doble de su valor por defecto (`0.3`) vemos que primeramente el cambio se aprecia en los reportes
de sta de la siguiente manera:

.. figure:: ../img/synthesis/sta_min_CLOCK_TRANSITION.png
  :name: sta_min_CLOCK_TRANSITION
  :scale: 80 %
  :align: center

  Reporte sta minimo de la tapa de síntesis

Además se obtiene un nuevo mensaje en el registro de advertencias:

.. figure:: ../img/synthesis/warning_CLOCK_TRANSITION.png
  :name: sta_CLOCK_TRANSITION
  :scale: 80 %
  :align: center

  Registro de advertencias.

Del cual revisando el reporte mencionado vemos que se producen tres violaciones de slew, que significa que la transición de la señal es muy lenta. 

``SYNTH_TIMING_DERATE``
=======================
Especifica un factor de reducción para multiplicar los retrasos de ruta. Especifica los rangos superior e inferior de sincronización. (Predeterminado: `+5%/-5%`)

Al aumentar este valor al doble de su valor por defecto (0.1) vemos que se aumenta el tiempo de llegada de los datos en 0.1 con respecto al valor por defecto; 
esto tras comparar para una misma ruta su análisis de sta como se observa en la siguiente imagen:

.. figure:: ../img/synthesis/sta_max_SYNTH_TIMING_DERATE.png
  :name: sta_max_SYNTH_TIMING_DERATE
  :scale: 40 %
  :align: center

  Reportes sta máximo de la tapa de síntesis.

``SYNTH_STRATEGY``
===================
Estrategias para la síntesis lógica abc y el mapeo tecnológico. Valores posibles son ``DELAY/AREA`` con rangos de `0-4` y `0-3` respectivamente; la primera parte se refiere al objetivo de optimización
de la estrategia de síntesis (area vs delay) y la segunda es un índice. (Predeterminado: ``AREA 0``). 

Al variar la estrategia se pueden obtener optimizaciones para ciertos objetivos específicos según la aplicación. Esto se puede observar en la siguiente imagen:

.. figure:: ../img/synthesis/design_exploration.png
  :name: design_exploration
  :scale: 80 %
  :align: center

  Resultados exploración espacio de diseño.

``SYNTH_BUFFERING``
===================
Habilita el buffer de celdas abc. Habilitado = 1, Deshabilitado = 0. (Predeterminado: `1`)
Lo cual tras deshabilitarlo se observa lo siguiente al comparar con el reporte por defecto:

.. figure:: ../img/synthesis/area_SYNTH_BUFFERING.png
  :name: area_SYNTH_BUFFERING
  :scale: 80 %
  :align: center

  Reportes de área de la etapa de sintesis.

De donde se observa que la principal diferencia entre las cantidad de celdas es provocada por disminución en la cantidad de buffers utilizados.

``SYNTH_SIZING``
================
Habilita el tamaño de celda abc (en lugar de almacenar en buffer).  Habilitado = 1, Deshabilitado = 0. (Predeterminado: `0`)
Se tienen los mismo resultados de habilitar el parámetro ``SYNTH_BUFFERING``.

``SYNTH_READ_BLACKBOX_LIB``
=============================
Bandera que permite leer el archivo biblioteca completo (sin recortar) como una caja negra para síntesis. No se utiliza en el mapeo tecnológico. 
Usarse para preservar instancias de compuerta en el rtl del diseño. Habilitado = 1, Deshabilitado = 0. (Predeterminado: `0`)

Lo cual tras habilitarlo se observa que el área disminuye porque se leen menos celdas ya que se utiliza el concepto de caja negra. Lo anterior se observa en los siguientes reportes:

.. figure:: ../img/synthesis/area_SYNTH_READ_BLACKBOX_LIB.png
  :name: area_SYNTH_READ_BLACKBOX_LIB
  :align: center

  Reportes de área de la etapa de síntesis.

``SYNTH_NO_FLAT``
=================
Bandera que deshabilita el aplanamiento de la jerarquía durante la síntesis, y solo la aplana después de la síntesis, el mapeo y las optimizaciones. Habilitado = 1, Deshabilitado = 0. (Predeterminado: `0`)

``SYNTH_SHARE_RESOURCES``
=========================
Bandera que permite a yosys reducir el número de celdas determinando recursos que se pueden compartir y fusionándolos. Habilitado = 1, Deshabilitado = 0. (Predeterminado: `1`).

``SYNTH_ADDER_TYPE``
====================
Tipo de sumador al que se asignan los operadores $add y $sub. Posibles valores `YOSYS/FA/RCA/CSA`; donde `YOSYS` usa el sumador interno de Yosys, 
`FA` usa full-adder structure, `RCA` usa ripple carry adder structure y `CSA` usa carry select adder. (Predeterminado: `YOSYS`)

Para sus distintos valores posibles se tiene el siguiente cuadro resumen de los parámetros mas importantes:

.. list-table:: Resumen parámetros de interés para las distintos tipos de sumadores
  :header-rows: 1
  :align: center

  * - Tipos de sumadores
    - YOSYS
    - FA
    - RCA
    - CSA
  * - Chip Area
    - 100462.6016
    - 105050.752
    - 100890.512 
    - 107314.1728
  * - Potencia
    - 1.99e-02
    - 2.20e-02
    - 2.00e-02
    - 2.05e-02
  * - Peor Setup
    - 3.15
    - 0.15
    - -16.59
    - 0.46
  * - Peor Hold
    - 0.16
    - 0.17 
    - 0.19
    - 0.2
  * - Violaciones Slew
    - 0
    - 0
    - 0
    - 28
  * - Violaciones Fanout
    - 4
    - 7
    - 13
    - 31
  * - Violaciones Cap 
    - 0
    - 0
    - 0
    - 0


Por otro lado la potencia y el skew se mantiene bastante similar.

``SYNTH_ELABORATE_ONLY``
========================
No se realiza ningún mapeo lógico. Útil cuando se trata de netlists estructurales de Verilog. (Predeterminado: `0`) 

``SYNTH_FLAT_TOP``
===================
Se especifica si el nivel superior debe aplanarse o no durante la elaboración. 1 = Verdadero, 0 = Falso. (Predeterminado: `0`)

``IO_PCT``
==========
Especifica el porcentaje del período de reloj utilizado en los retrasos de entrada/salida. Varía de 0 a 1,0. (Predeterminado: `0.2`)

Al aumentarlo al doble de su valor por defecto (`0.4`) vemos que este cambio primeramente se puede apreciar en los reportes de sta de la
siguiente manera:

.. figure:: ../img/synthesis/sta_max_IO_PCT.png
  :name: sta_max_IO_PCT
  :align: center

  Reporte sta máximo de la tapa de síntesis.

Esto principalmente afecta el tiempo de llegada del dato que para caminos críticos si se aumenta mucho puede provocar violaciones de setup, como es el caso por ejemplo de utilizar un valor de 0.6.

``SYNTH_BUFFER_DIRECT_WIRES``
===============================
Inserta celdas intermedias en el diseño para cables conectados directamente. (Predeterminado: `1`)

Al deshabilitarlo se modifica el reporte de área, ya que la cantidad de celdas disminuye en 8, de 9442 a 9434, reduciendo ligeramente el área como se observa
en la siguiente imagen:

.. figure:: ../img/synthesis/area_SYNTH_BUFFER_DIRECT_WIRES.png
  :name: area_SYNTH_BUFFER_DIRECT_WIRES
  :align: center

  Reportes área de la tapa de síntesis.

``SYNTH_SPLITNETS``
===================
Divide redes de varios bits en redes de un solo bit. (Predeterminado: `1`)

Al deshabilitarlo se aumenta considerablemente el área, debido a que se utilizan mas wires y bits por wire, esto se observa en el siguiente reporte:

.. figure:: ../img/synthesis/area_SYNTH_SPLITNETS.png
  :name: area_SYNTH_SPLITNETS
  :align: center

  Reportes área de la tapa de síntesis.


Resumen de resultados:
************************
Se va a compara, en porcentajes, cuanto vario con respecto al modelo de referencia los parámetros mas importantes para esta etapa al modificar cada variable.
Los valores de las variables son los mismo utilizados anteriormente, de modo que se tienen los siguientes resultados:

.. list-table:: Comparación de parámetros con el modelo de referencia, etapa de síntesis
  :header-rows: 1
  :align: center

  * - Variables
    - Chip Area
    - Potencia 
    - Peor Setup 
    - Peor Hold
    - Violaciones Slew 
    - Violaciones Fanout
    - Violaciones Cap
  * - ``SYNTH_CLOCK_UNCERTAINTY``
    - 0
    - 0
    - -7.94
    - -156.25
    - 0
    - 12
    - 0
  * - ``SYNTH_CLOCK_TRANSITION``
    - 0
    - 0
    - -0.317
    - 6.25
    - 4
    - 11
    - 0
  * - ``SYNTH_TIME_DERATE``
    - 0
    - 0
    - -9.84
    - -12.50
    - 0
    - -1
    - 0
  * - ``SYNTH_STRATEGY``
    - 3.963
    - 44.72
    - 47.30
    - 18.75
    - 2
    - 49
    - 0
  * - ``SYNTH_BUFFERING``
    - -7.65
    - -3.01
    - -76.50
    - 0
    - 0
    - -13
    - 0
  * - ``SYNTH_SIZING``
    - -7.65
    - -3.01
    - -76.50
    - 0
    - 0
    - -13
    - 0
  * - ``SYNTH_READ_BLACKBOX_LIB``
    - -0.340
    - -3.01
    - 10.47
    - 12.5
    - 0
    - -6
    - 0
  * - ``SYNTH_ADDER_TYPE``
    - 6.82
    - 3.015
    - -85.39
    - 25
    - 0
    - -21
    - 0
  * - ``IO_PCT``
    - 0
    - 0
    - -66.35
    - 0
    - 2
    - 1
    - 0
  * - ``SYNTH_BUFFER_DIRECT_WIRES``
    - -0.039
    - 0
    - 0
    - 0
    - 0
    - 8
    - 0
  * - ``SYNTH_SPLITNETS``
    - 17.76
    - 8.04
    - -5.71
    - 112.5
    - 0
    - -29
    - 0