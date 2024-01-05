.. OpenLane documentation master file, created by
   sphinx-quickstart on Tue Sep  5 21:39:46 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



Manual de uso de la herramienta OpenLane
========================================
.. warning:: 
   Este proyecto se encuentra  bajo desarrollo...


La siguiente documentación busca complementar el uso de la herramienta OpenLane para estudiantes de la `Escuela de Ingeniería Eléctrica de la UCR <https://eie.ucr.ac.cr/>`_.
Esta misma fue creada a partir de la documentación ya existente de `OpenLane documentación oficial <https://openlane.readthedocs.io/en/latest/index.html>`_.

Se documentarán las siguientes varaibles de configuración:

.. toctree::
   :maxdepth: 1
   :caption: Contenido:
   :glob:

   general
   macros
   synthesis
   ta
   design

Además se ilustrará el funcionamiento, por medio de ejemplos, los siguientes principales pasos del flujo de diseño:

.. toctree::
   :maxdepth: 1
   :caption: Contenido:
   :glob:

   synthesis
   design

Ejemplos que se compararan con un modelo de referencia para entender su funcionamiento en el diseño.

Modelo de referencia
---------------------
Para esto se utilizo el diseño **picrov32a**; el cual viene por defecto en la herramienta y es utilizado 
para realizar la evaluación del impacto de cada parámetro. Este diseño es un pequeño procesador RISC-V (RV32I) y ejecuta funcionalidades cruciales de la
herramienta. 

El modelo de referencia van a ser los resultados de pasos para el diseño con la configuración por defecto que
genera la herramienta. Esta configuración se ve de la siguiente manera en su archivo *.json*:

.. figure:: ../img/def/config.png
   :name: config_def
   :scale: 80 %
   :align: center
   
   Configuración por defecto

Tras ejecutar el flujo de la herramienta se tienen los siguientes resultados para cada paso. Primeramente el 
registro de advertencias (*warnings.log*) muestra los siguientes mensajes:

.. figure:: ../img/def/warnings.png
   :name: warnings_def
   :scale: 50 %
   :align: center
   
   Mensajes del registro de adverencias para la configuración por defecto.

#. En la etapa de síntesis lógica se tiene como resultados principales los siguientes reportes:

   .. figure:: ../img/def/area0-report.png
      :name: area0-report
      :scale: 60 %
      :align: center

      Reporte area.

   .. figure:: ../img/def/power-report.png
      :name: power-report.
      :scale: 60 %
      :align: center

      Reporte potencia.

   .. figure:: ../img/def/sta-report.png
      :name: sta-report
      :scale: 60 %
      :align: center

      Reporte sumatoria sta.

#. En la etapa de floorplan se tiene como resultado principal el layout del circuito, el cual es el siguiente:
  
   .. figure:: ../img/def/FP_DEFAULT.png
      :name: layout_fp
      :align: center

      Layout etapa de floorplan.

#. En la etapa de placement se tiene como resultados el layout del circuito, el cual es el siguiente:

   .. figure:: ../img/def/PL_DEFAULT.png
      :name: layout_pl
      :align: center

      Layout etapa de placement.

   Además, de sus dos subetapas se tiene los siguientes valores de los parámetros de interés, tomados de los reportes respectivos:

   .. list-table:: Parámetros de interés para etapa placement
      :header-rows: 1
      :align: center

      * - Parametros
        - Placement Global
        - Placement Detallado
      * - Chip Area (:math:`μm^{2}`)
        - 100274.922
        - 100274.922
      * - Potencia (`W`)
        - 2.33e-2
        - 2.25e-2
      * - Peor Setup (`ns`)
        - 2.83
        - 3.21
      * - Peor Hold (`ns`)
        - 0.17
        -  0.18
      * - Violaciones Slew
        - 22
        - 0
      * - Violaciones Fanout
        - 4
        - 0
      * - Violaciones Cap
        - 2
        - 0

#. En la etapa de routing se tiene como resultados el siguiente layout:

   .. figure:: ../img/def/RT_DEFAULT.png
      :name: layout_rt
      :align: center

      Layout etapa de routing.

   También los siguientes registros de sus subetapas con información importante de cada una de ellas:

   .. figure:: ../img/def/rt-global-log_default.png
      :name: global-log_default
      :align: center

      Registro subetapa routing global

   .. figure:: ../img/def/rt-detailed-log_default.png
      :name: detailed-log_default
      :align: center

      Registro subetapa routing detallado
      
   Y además los siguientes valores de los parámetros de interés, tomados de los reportes respectivos:

   .. list-table:: Parámetros de interés para etapa routing
      :header-rows: 1
      :align: center

      * - Parametros
        - Valores
      * - Chip Area (:math:`μm^{2}`)
        - 118971.603
      * - Potencia (`W`)
        - 2.43e-2
      * - Peor Setup (`ns`)
        - 4.09
      * - Peor Hold (`ns`)
        - 0.19
      * - Violaciones Slew
        - 0
      * - Violaciones Fanout
        - 102
      * - Violaciones Cap
        - 0

#. En la etapa de síntesis de árbol de reloj (CTS) se tiene como resultados el siguiente layout:

   .. figure:: ../img/def/CTS_DEFAULT.png
      :name: layout_cts
      :align: center

      Layout etapa de cts.

   También el registro con información importante de esta etapa:

   .. figure:: ../img/def/cts-log_default.png
      :name: cts-log
      :align: center

      Registro de la etapa de cts.

   Y además los siguientes valores de los parámetros de interés, tomados de los reportes respectivos:

   .. list-table:: Parámetros de interés para etapa cts
      :header-rows: 1
      :align: center

      * - Parametros
        - Valores
      * - Chip Area (:math:`μm^{2}`)
        - 104699.165
      * - Potencia (`W`)
        - 2.75e-2
      * - Peor Setup (`ns`)
        - 3.21
      * - Peor Hold (`ns`)
        - 0.17
      * - Skew (`ns`) 
        - 0.24
      * - Violaciones Slew
        - 0
      * - Violaciones Fanout
        - 68
      * - Violaciones Cap
        - 0
