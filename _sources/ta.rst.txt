Análisis de temporización estatico (STA)
#########################################
.. contents:: Contenidos
    :depth: 3
    
Descripción:
***********************

``STA_REPORT_POWER``
=============================
Habilita el reporte de potencia en sta. (Predeterminado: `1`)

``EXTRA_SPEFS``
=============================
Especifica archivos spef mínimo, nom y máximo para los módulos. La variable debe proporcionarse como una lista json/tcl o una cadena tcl delimitada por espacios. Tenga en cuenta que se proporciona un nombre de módulo, no un nombre de instancia. Un módulo puede tener varias instancias. Cada módulo debe tener definidos 3 archivos,
uno para cada esquina. Por ejemplo: ``module1 min1 nom1 max1 module2 min2 nom2 max2``. Un archivo se puede utilizar varias veces en caso de ausencia de otros archivos de esquina. Por ejemplo: ``module nom nom nom``. En este caso, el archivo nom se utilizará en todos los rincones de sta. En todo momento un módulo debe especificar 3 archivos.
(Predeterminado: NINGUNO)

=============================
Controla si un modelo de temporizacion se escribe utilizando OpenROAD o OpenSTA después de sta. Esta es una opción ya que, en su estado actual, la generación del modelo de temporizacion (y el modelo en sí) puede tener bastantes errores. (Predeterminado: 1)