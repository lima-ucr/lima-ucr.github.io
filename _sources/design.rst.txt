Diseño físico
############################
.. contents:: Contenidos
    :depth: 4


Floorplan (FP)
***************************************************

Configuración por defecto:
===========================
Revisando la ruta ``~/OpenLane/configuration/floorplan.tcl`` se encuentra la siguiente información en este archivo:

.. figure:: ../img/def/fp_var.png
  :name: fp_def
  :scale: 80 %
  :align: center

  Configuración por defecto de las variables de floorplan.

Descripción y ejemplos:
===========================

``RUN_TAP_DECAP_INSERTION``
-----------------------------------------------------------------------------
Permite la inserción de celdas tap y decap después de floorplan. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

Tras deshabilitarlo se observa lo siguiente en el layout y la descripción de su área:

.. figure:: ../img/floorplan/FP_RUN_TAP_DECAP_INSERTION.png
  :name: fp_RUN_TAP_DECAP_INSERTION
  :align: center

  Layout del diseño.

De donde principalmente se puede ver que se elimina la cuadricula que produce las celdas tap y decap para la conexion con los sustratos.
Además en el hierarchy solo se tiene el modulo principal (top), no se tienen ya las instancias físicas de las celdas fill y tap. 

``FP_CORE_UTIL``
-----------------------------------------------------------------------------
El porcentaje de utilización del núcleo. (Predeterminado: `50%`)

Tras bajarlo a un 30 por ciento se tiene el siguiente resultado:

.. figure:: ../img/floorplan/FP_CORE_UTIL_30.png
  :name: FP_CORE_UTIL_30
  :align: center

  Layout del diseno.

De donde se observa que para que la utilización se reduzca se tiene que aumentar el área disponible, que corresponde a el área física.
La cual aumenta, de 4762 a 5890 :math:`μm^{2}`, ya que se mantiene fija el área de las celdas.

``FP_ASPECT_RATIO``
-----------------------------------------------------------------------------
La relación de aspecto del núcleo, se define como: alto/ancho. (Predeterminado: `1`)

Al modificar esta relación a 0.5 se observa como el ancho pasa a ser el doble del alto en la siguiente imagen:

.. figure:: ../img/floorplan/FP_ASPECT_RATIO_0.5.png
  :name: FP_ASPECT_RATIO_0.5
  :align: center

  Layout del diseño.

Además se modifica el placenta de los pines.

``FP_SIZING``
-----------------------------------------------------------------------------
Determina si se va a utilizar un tamaño relativo, tomando lo definido por la variable ``FP_CORE_UTIL``, o un tamaño absoluto, tomando lo definido por la variable ``DIE_ARE``, en el floorplan. (Predeterminado: `realtive/absolute`)

``DIE_AREA``
-----------------------------------------------------------------------------
Cuando ``FP_SIZING`` se establece en absoluto especifica el área muerta para utilizar en el floorplan. Se define como un rectángulo de 4 esquinas de la forma:  “x0 y0 x1 y1”. Unidades en μm. (Predeterminado: sin definir)

Al aumentar este área muerta, que para se toma el área muerta predeterminada que tiene el diseño (0.0 0.0 459.285 470.005) se le agregan 200 μm a las coordenadas x1 y y1; además se mantiene fijo el área del núcleo.  Lo cual da como resultado el siguiente layout:

.. figure:: ../img/floorplan/DIE_AREA.png
  :name: DIE_AREA
  :align: center

  Layout del diseño.

  
``CORE_AREA``
-----------------------------------------------------------------------------
Cuando ``FP_SIZING`` se establece en absoluto especifica el área del núcleo, es decir el área muerta (``DIE_AREA``) menos los margenes. Se define como un rectángulo de 4 esquinas de la forma: “x0 y0 x1 y1”. Unidades en μm. (Predeterminado: sin definir)

De forma similar al die area, al aumentar el área del núcleo a 200 μm en las coordenadas x1 y y1 esta vez se tiene que aumentar el ``DIE_AREA`` para que el flujo de diseño sea completado; lo cual esto produce que el layout se vea de la siguiente manera:

.. figure:: ../img/floorplan/CORE_AREA.png
  :name: CORE_AREA
  :align: center

  Layout del diseño.

``FP_IO_MODE``
-----------------------------------------------------------------------------
Decide el modo de la opción de colocación aleatoria de IOs. 0 = modo coincidente, 1 = modo equidistante aleatorio. El modo de coincidencia intenta optimizar la 
ubicación de pines y celdas. El modo equidistante aleatorio coloca pines equidistantes en un orden aleatorio. (Predeterminado: `0`)

Al utilizar el modo equidistante se obtiene lo siguiente:

.. figure:: ../img/floorplan/FP_IO_MODE.png
  :name: FP_IO_MODE
  :align: center

  Layout del diseño.

``FP_WELLTAP_CELL``
-----------------------------------------------------------------------------
El nombre de las celdas welltap utilizado durante para la inserción de welltap.

``FP_ENCAP_CELL``
-----------------------------------------------------------------------------
El nombre de las celdas endcap utilizando durante le inserción de encap.

``FP_PDN_CFG``
-----------------------------------------------------------------------------
Apunta a un archivo de configuración de PDN que describe cómo construir el PDN en detalle. (Predeterminado: ``scripts/openroad/common/pdn_cfg.tcl``)

``FP_PDN_AUTO_ADJUST``
-----------------------------------------------------------------------------
Decide si el flujo debe intentar reajustar la red eléctrica para que encaje dentro del área núcleo del diseño, si es necesario. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

Al deshabilitar esta opción se observa lo siguiente:

.. figure:: ../img/floorplan/FP_PDN_AUTO_ADJUST.png
  :name: FP_PDN_AUTO_ADJUST
  :align: center

  Layout del diseño, énfasis red eléctrica.

De la imagen anterior se tiene que la red eléctrica se mantiene igual, por lo que este parámetro no era necesario para este diseño. 

``FP_PDN_SKIPTRIM``
-----------------------------------------------------------------------------
Habilita la opción ``-skip_trim`` durante pdngen. El cual omite el paso de recorte de metal, encargado de intentar eliminar trozos de metal. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `0`)

``FP_TAPCELL_DIST``
-----------------------------------------------------------------------------
Distancia horizontal entre dos columnas de tapcell. (Predeterminado: `14`)

Al reducir este valor a la mitad, revisando las instancias de las celdas welltap observamos que aumenta la cantidad de instancias.Como se observa en la siguiente imagen:

.. figure:: ../img/floorplan/FP_TAPCELL_DIST_7.png
  :name: FP_TAPCELL_DIST_7
  :align: center

  Layout del diseño, énfasis instancias celdas welltap

Mientras que con su distancia predeterminada estas instancias se observan de la siguiente manera:

.. figure:: ../img/floorplan/FP_TAPCELL_DIST_14.png
  :name: FP_TAPCELL_DIST_14
  :align: center

  Layout del diseno, énfasis instancias celdas welltap

``FP_IO_VEXTEND``
-----------------------------------------------------------------------------
Extiende los pines IOs verticales fuera del área muerta, en las unidades especificadas por esta (μm). (Predeterminado: `0` Desactivado)

Al extenderlos una distancia de 10μm se observa lo siguiente:

.. figure:: ../img/floorplan/FP_IO_VEXTEND.png
  :name: FP_IO_VEXTEND
  :align: center

  Pines IOs verticales.

``FP_IO_HEXTEND``
-----------------------------------------------------------------------------
Extiende los pines IOs horizontales fuera del área muerta, en las unidades especificadas por esta (μm). (Predeterminado: `0` Desactivado)

Al extenderlos una distancia de 10μm se observa lo siguiente:

.. figure:: ../img/floorplan/FP_IO_HEXTEND.png
  :name: FP_IO_HEXTEND
  :align: center

  Pines IOs horizontales.
  

``FP_IO_VLENGTH``
-----------------------------------------------------------------------------
La longitud de los pines IOs verticales en micrómetros. (Predeterminado: `4`)

Los pines verticales se encuentran en la capa de metal2, por lo que revisando esta capa se tiene que para cuando tienen una longitud de 4 (valor predeterminado) son de la siguiente manera:

.. figure:: ../img/floorplan/FP_IO_VLENGTH_4.png
  :name: FP_IO_VLENGTH_4
  :align: center

  Pines IOs verticales predeterminados.

Y al reducir su longitud a la mitad (2) de su valor predeterminado se tiene el siguiente resultado:

.. figure:: ../img/floorplan/FP_IO_VLENGTH_2.png
  :name: FP_IO_VLENGTH_2
  :align: center

  Pines IOs verticales a la mitad de su longitud predeterminada.

``FP_IO_HLENGTH``
-----------------------------------------------------------------------------
La longitud de los pines IOs horizontales en micrómetros. (Predeterminado: `4`)

De forma similar a los pines verticales, los horizontales se encuentran en la capa de metal3 y al reducir su longitud a la mitad se tiene el siguiente resultado:

.. figure:: ../img/floorplan/FP_IO_HLENGTH_4.png
  :name: FP_IO_HLENGTH_4
  :align: center

  Pines IOs horizontales predeterminados.

.. figure:: ../img/floorplan/FP_IO_HLENGTH_2.png
  :name: FP_IO_HLENGTH_2
  :align: center

  Pines IOs horizontales a la mitad de su longitud predeterminada.

``FP_IO_VTHICKNESS_MULT``
-----------------------------------------------------------------------------
Un multiplicador para el grosor de los pines IOs verticales. El grosoro base es el ancho mínimo de la capa de pines (Predeterminado: `2`)

Al aumentar el ancho al doble de su valor predeterminado se observa lo siguiente:

.. figure:: ../img/floorplan/FP_IO_VTHICKNESS_MULT_4.png
  :name: FP_IO_VTHICKNESS_MULT_4
  :align: center

  Pines IOs verticales a doble de su ancho predeterminado.

``FP_IO_HTHICKNESS_MULT``
-----------------------------------------------------------------------------
Un multiplicador para el grosor de los pines IOs horizontales. El grosoro base es el ancho mínimo de la capa de pines (Predeterminado: `2`)

De forma similar al parámetro anterior, al aumentarlo al doble se tiene:

.. figure:: ../img/floorplan/FP_IO_HTHICKNESS_MULT_4.png
  :name: FP_IO_HTHICKNESS_MULT_4
  :align: center

  Pines IOs horizontales a doble de su ancho predeterminado.

``BOTTOM_MARGIN_MULT``
-----------------------------------------------------------------------------
El margen del núcleo, en múltiplos de las alturas del sitio, desde el límite inferior. Si ``FP_SIZING`` es absoluto y se establece ``CORE_AREA``, esta variable no tiene ningún efecto. (Predeterminado: `4`)

Al reducirlo a la mitad se observa en la siguiente imagen como el margen inferior disminuye: 

.. figure:: ../img/floorplan/BOTTOM_MARGIN_MULT_2.png
  :name: BOTTOM_MARGIN_MULT_2
  :align: center

  Layout del diseño.

``TOP_MARGIN_MULT``
-----------------------------------------------------------------------------
El margen del núcleo, en múltiplos de las alturas del sitio, desde el límite superior. Si ``FP_SIZING`` es absoluto y se establece ``CORE_AREA``, esta variable no tiene ningún efecto. (Predeterminado: `4`)

Al reducirlo a la mitad se observa en la siguiente imagen como el margen superior disminuye: 

.. figure:: ../img/floorplan/TOP_MARGIN_MULT_2.png
  :name: TOP_MARGIN_MULT_2
  :align: center

  Layout del diseño.

``LEFT_MARGIN_MULT``
-----------------------------------------------------------------------------
El margen del núcleo, en múltiplos de los anchos del sitio, desde el límite izquierdo. Si ``FP_SIZING`` es absoluto y se establece ``CORE_AREA``, esta variable no tiene ningún efecto. (Predeterminado: `12`)

Al reducirlo a 8 se observa en la siguiente imagen que el margen izquierdo disminuye, además esto produce también que el placement de los IOs cambie, esto se observa en la siguiente imagen:

.. figure:: ../img/floorplan/LEFT_MARGIN_MULT_8.png
  :name: LEFT_MARGIN_MULT_8
  :align: center

  Layout del diseño.

``RIGHT_MARGIN_MULT``
-----------------------------------------------------------------------------
El margen del núcleo, en múltiplos de los anchos del sitio, desde el límite derecho. Si ``FP_SIZING`` es absoluto y se establece ``CORE_AREA``, esta variable no tiene ningún efecto. (Predeterminado: `4`)

De forma similar al parámetro anterior al reducirlo a 8 ahora se observa que es el margen derecho el que se reduce. 

.. figure:: ../img/floorplan/RIGHT_MARGIN_MULT_8.png
  :name: RIGHT_MARGIN_MULT_8
  :align: center

  Layout del diseño.

``FP_PDN_CORE_RING``
-----------------------------------------------------------------------------
Permite agregar un anillo central alrededor del diseño. Más detalles sobre las variables de control en la documentación de configuraciones de pdk. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `0`)

Al habilitar esta opción este anillo se observa de la siguiente manera:

.. figure:: ../img/floorplan/FP_PDN_CORE_RING.png
  :name: FP_PDN_CORE_RING
  :align: center

  Layout del diseño, énfasis anillo red eléctrica.

``FP_PDN_ENABLE__GLOBAL_CONNECTIONS``
-----------------------------------------------------------------------------
Permite la conexión a la alimentación de las celdas estándar. Es raro que sea necesario deshabilitar esta variable (Predeterminado: `1`)

``FP_PDN_ENABLE_RAILS``
-----------------------------------------------------------------------------
Habilita la creación de carriles en la red eléctrica. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

Al deshabilitarlo se la red eléctrica del diseño se observa de la siguiente manera:

.. figure:: ../img/floorplan/FP_PDN_ENABLE_RAILS.png
  :name: FP_PDN_ENABLE_RAILS
  :align: center

  Layout del diseño, énfasis red eléctrica.

``FP_PDN_ENABLE_MACROS_GRID``
-----------------------------------------------------------------------------
Permite la conexión de macros a la red eléctrica de primer nivel. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

``FP_PDN_MACRO_HOOKS``
-----------------------------------------------------------------------------
Especifica conexiones explícitas de macros internas a la nivel superior de la red eléctrica como: una lista de nombres de instancias de macros, vdd de dominio de energía, nombres de redes de tierra, nombres de vdd de macros y pines de tierra; lo cual es: ``<instance_name> <vdd_net> <gnd_net> <vdd_pin> <gnd_pin>``. Mientras que en una archivo .JSON declárelo como una matriz de cadenas y en Tcl, use comas como delimitador.

``FP_PDN_CHECK_NODES``
-----------------------------------------------------------------------------
Permite comprobar si hay nodos no conectados en la red eléctrica. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

``FP_TAP_HORIZONTAL_HALO``
-----------------------------------------------------------------------------
Especifica el tamaño del anillo horizontal alrededor de las macros durante la inserción de celdas tap. El valor proporcionado está en micrómetros. (Predeterminado: `10`)

``FP_TAP_VERTICAL_HALO``
-----------------------------------------------------------------------------
Especifica el tamaño del anillo vertical alrededor de las macros durante la inserción de celdas tap. El valor proporcionado está en micrómetros. (Predeterminado: `10`)

``FP_PDN_HORIZONTAL_HALO``
-----------------------------------------------------------------------------
Establece el anillo horizontal alrededor de las macros durante la inserción de la red eléctrica. El valor proporcionado está en micrómetros. (Predeterminado: `10`)

``FP_PDN_VERTICAL_HALO``
-----------------------------------------------------------------------------
Establece el anillo vertical alrededor de las macros durante la inserción de la red eléctrica. El valor proporcionado está en micrómetros. (Predeterminado: `10`)

``DESIGN_IS_CORE``
-----------------------------------------------------------------------------
Controla las capas utilizadas en la red eléctrica. Dependiendo de si el diseño es el núcleo del chip o una macro dentro del núcleo. 1 = core, 0 = macro. (Predeterminado: `1`)

Al establecerlo como macro, la red eléctrica es lo único que cambia y queda de la siguiente manera:

.. figure:: ../img/floorplan/DESIGN_IS_CORE.png
  :name: DESIGN_IS_CORE
  :align: center

  Layout del diseño, énfasis red eléctrica.

``FP_PIN_ORDER_CFG``
-----------------------------------------------------------------------------
Apunta al archivo de configuración del orden de los pines para configurar los pines en direcciones específicas (S, W, E, N). 
Si no se configura, los pines IO se colocarán según uno de los otros métodos dependiendo del resto de las configuraciones.

También se puede utilizar ``$<number>`` para colocar un pin virtual donde ``<number>`` indica, este es el contador de pines virtuales. Y ``@min_distance=<number>`` se utiliza para establecer la distancia mínima entre pines en una dirección específica.

Un ejemplo de como se vería este archivo de configuración es el siguiente:

.. figure:: ../img/floorplan/FP_PIN_ORDER_CFG.png
  :name: FP_PIN_ORDER_CFG
  :align: center

  Ejemplo archivo configuración orden de pines.

``FP_IO_MIN_DISTANCE``
-----------------------------------------------------------------------------
La distancia mínima entre los pines IOs en micrones. (Predeterminado: `3`) 

A su distancia predeterminada los IOs del diseño son de la siguiente manera:

.. figure:: ../img/floorplan/FP_IO_MIN_DISTANCE_3.png
  :name: FP_IO_MIN_DISTANCE_3
  :align: center

  Pines IOs.

Al reducir esta distancia a la mitad, se observa lo siguiente en los IOs del diseño:

.. figure:: ../img/floorplan/FP_IO_H_MIN_DISTANCE_1.5.png
  :name: FP_IO_H_MIN_DISTANCE_1.5
  :align: center

  Pines IOs horizontales.

.. figure:: ../img/floorplan/FP_IO_V_MIN_DISTANCE_1.5.png
  :name: FP_IO_V_MIN_DISTANCE_1.5
  :align: center

  Pines IOs verticales.


``FP_PADFRAME_CFG``
-----------------------------------------------------------------------------
Un archivo de configuración pasado a padringer, un generador de padframe. (Predeterminado: NINGUNO)

Variables de capa I/O 
***************************************************

Descripción y ejemplos:
===========================

``FP_IO_HLAYER``
-----------------------------------------------------------------------------
Capa de metal en la cual se colocan los pines horizontales. (Predeterminado: `4`)

Al colocar los pines horizontales en la capa de metal 2 se obtiene el siguiente layout:

.. figure:: ../img/fp_io_layer/FP_IO_LAYER.png
  :name: FP_IO_LAYER
  :align: center

  Layout del diseño.

De donde el cambio de color a morado corresponde a la capa de metal 2.

``FP_IO_VLAYER``
-----------------------------------------------------------------------------
Capa de metal en la cual se colocan los pines verticales. (Predeterminado: `3`)

Al colocar los pines horizontales en la capa de metal 5 se tiene el layout anterior en donde el cambio de color a celeste corresponde
a la capa de metal 5.


Todos los pasos para el Resizer (RSZ)
***************************************************

Descripción:
===========================

``RSZ_LIB``
-----------------------------------------------------------------------------
Apunta a uno o más archivos lib, correspondientes a la esquina típica, que se utiliza durante las optimizaciones
del resizer. (Predeterminado: establecido en el valor de ``LIB_SYNTH`` de los PDK's)

``RSZ_LIB_FASTEST``
-----------------------------------------------------------------------------
Apunta a uno o más archivos lib, correspondientes a la esquina mas rápida, que se utiliza durante las optimizaciones
del resizer. (Predeterminado: establecido en el valor de ``LIB_FASTEST`` de los PDK's)

``RSZ_LIB_SLOWEST``
-----------------------------------------------------------------------------
Apunta a uno o más archivos lib, correspondientes a la esquina mas lenta, que se utiliza durante las optimizaciones
del resizer. (Predeterminado: establecido en el valor de ``LIB_SLOWEST`` de los PDK's)

``RSZ_MULTICORNER_LIB``
-----------------------------------------------------------------------------
Una bandera para leer las esquinas más rápida y más lenta durante las optimizaciones del resizer.
(Predeterminado: 1)

``RSZ_DONT_TOUCH_RX``
-----------------------------------------------------------------------------
Una única expresión regular que designa las redes como "no tocar" por las optimizaciones de resizer.
(Predeterminado: ``$^`` (no coincide con nada))

``RSZ_DONT_TOUCH``
-----------------------------------------------------------------------------
Una lista de redes o instancias para configurar como "no tocar". (Predeterminado: Vacío)


Placement Global y Detallado (GPL/DPL)
***************************************************

Configuración por defecto:
===========================
Revisando la ruta ``~/OpenLane/configuration/placement.tcl`` se encuentra la siguiente información en este archivo:

.. figure:: ../img/def/pl_var.png
  :name: pl_def
  :scale: 80 %
  :align: center

  Configuración por defecto de las variables de síntesis.

Descripción y ejemplos:
===========================

``PL_TARGET_DENSITY``
-----------------------------------------------------------------------------
Define la densidad de placement deseada de las celdas. Refleja qué tan dispersas estarían las celdas en el área del núcleo. 1 = muy denso. 0 = ampliamente difundido. 
(Predeterminado: ``($::env(FP_CORE_UTIL) + 10 + (5 * $::env(GPL_CELL_PADDING)) ) / 100.0)``)

Utilizando su valor máximo para tener la mayor densidad se observa como las instancias están mas juntas y ocupan menor área, lo cual se observa en la siguiente imagen:

.. figure:: ../img/placement/PL_TARGET_DENSITY_1.png
  :name: PL_TARGET_DENSITY_1
  :align: center

  Layout del diseño.

También al tener mayor densidad produce que se disminuya el área y el consumo de potencia.

``PL_TIME_DRIVEN``
-----------------------------------------------------------------------------
Especifica si el placer debe realizar la ubicación basada en el tiempo. 0 = falso, 1 = verdadero. (Predeterminado: `1`)

Tras desactivar esta función se observa en la siguiente imagen como se modifica el placement y se observa menos densidad, ya que aumenta el área y se mantiene igual la cantidad de instancias.

.. figure:: ../img/placement/PL_TIME_DRIVEN.png
  :name: PL_TIME_DRIVEN
  :align: center

  Layout del diseño.

Pero vemos de los reportes de sta como en general no genera muchos cambios en el timing.

``PL_BASIC_PLACEMENT``
-----------------------------------------------------------------------------
Especifica si el placer debe ejecutar colocación básica. El placement básico se utiliza para diseños extremadamente simples y de baja densidad de solo unas pocas docenas de puertas; debe desactivarse para la mayoría de los diseños. 0 = falso, 1 = verdadero. (Predeterminado: `0`)

``PL_SKIP_INITIAL_PLACEMENT``
-----------------------------------------------------------------------------
Especifica si el placer debe ejecutar el placement inicial o no. 0 = falso, 1 = verdadero. (Predeterminado: `0`)

Al desactivar el placement inicial se observa como en la siguiente imagen el placement en la esquina superior izquierda se
ve bastante modificado, ademas de igual manera se disminuye la densidad.

.. figure:: ../img/placement/PL_SKIP_INITIAL_PLACEMENT.png
  :name: PL_SKIP_INITIAL_PLACEMENT
  :align: center

  Layout del diseño.

El principal efecto que tiene desactivar este parametro es en los reportes de sta se aumentan las violaciones de slew, ya que el placement inicial ayuda a optimizar el tiempo de llegada de la señal de reloj.

``PL_RANDOM_GLB_PLACEMENT``
-----------------------------------------------------------------------------
Especifica si el placer debe ejecutar una colocación aleatoria o no. Esto resulta útil si el diseño es pequeño (menos de 100 celdas). 0 = falso, 1 = verdadero. (Predeterminado: `0`)

``PL_RANDOM_INITIAL_PLACEMENT``
-----------------------------------------------------------------------------
Especifica si el placer debe ejecutar una placement aleatoria en el placement inicial. Esto resulta útil si el diseño es pequeño (menos de 100 celdas). 0 = falso, 1 = verdadero. (Predeterminado: `0`)

``PL_ROUTABILITY_DRIVEN``
-----------------------------------------------------------------------------
Especifica si el placer debe utilizar la ubicación basada en la enrutabilidad. 0 = falso, 1 = verdadero. (Predeterminado: `1`)

``PL_RESIZER_TIE_SEPERATION``
-----------------------------------------------------------------------------
Distancia en micrómetros entre la carga y una celda de unión insertada. El resizer utiliza este valor. (Predeterminado: `0`)

``PL_RESIZER_DESIGN_OPTIMIZATIONS``
-----------------------------------------------------------------------------
Especifica si el resizer debe realizar o no optimizaciones  en el diseño. 0 = falso, 1 = verdadero. (Predeterminado: `1`)

Lo cual al desactivarlo produce los siguientes cambios en el layout:

.. figure:: ../img/placement/PL_RESIZER_DESIGN_OPTIMIZATIONS.png
  :name: PL_RESIZER_DESIGN_OPTIMIZATIONS
  :align: center

  Layout del diseño.

De donde se observa que principalmente de su reporte de área como esta aumenta, a pesar de que disminuye considerablemente la cantidad de instancias, esto se debe a que comparando con el reporte de la configuración por defecto, vemos que esta variable introduce buffers/inversores por las optimizaciones que realiza en el diseño.

``PL_RESIZER_TIMING_OPTIMIZATIONS``
-----------------------------------------------------------------------------
Especifica si el resizer debe realizar o no optimizaciones de tiempo. 0 = falso, 1 = verdadero. (Predeterminado: `1`)

``PL_RESIZER_MAX_WIRE_LENGTH``
-----------------------------------------------------------------------------
Especifica el límite de longitud máxima del cable utilizado por el resizer para insertar buffers. Si se establece en 0, no se insertarán buffers. Valor en micrómetros. (Predeterminado: `0`)

Utilizando un valor mucho menor al por defecto, de 50, se tiene el siguiente registro del resizer:

.. figure:: ../img/placement/resizer-log_PL_RESIZER_MAX_WIRE_LENGTH_50.png
  :name: resizer-log_PL_RESIZER_MAX_WIRE_LENGTH_50
  :align: center

  Registro del resizer, etapa placement.

De donde vemos que como se esta poniendo menos que su valor por defecto va a producir que aumente el retraso en ellos; lo cual se ve reflejado en el análisis sta donde el setup se reduce drásticamente ya que el tiempo de llegada aumenta. 

Además se encuentran 1426 cables que exceden el limite establecido, lo cual produce que se inserten muchos mas buffers.
Esto se puede observan en el reporte de área y en el layout de la siguiente imagen:

.. figure:: ../img/placement/PL_RESIZER_MAX_WIRE_LENGTH_50.png
  :name: PL_RESIZER_MAX_WIRE_LENGTH_50
  :align: center

  Layout del diseño.

``PL_RESIZER_MAX_SLEW_MARGIN``
-----------------------------------------------------------------------------
Especifica un margen para los slews en porcentaje para el resizer. (Predeterminado: `20`)


``PL_RESIZER_MAX_CAP_MARGIN``
-----------------------------------------------------------------------------
Especifica un margen máximo para las capacitancias en porcentajes para el resizer. (Predeterminado: `20`)

``PL_RESIZER_HOLD_SLACK_MARGIN``
-----------------------------------------------------------------------------
Especifica un margen de tiempo para el slack al corregir violaciones de hold. Normalmente, el resizer se detendrá cuando el slack llegue a cero. Esta opción le permite sobrefijar. (Predeterminado: `0.1ns`)

``PL_RESIZER_SETUP_SLACK_MARGIN``
-----------------------------------------------------------------------------
Especifica un margen de tiempo para el salck al corregir violaciones de setup. (Predeterminado: `0.05ns`)


``PL_RESIZER_HOLD_MAX_BUFFER_PERCENT``
-----------------------------------------------------------------------------
Especifica un cantidad máxima de buffers para insertar al para corregir violaciones de hold. Este número se calcula como un porcentaje del número de instancias en el diseño. (Predeterminado: `50`)

``PL_RESIZER_SETUP_MAX_BUFFER_PERCENT``
-----------------------------------------------------------------------------
Especifica un cantidad máxima de buffers para insertar al para corregir violaciones de setup. Este número se calcula como un porcentaje del número de instancias en el diseño. (Predeterminado: 50)

``PL_RESIZER_ALLOW_SETUP_VIOS``
-----------------------------------------------------------------------------
Permite violaciones de setup al corregir violaciones de hold. (Predeterminado: `0`)

``PL_WIRELENGTH_COEF``
-----------------------------------------------------------------------------
Coeficiente de longitud de cable inicial en placement global. Disminuir la variable modificará el placement inicial de las celdas estándar para reducir las longitudes de los cables. (Predeterminado: `0.25`)

Probando con aumentar este valor al doble (0.5) se observa lo siguiente en el layout:

.. figure:: ../img/placement/PL_WIRELENGTH_COEF_0.5.png
  :name: PL_WIRELENGTH_COEF_50
  :align: center

  Layout del diseño.

De donde se observa que se tiene la misma cantidad de instancias, pero como se esta utilizando mayor longitud de cable esto produce que se aumente el área y el placement cambie completamente comparado con el modelo de referencia. También de sus reportes de sta vemos que aumentar el largo de los cables afecta directamente el slew aumentando las violaciones y
en menor manera las capacitancias parásitas para la etapa de placement global, ya en el detallado este propio resizer lo llega a solucionar y elimina estas violaciones.
 
``DONT_USE_CELLS``
-----------------------------------------------------------------------------
Lista de celdas para no utilizar en las optimizaciones del resizer. (Predeterminado: contenidos de ``DRC_EXCLUDE_CELL_LIST``)

``PL_ESTIMATE_PARASITICS``
-----------------------------------------------------------------------------
Especifica si se debe ejecutar o no STA después del placement global utilizando OpenROAD’s estimate_parasitics -placement y generar reportes en ``logs/placement``. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

``PL_OPTIMIZE_MIRRORING``
-----------------------------------------------------------------------------
Especifica si se debe o no ejecutar optimize_mirroring cada vez que se ocurre un placement detallado. Esto reflejará las celdas siempre que sea posible para optimizar el diseño. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

Tras desactivar esta opción se observa lo siguiente en el registro del resizer:

.. figure:: ../img/placement/resizer-log_PL_OPTIMIZE_MIRRORING.png
  :name: resizer-log_PL_OPTIMIZE_MIRRORING
  :align: center

  Registro del resizer.

En donde una vez se realiza el análisis del placement, no se realiza mirroring en el placement detallado ya que no da ningún mensaje de información en comparación con el registro del modelo de referencia, en donde se indica la cantidad de celdas reflejadas.

``PL_RESIZER_BUFFER_INPUT_PORTS``
-----------------------------------------------------------------------------
Especifica si se insertan o no buffers en los puertos de entrada cada vez que se ejecutan optimizaciones de resizer. Para utilizar esto, ``PL_RESIZER_DESIGN_OPTIMIZATION`` debe  establecerse en 1. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

Tras deshabilitarlo las instancias en los puertos de salida se observan de la siguiente manera:

.. figure:: ../img/placement/PL_RESIZER_BUFFER_INPUT_PORTS.png
  :name: PL_RESIZER_BUFFER_INPUT_PORTS
  :align: center

  Layout del diseño, énfasis puertos de entrada

En donde de su reporte de área, se observa que disminuye la cantidad de buffers en los puertos de 242 a 208.

``PL_RESIZER_BUFFER_OUTPUT_PORTS``
-----------------------------------------------------------------------------
Especifica si se insertan o no buffers en los puertos de salida cada vez que se ejecutan optimizaciones de resizer. Para utilizar esto, ``PL_RESIZER_DESIGN_OPTIMIZATION`` debe establecerse en 1. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

Tras deshabilitarlo las instancias en los puertos de salida se observan de la siguiente manera:

.. figure:: ../img/placement/PL_RESIZER_BUFFER_OUTPUT_PORTS.png
  :name: PL_RESIZER_BUFFER_OUTPUT_PORTS
  :align: center

  Layout del diseño, énfasis puertos de salida

En donde de su reporte de área, se observa que disminuye la cantidad de buffers en los puertos de 242 a 38.

``PL_RESIZER_REPAIR_TIE_FANOUT``
-----------------------------------------------------------------------------
Especifica si si debe o no repara reparar el fanout de las celdas tie cuando se corren optimizaciones del resizer. Para utilizar esto, ``PL_RESIZER_DESIGN_OPTIMIZATIONS`` debe establecerse en 1. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

``PL_MAX_DISPLACEMENT_X``
-----------------------------------------------------------------------------
Especifica hasta qué punto se puede mover una instancia a lo largo del eje X al encontrar un sitio donde se puede colocar durante el placement detallado. (Predeterminado: `500` μm)

``PL_MAX_DISPLACEMENT_Y``
-----------------------------------------------------------------------------
Especifica hasta qué punto se puede mover una instancia a lo largo del eje Y al encontrar un sitio donde se puede colocar durante el placement detallado. (Predeterminado: `100` μm)

``PL_MACRO_HALO``
-----------------------------------------------------------------------------
Espacio de colocación macros. Formato: {Horizontal} {Vertical}. (Predeterminado: `0 0` μm).

``PL_MACRO_CHANNEL``
-----------------------------------------------------------------------------
Anchos de canal entre macros. Formato: {Horizontal} {Vertical}. (Predeterminado: `0 0` μm).

``MACRO_PLACEMENT_CFG``
-----------------------------------------------------------------------------
Especifica la ruta de un archivo que especifica cómo Openlane debe colocar ciertas macros.


Resumen de resultados:
===========================
Se va a comparar, en porcentajes, cuanto vario con respecto al modelo de referencia los parámetros mas importantes para esta etapa al modificar cada variable. Los valores de las variables son los mismo utilizados anteriormente, de modo que se tienen los siguientes resultados para cada etapa de placement:

.. list-table:: Comparación de parámetros con el modelo de referencia, etapa de placement global
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
  * - ``PL_TARGET_DENSITY``
    - -0.844
    - -2.57
    - 2.12
    - 0
    - 0
    - 0
    - 0
  * - ``PL_TIME_DRIVEN``
    - 0.0923
    - 0
    - -0.706
    - 0
    - -1
    - 0
    - 0
  * - ``PL_SKIP_INITIAL_PLACEMENT``
    - 0.0119
    - 0
    - -0.353
    - 0
    - 9
    - 0
    - 1
  * - ``PL_RESIZER_DESIGN_OPTIMIZATIONS``
    - 0.187
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
  * - ``PL_RESIZER_MAX_WIRE_LENGTH``
    - 21.5
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
  * - ``PL_WIRELENGTH_COEF``
    - 0.506
    - 1.28
    - -3.88
    - 0
    - 33
    - 0
    - 3
  * - ``PL_RESIZER_BUFFER_INPUT_PORTS``
    - -0.240
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
  * - ``PL_RESIZER_BUFFER_OUTPUT_PORTS``
    - -0.773
    - 0
    - 0
    - 0
    - 0
    - 0
    - 0
  
.. list-table:: Comparación de parámetros con el modelo de referencia, etapa de placement detallado
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
  * - ``PL_TARGET_DENSITY``
    - -0.844
    - -0.889
    - 3.738
    - 5.56
    - 0
    - 0
    - 0
  * - ``PL_TIME_DRIVEN``
    - 0.0923
    - 0
    - 0.311
    - 0
    - 0
    - 0
    - 0
  * - ``PL_SKIP_INITIAL_PLACEMENT``
    - 0.0119
    - -0.444
    - 0
    - 0
    - 0
    - 0
    - 0
  * - ``PL_RESIZER_DESIGN_OPTIMIZATIONS``
    - 0.187
    - 4.44
    - -14.6
    - -5.56
    - 22
    - 4
    - 2
  * - ``PL_RESIZER_MAX_WIRE_LENGTH``
    - 21.5
    - 15.6
    - -73.83
    - 5.56
    - 0
    - 0
    - 0
  * - ``PL_WIRELENGTH_COEF``
    - 0.506
    - 1.77
    - -3.11
    - 0
    - 0
    - 0
    - 0
  * - ``PL_RESIZER_BUFFER_INPUT_PORTS``
    - -0.240
    - -0.445
    - 0
    - 0
    - 0
    - 0
    - 0
  * - ``PL_RESIZER_BUFFER_OUTPUT_PORTS``
    - -0.773
    - -0.889
    - 0
    - 0
    - 0
    - 0
    - 0


Síntesis del árbol de reloj (CTS)
***************************************************

Configuración por defecto:
===========================
Revisando la ruta ``~/OpenLane/configuration/cts.tcl`` se encuentra la siguiente información en este archivo:

.. figure:: ../img/def/cts_var.png
  :name: cts_def
  :scale: 80 %
  :align: center

  Configuración por defecto de las variables de síntesis.

Descripcion y ejemplos:
===========================

``RUN_CTS``
-----------------------------------------------------------------------------
Habilite la síntesis del árbol de reloj. (Predeterminado: `1`)

``RUN_FILL_INSERTION``
-----------------------------------------------------------------------------
Habilita la inserción de celdas de relleno después de cts (si es posible). 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

``CTS_SINK_CLUSTERING_SIZE``
-----------------------------------------------------------------------------
Especifica el número máximo de receptores por cluster. (Predeterminado: `25`)

Al disminuir este valor a 8 se tiene la siguiente información en el registro de esta etapa:

.. figure:: ../img/cts/cts-log_CTS_SINK_CLUSTERING_SIZE_8.png
  :name: cts-log_CTS_SINK_CLUSTERING_SIZE_8
  :align: center

  Registro etapa cts.

Lo cual produce los siguientes cambios en el layout de esta etapa:

.. figure:: ../img/cts/CTS_SINK_CLUSTERING_SIZE_8.png
  :name: CTS_SINK_CLUSTERING_SIZE_8
  :align: center

  Layout etapa cts.

De donde se observa principalmente que se tiene mas instancias de buffers/inversores en el árbol de reloj, aumentado de 184 a 232. Lo cual produce un pequeño aumento en el área y además reduce significativamente las violaciones de fanout de 68 a 15, lo cual es significativamente positivo.

``CTS_SINK_CLUSTERING_MAX_DIAMETER``
-----------------------------------------------------------------------------
Especifica el diámetro máximo (en micrómetros) del receptor por clúster. (Predeterminado: `50`)

Al reducir este diámetro a la mitad de su valor predeterminado (25) se tiene la siguiente información en el registro de esta etapa:

.. figure:: ../img/cts/cts-log_CTS_SINK_CLUSTERING_MAX_DIAMETER_25.png
  :name: cts-log_CTS_SINK_CLUSTERING_MAX_DIAMETER_25
  :align: center

  Registro etapa cts.

Lo cual de forma similar a la variable anterior produce un aumento mayor en la cantidad de buffers/inversores en el árbol 
de reloj, aumentado a mas de doble a 494. Lo cual produce un mayor aumento en el área y reduce en mayor medida las
violaciones de fanout. Lo cual se observa en la siguiente imagen del layout:

.. figure:: ../img/cts/CTS_SINK_CLUSTERING_MAX_DIAMETER_25.png
  :name: CTS_SINK_CLUSTERING_MAX_DIAMETER_25
  :align: center

  Layout etapa cts.


``CTS_REPORT_TIMING``
-----------------------------------------------------------------------------
Especifica si se debe ejecutar o no STA después de la síntesis del árbol de reloj utilizando OpenROAD's estimate_parasitics -placement y generar genera informes en ``logs/cts``. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

``CTS_CLK_MAX_WIRE_LENGTH``
-----------------------------------------------------------------------------
Especifica la longitud máxima del cable en la red del reloj. Valor en micrómetros. (Predeterminado: `0`)

Al utilizar un valor de 50, se produce lo siguiente en el registro de esta etapa:

.. figure:: ../img/cts/cts-log_CTS_CLK_MAX_WIRE_LENGTH_50.png
  :name: cts-log_CTS_CLK_MAX_WIRE_LENGTH_50
  :align: center

  Registro etapa cts.

Lo cual se ve reflejado en el reporte de área y el layout de la siguiente manera:

.. figure:: ../img/cts/CTS_CLK_MAX_WIRE_LENGTH_50.png
  :name: CTS_CLK_MAX_WIRE_LENGTH_50
  :align: center

  Layout etapa cts.

Además esto produce un aumento considerable en el skew, pasando de 0.24 a 1.07 por aumento en la latencia de 
la señal de reloj.

``CTS_DISABLE_POST_PROCESSING``
-----------------------------------------------------------------------------
Especifica si se deshabilita o no el procesamiento posterior a cts para receptores atípicos. (Predeterminado: `0`)

``CTS_DISTANCE_BETWEEN_BUFFERS``
-----------------------------------------------------------------------------
Especifica la distancia (en micrómetros) entre buffers al crear  el árbol de reloj. (Predeterminado: `0`)

Utilizando un valor de 50 um, se tiene la siguiente información en el registro de esta etapa:

.. figure:: ../img/cts/cts-log_CTS_DISTANCE_BETWEEN_BUFFERS_50.png
  :name: cts-log_CTS_DISTANCE_BETWEEN_BUFFERS_50
  :align: center

  Registro etapa cts.


``LIB_CTS``
-----------------------------------------------------------------------------
El archivo biblioteca utilizado para CTS para las esquina típica. De forma predeterminada, este es ``LIB_SYNTH`` menos las
celdas con errores de drc según lo especificado en la lista de exclusión de drc. (Predeterminado: ``$::env(cts_tmpfiles)/cts.lib``)

``LIB_CTS_SLOWEST``
-----------------------------------------------------------------------------
El archivo biblioteca utilizado para CTS para las esquina mas lenta. De forma predeterminada, este es ``LIB_CTS_SLOWEST`` menos las celdas con errores de drc según lo especificado en la lista de exclusión de drc. (Predeterminado: ``$::env(cts_tmpfiles)/cts-slowest.lib``)

``LIB_CTS_FASTEST``
-----------------------------------------------------------------------------
El archivo biblioteca utilizado para CTS para las esquina mas rapida. De forma predeterminada, este es ``LIB_CTS_FASTEST`` menos las celdas con errores de drc según lo especificado en la lista de exclusión de drc. (Predeterminado: ``$::env(cts_tmpfiles)/cts-fastest.lib``)

``CTS_MULTICORNER_LIB``
-----------------------------------------------------------------------------
Una bandera para leer las esquinas mas rapida y lenta durante CTS. (Predeterminado: `1`)


Resumen de resultados:
===========================
Se va a comparar, en porcentajes, cuanto vario con respecto al modelo de referencia los parámetros mas importantes para esta etapa al modificar cada variable. Los valores de las variables son los mismo utilizados anteriormente, de modo que se tienen los siguientes resultados para la etapa de cts:

.. list-table:: Comparación de parámetros con el modelo de referencia, etapa de cts
  :header-rows: 1
  :align: center

  * - Variables
    - Chip Area
    - Potencia 
    - Peor Setup 
    - Peor Hold 
    - Skew
    - Violaciones Slew
    - Violaciones Fanout
    - Violaciones Cap
  * - ``CTS_SINK_CLUSTERING_SIZE``
    - 1.15
    - 3.27
    - 0
    - 0
    - 4.16
    - 0
    - -53
    - 0
  * - ``CTS_SINK_CLUSTERING_MAX_DIAMETER``
    - 7.40
    - 22.2
    - -0.93
    - 0
    - -4.16
    - 0
    - -66
    - 0
  * - ``CTS_CLK_MAX_WIRE_LENGTH``
    - 0.535
    - 1.45
    - -24.9
    - -482
    - 345
    - 0
    - -11
    - 0
  * - ``CTS_DISTANCE_BETWEEN_BUFFERS``
    - 0.18
    - 0.364
    - 0.311
    - 0
    - 8.33
    - 0
    - -1
    - 0

Routing global y detallado (GRT/DRT)
***************************************************

Configuración por defecto:
===========================
Revisando la ruta ``~/OpenLane/configuration/routing.tcl`` se encuentra la siguiente información en este archivo:

.. figure:: ../img/def/rt_var.png
  :name: rt_def
  :scale: 80 %
  :align: center

  Configuración por defecto de las routing

Descripción y ejemplos:
===========================

``RUN_DRT``
-----------------------------------------------------------------------------
Habilita routing detallado. 1 = Habilitado, 0 = Deshabilitado (Predeterminado: `1`)

``GLOBAL_ROUTER``
-----------------------------------------------------------------------------
Especifica cual routing global usar. Valores: ``fastroute``. (``cugr`` está en desuso). (Predeterminado: ``fastroute``)

``DETAILED_ROUTER``
-----------------------------------------------------------------------------
Especifica qué routing detallado usar. Valores: ``tritonroute``. (``drcu/tritonroute_or`` están obsoletos). (Predeterminado: ``tritonroute``)

``ROUTING_CORES``
-----------------------------------------------------------------------------
Especifica el número de subprocesos que se utilizarán en TritonRoute. Se puede anular mediante una variable de entorno. (Predeterminado: `2`)

Al aumentarlo al doble de subprocesos de su valor predeterminado se obtiene la siguiente información en el registro de la subetapa de routing detallado:

.. figure:: ../img/routing/detailed-log_ROUTING_CORES_4.png
  :name: detailed-log_ROUTING_CORES_4
  :align: center

  Registro subetapa routing detallado.

Lo cual produce un reducción en el tiempo de duración de esta subetapa optimizando TritonRoute.

``RT_CLOCK_MIN_LAYER``
-----------------------------------------------------------------------------
El nombre de la capa más baja que se utilizará para enrutar la red del reloj. (Predeterminado: ``RT_MIN_LAYER``)

``RT_CLOCK_MAX_LAYER``
-----------------------------------------------------------------------------
El nombre de la capa más alta que se utilizará para enrutar la red del reloj. (Predeterminado: ``RT_MAX_LAYER``)

``GLB_RESIZER_TIMING_OPTIMIZATIONS``
-----------------------------------------------------------------------------
Especifica si las optimizaciones de tiempo del resizer deben realizarse después del routing global o no. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

Tras desactivar estas optimizaciones se produce que ligeramente el tiempo de llegada de los datos aumente disminuye el setup slack de 4.09 a 3.87. Además el layout se modifica ligeramente de la siguiente manera:

.. figure:: ../img/routing/GLB_RESIZER_TIMING_OPTIMIZATIONS.png
  :name: GLB_RESIZER_TIMING_OPTIMIZATIONS
  :align: center

  Layout etapa routing.

De donde se observa de su registro de área que los principales cambios son producto de menor instancias de buffers/inversores de optimizaciones de temporización, lo cual a su vez modifica ligeramente las instancias de la parte fisica. En general esto produce que se reduzca ligeramente el área.

``GLB_RESIZER_DESIGN_OPTIMIZATIONS``
-----------------------------------------------------------------------------
Especifica si las optimizaciones del diseño del resizer deben realizarse después del routing global o no. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

Al desactivar estas optimizaciones se produce un aumento considerablemente de las violaciones de fanout, pasando de 102 a 123. Además el layout se modifica ligeramente de la siguiente manera:

.. figure:: ../img/routing/GLB_RESIZER_DESIGN_OPTIMIZATIONS.png
  :name: GLB_RESIZER_DESIGN_OPTIMIZATIONS
  :align: center

  Layout etapa routing.


``GLB_RESIZER_MAX_WIRE_LENGTH``
-----------------------------------------------------------------------------
Especifica el límite de longitud máxima del cable utilizado por el resizer para insertar buffers. Si se establece en 0, no se insertarán buffers. Valor en micrómetros. (Predeterminado: `0`)

``GLB_RESIZER_MAX_SLEW_MARGIN``
-----------------------------------------------------------------------------
Especifica un margen para el slew. (Predeterminado: `10`)

Al aumentar este margen 10 veces su valor determinado, se obtiene la siguiente información en el registro del resizer:

.. figure:: ../img/routing/resizer-log_GLB_RESIZER_MAX_SLEW_MARGIN_100.png
  :name: resizer-log_GLB_RESIZER_MAX_SLEW_MARGIN_100
  :align: center

  Registro del resizer de la etapa routing.

Donde se observa que al aumentar este margen produce que se detectan 10687 violaciones de slew que produce el redimensionamiento de 425 instancias; que al comprar con la cantidad de instancias redimensionadas del modelo de referencia, se tienen 12 instancias mas.

``GLB_RESIZER_MAX_CAP_MARGIN``
-----------------------------------------------------------------------------
Especifica un margen para las capacitancias. (Predeterminado: `10`)

Al aumentar este margen 5 veces su valor determinado, se obtiene la siguiente información en el registro del resizer:

.. figure:: ../img/routing/resizer-log_GLB_RESIZER_MAX_CAP_MARGIN_50.png
  :name: resizer-log_GLB_RESIZER_MAX_CAP_MARGIN_50
  :align: center

  Registro del resizer de la etapa routing.

Se observa que al aumentar este margen se produce 2 violaciones de capacitancias y para solucionarlas se inserta 1 buffer en 2 nets. Además se tienen 1 instancia mas redimensionada en comparación con el modelo de referencia.

``GLB_RESIZER_HOLD_SLACK_MARGIN``
-----------------------------------------------------------------------------
Especifica un margen de tiempo para el slack al corregir violaciones de hold. Normalmente, el resizer se detendrá cuando llegue a cero slack. Esta opción le permite sobrefijar. (Predeterminado: `0.05` ns) 

``GLB_RESIZER_SETUP_SLACK_MARGIN``
-----------------------------------------------------------------------------
Especifica un margen de tiempo para el salck al corregir violaciones de setup. (Predeterminado: `0.025` ns)

``GLB_RESIZER_HOLD_MAX_BUFFER_PERCENT``
-----------------------------------------------------------------------------
Especifica una cantidad máxima de buffers que se insertarán para corregir violaciones de hold. Este número se calcula como un porcentaje del número de instancias en el diseño. (Predeterminado: `50`) 

``GLB_RESIZER_SETUP_MAX_BUFFER_PERCENT``
-----------------------------------------------------------------------------
Especifica una cantidad máxima de buffers que se insertarán para corregir violaciones de setup. Este número se calcula como un porcentaje del número de instancias en el diseño. (Predeterminado: `50`)

``GLB_RESIZER_ALLOW_SETUP_VIOS``
-----------------------------------------------------------------------------
Permite violaciones de setup al corregir hold. (Predeterminado: `0`)

``GLB_OPTIMIZE_MIRRORING``
-----------------------------------------------------------------------------
Especifica si se ejecuta o no optimize_mirroring cada vez que define un placement detallado de una instancia después de las
optimizaciones de tiempo del routing. Esto reflejará las celdas siempre que sea posible para optimizar el diseño. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

Al deshabilitar estas optimizaciónes se tiene la siguiente información del registro del resizer:

.. figure:: ../img/routing/resizer-log_GLB_OPTIMIZE_MIRRORING.png
  :name: resizer-log_GLB_OPTIMIZE_MIRRORING
  :align: center

  Registro del resizer de la etapa routing.

Donde vemos que al comprar con el registro del modelo de referencia, no se reflejan 4605 instancias.

``GRT_ALLOW_CONGESTION``
-----------------------------------------------------------------------------
Permitir congestión en las guías resultantes. 0 = falso, 1 = verdadero. (Predeterminado: `0`)

``GRT_OVERFLOW_ITERS``
-----------------------------------------------------------------------------
El número máximo de iteraciones en espera de que el desbordamiento alcance el valor deseado. (Predeterminado: `50`)

``GRT_ANT_ITERS``
-----------------------------------------------------------------------------
El número máximo de iteraciones para repair_antenna del routing global. Esta opción solo está disponible cuando ``GRT_REPAIR_ANTENNAS`` está habilitado. (Predeterminado: `15`)

Al reducir la cantidad de iteraciones a 3 vemos que se tiene la siguiente información en el registro de routing global:

.. figure:: ../img/routing/global-log_GRT_ANT_ITERS_3.png
  :name: global-log_GRT_ANT_ITERS_3
  :align: center

  Registro de routing global.

Comparando con el registro de routing global del modelo de referencia se observa que se tiene una iteración menos  por lo que produce que quedan pendientes 6 violaciones de antenna.

``GRT_ANT_MARGIN``
-----------------------------------------------------------------------------
El margen, en porcentaje, para corregir violaciones de antena en el routing global. Esta opción solo está disponible cuando ``GRT_REPAIR_ANTENNAS`` está habilitado. (Predeterminado: `10`)

Al aumenter este margen al doble de su valor se tiene la siguiente información en el registro de routing global:

.. figure:: ../img/routing/global-log_GRT_ANT_MARGIN_20.png
  :name: global-log_GRT_ANT_MARGIN_20
  :align: center

  Registro de routing global.

Comparando con el registro de routing global del modelo de referencia se tiene que se ocupa 1 iteracion mas para completar lograr eliminar las violaciones de antenna, desde la primer iteración se encuentran 8 violaciones mas y se inserta una mayor cantidad diodos. Lo cual todo esto produce los siguientes cambios en el layout:

.. figure:: ../img/routing/GRT_ANT_MARGIN_20.png
  :name: GRT_ANT_MARGIN_20
  :align: center

  Layout etapa de routing.

De donde la mayor diferencia con el modelo de referencia es en el aumento significativo en las instancias de antenna, como se observa en el reporte de area de la imagen anterior que hay 379 instancias que son 102 mas. Esto a su vez produce cambios en el diseño físico y área del chip.

``GRT_ESTIMATE_PARASITICS``
-----------------------------------------------------------------------------
Especifica si se debe ejecutar o no STA después del routing global usando OpenROAD’s estimate_parasitics -global_routing 
y generar informes en ``logs/routing``. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: 1)

``GRT_MAX_DIODE_INS_ITERS``
-----------------------------------------------------------------------------
Controla el número máximo de iteraciones en las que se detiene la repetición de Fastroute para la inserción de diodos. En cada iteración, ARC detecta las infracciones y FastRoute las corrige insertando diodos y luego produciendo el nuevo DEF. El número de violaciones de antena se compara con la iteración anterior y si son iguales o el número es mayor las iteraciones se detienen y el DEF de la iteración anterior se utiliza en el resto del flujo. Si las violaciones actuales de la antena llegan a cero, se utilizará la definición actual y las iteraciones no continuarán. Esta opción solo está disponible cuando ``GRT_REPAIR_ANTENNAS`` está habilitado. (Predeterminado: `1`)

``GRT_REPAIR_ANTENNAS``
-----------------------------------------------------------------------------
Habilita el flujo para evadir antena de OpenROAD's. (Predeterminado: `1`)

``GRT_OBS``
-----------------------------------------------------------------------------
Especifica la obstrucción personalizada que se agregará antes del routing global como capa y coordenadas en el formato ``layer llx lly urx ury``; donde: ``ll`` y ``ur`` "representan inferior izquierda" y "superior derecha", respectivamente por sus siglas en ingles. En JSON, se declaran como una matriz de caracteres y en Tcl se utilizan comas como delimitador. (Ejemplo: ``li1 0 100 1000 300, met5 0 0 1000 500``). (Predeterminado: no definido)

``GRT_ADJUSTMENT``
-----------------------------------------------------------------------------
Reducción de la capacidad de routing de los bordes entre las celdas en el grafo de routing global. Los valores varían de 0 a 1. 1 = mayor reducción, 0 = menor reducción. (Predeterminado: `0.3`)

Al reducir esta capacidad a 0.1 se obtiene el siguiente layout:

.. figure:: ../img/routing/GRT_ADJUSTMENT_0.1.png
  :name: GRT_ADJUSTMENT_0.1
  :align: center

  Layout etapa de routing.

De donde se observa considerables cambio en el metal donde se ve reducido, a su vez disminuye el area fisica y las instancias de antenna.

``GRT_MACRO_EXTENSION``
-----------------------------------------------------------------------------
Establece la cantidad de GCells agregadas a los límites de los bloqueos desde las macros. Una GCell normalmente se define en términos de pistas de routing Mx. El tamaño predeterminado de GCell es de 15 pasos M3. (Predeterminado: `0`)

``DRT_MIN_LAYER``
-----------------------------------------------------------------------------
Una anulación opcional de la capa más baja utilizada en el routing detallado. Por ejemplo, en sky130, es posible que desee que el routing global evite li1, pero permita que el routing detallado use li1 si es necesario. (Predeterminado: ``RT_MIN_LAYER``)

``DRT_MAX_LAYER``
-----------------------------------------------------------------------------
Una anulación opcional de la capa más alta utilizada en el routing detallado. (Predeterminado: ``RT_MAX_LAYER``)

``DRT_OPT_ITERS``
-----------------------------------------------------------------------------
Especifica el número máximo de iteraciones de optimización durante el routing detallado en TritonRoute. (Predeterminado: `64`)

Al reducir el numero de iteraciones a 3, se obtiene la siguiente información en el registro de routing detallado:

.. figure:: ../img/routing/detailed-log_DRT_OPT_ITERS_3.png
  :name: detailed-log_DRT_OPT_ITERS_3
  :align: center

  Registro etapa routing detallado.

De donde se observa que esto producen 1290 violaciones pendientes que resolver, ya que al compara con el registro del modelo de referencia estas violaciones pendientes se resuelven el doble de iteraciones.

Resumen de resultados:
===========================
Se va a comparar, en porcentajes, cuanto vario con respecto al modelo de referencia los parámetros mas importantes para esta etapa al modificar cada variable. Los valores de las variables son los mismo utilizados anteriormente, de modo que se tienen los siguientes resultados para la  etapa de cts:

.. list-table:: Comparación de parámetros con el modelo de referencia, etapa de routing
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
  * - ``GLB_RESIZER_TIMING_OPTIMIZATIONS``
    - -0.133
    - 0
    - -5.38
    - 0
    - 0
    - 4
    - 0
  * - ``GLB_RESIZER_DESIGN_OPTIMIZATIONS``
    - -0.703
    - -0.411
    - -2.44
    - 0
    - 0
    - 21
    - 0
  * - ``GLB_RESIZER_MAX_SLEW_MARGIN``
    - -0.142
    - 0
    - 0
    - 0
    - 0
    - -2
    - 0
  * - ``GLB_RESIZER_MAX_CAP_MARGIN``
    - 0.002
    - 0
    - 0
    - 0
    - 0
    - 1
    - 0
  * - ``GLB_OPTIMIZE_MIRRORING``
    - -0.144
    - 0
    - 0
    - 0
    - 0
    - -8
    - 0
  * - ``GRT_ANT_MARGIN``
    - 0.248
    - 0.411
    - 0
    - 0
    - 0
    - 7
    - 0
  * - ``GRT_REPAIR_ANTENNAS``
    - -0.583
    - 0
    - 0
    - 0
    - 0
    - -34
    - 0
  * - ``GRT_REPAIR_ANTENNAS``
    - -0.420
    - 0
    - 0
    - 0
    - 0
    - -22
    - 0


Scripts de inserción de diodos personalizada
***************************************************

Configuración por defecto:
===========================
Revisando la ruta ``~/OpenLane/configuration/routing.tcl`` se encuentra la siguiente información en este archivo:

.. figure:: ../img/def/CDIS_var.png
  :name: CDIS_def
  :align: center

  Configuración por defecto de las variables de inserción de diodos personalizada.

Descripción y ejemplos:
===========================

``RUN_HEURISTIC_DIODE_INSERTION``
-----------------------------------------------------------------------------
Ejecuta un script de Sylvain Munaut que inserta diodos heurísticamente. 1 = Habilitado, 0 = Deshabilitado
(Predeterminado: `0`)

``HEURISTIC_ANTENNA_THRESHOLD``
-----------------------------------------------------------------------------
Distancia mínima de una red para insertar un diodo en micrómetros. Solo se aplica para ``RUN_HEURISTIC_DIODE_INSERTION``
está habilitado. (Predeterminado: 90)

Aumentado esta distancia al doble, ya que con su valor predeterminado el flujo no es completado por problemas de congestionamiento, se obtiene la siguiente información del registro de diodos:

.. figure:: ../img/cdis/diodes-log_HEURISTIC_ANTENNA_THRESHOLD_180.png
  :name: ddiodes-log_HEURISTIC_ANTENNA_THRESHOLD_180
  :align: center

  Registro diodos, etapa routing detallado.

Lo cual se puede observar en el siguiente layout y su reporte de área:

.. figure:: ../img/cdis/HEURISTIC_ANTENNA_THRESHOLD_180.png
  :name: HEURISTIC_ANTENNA_THRESHOLD_180
  :align: center

  Layout etapa routing, énfasis instancias antenna.

``DIODE_ON_PORTS``
-----------------------------------------------------------------------------
Inserta diodos en los puertos con las polaridades especificadas. Las opciones disponibles son: ninguna, dentro, fuera y ambas (none, in, out y both). (Predeterminado: `none`)

Utilizando la configuración ambas (both) se obtiene un nuevo de registro de diodos IO con la siguiente información:

.. figure:: ../img/cdis/io-diodes-log.png
  :name: io-diodes-log
  :align: center

  Registro diodos IO.

Estos diodos se puede apreciar en el siguiente layout y registro de área:

.. figure:: ../img/cdis/DIODE_ON_PORTS_both.png
  :name: DIODE_ON_PORTS_both
  :align: center

  Registro diodos IO.

Ya que se tienen 311, 35 mas en comparación con los 277 que se tienen en el modelo de referencia.

Capacitancias y resistencias parásitas
***************************************************

Configuración por defecto:
===========================
Revisando la ruta ``~/OpenLane/configuration/extraction.tcl`` se encuentra la siguiente información en este archivo:


.. figure:: ../img/def/RCX_var.png
  :name: RCX_def
  :scale: 80 %
  :align: center

  Configuración por defecto de las variables de síntesis.

Descripción:
===========================

``RUN_SPEF_EXTRACTION``
-----------------------------------------------------------------------------
Especifica si se debe ejecutar o no la extracción SPEF en el DEF enrutado. 1 = Habilitado 0 = Deshabilitado. (Predeterminado: `1`)

``SPEF_EXTRACTOR``
-----------------------------------------------------------------------------
Especifica cual extractor spef usar. Valores: ``openrcx`` (eliminado: ``def2spef``). (Predeterminado: ``openrcx``)

``RCX_MERGE_VIA_WIRE_RES``
-----------------------------------------------------------------------------
Especifica si se debe fusionar la resistencia de vía con la resistencia del cable o separarla de la resistencia del cable. 1 = Fusionar mediante resistencia, 0 = Separar mediante resistencia. (Predeterminado: `1`)

Análisis de caída de IR
***************************************************

Descripción:
===========================

``RUN_IRDROP_REPORT``
-----------------------------------------------------------------------------
Crea un informe de caída de IR utilizando OpenROAD PSM. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

``VSRC_LOC_FILES``
-----------------------------------------------------------------------------
Archivo loc PSM para redes eléctricas y terrestres. La variable debe proporcionarse como una lista json/tcl o una cadena tcl delimitada por espacios de la siguiente manera: ``net1 archivo1 net2 archivo2``. Vea `esto <https://github.com/The-OpenROAD-Project/OpenROAD/tree/master/src/psm#commands>`_ para más información. (Predeterminado: NINGUNO)

Signoff
***************************************************

Configuración por defecto:
===========================
Revisando la ruta ``~/OpenLane/configuration/general.tcl`` se encuentra la siguiente información en este archivo:


.. figure:: ../img/def/signoff_var.png
  :name: signoff_def
  :align: center

  Configuración por defecto de las variables de signoff.

Descripción:
===========================

``PRIMARY_SIGNOFF_TOOL``
-----------------------------------------------------------------------------
Determina si ``magic`` o ``klayout`` es la herramienta de signoff principal.
(Predeterminado: ``magic``)

``USE_ARC_ANTENNA_CHECK``
-----------------------------------------------------------------------------
Especifica si se debe utilizar el checker de antena Openroad ARC o el checker de antena magic.
0 = comprobador de antena magic, 1 = checker de antena ARC OR. (Predeterminado: 1)

``RUN_CVC``
-----------------------------------------------------------------------------
Ejecuta CVC en la especia de salida, que es un verificador de validez de circuito. Checker ERC consciente
del voltaje para listas de red CDL. 1 = Habilitado, 0 = Deshabilitado. (Predeterminado: `1`)

``SIGNOFF_SDC_FILE``
-----------------------------------------------------------------------------
Especifica el archivo SDC utilizado por STA multiesquina durante la etapa de signoff, que puede ser diferente del utilizado para la implementación. (Predeterminado: ``BASE_SDC_FILE``)