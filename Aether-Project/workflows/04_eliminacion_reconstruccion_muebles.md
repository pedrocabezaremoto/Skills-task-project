# Workflow: Eliminación y Reconstrucción Multiturno de Muebles

**Objetivo:** "Vaciar" digitalmente una habitación paso a paso tapando y eliminando piezas de mobiliario, para luego, desde una habitación limpia (sin muebles generados), escribir un Prompt Inverso que instruya a un usuario de IA externo cómo volver a llenarla sin mencionar los objetos anteriores ni la imagen base. Se realiza en `multimango.com`. Prohibición de IA.

## Paso 1: Enmascaramiento del Objeto Quitar (Masking Quirúrgico)
Debe realizarse **objeto por objeto**, uno a la vez. Entiéndase por muebles desde candelabros hasta alfombras, electrodomésticos visuales y decoración.
1. Pintar sobre la silla o la mesa. Ajustar tamaño de brochas.
2. **NUNCA SOBRE-ENMASCARAR:** No tirar un brochazo grueso gigante que tape a medias con mucho borde invisible el fondo, esto forzará a la IA a inpaintar media habitación, y generará un artefacto.

## Paso 2: Ejecutar el Borrado ("Removal Prompt")
Escribe algo sucinta y llanamente directo:
> *"Remove the blanket on the couch"*
> *"Remove the chandelier above the dining table"*

## Paso 3 y 4: Auditar Variantes Generadas y Confirmar Eliminación
La IA arrojará dos opciones sin el objeto.
1. Utiliza el Flipbook o la vista en lupa. Inspecciona donde estaba el objeto.
2. **Requisito para aceptar:** El fondo tuvo que reconstruirse perfecto. Las líneas del parquet concuerdan, el papel tapiz cuadra, o la base de la chimenea no se difumina como una plastilina goteada. Y OBLIGATORIO: Se han borrado sus sombras proyectadas y reflejos en vidrios.
3. **Rechazo (Reject & Try Again):** Sombras flotantes (error CE3 fatal). Si no existe una buena variante, rechazar y reintentar un enmascaramiento más ajustado.
4. Si es impecable, presiona **"Accept & Remove Another"**.

## Paso 5: El "Prompt de Reconstrucción Final"
Tras haber retirado todos y cada uno de los elementos clave iterativamente, la habitación queda virtualmente desocupada de decoración o muebles. Debes redactar un único requerimiento de reconstrucción (Reverse Prompt).

**Reglas Críticas del Prompt Inverso:**
- Redáctalo como si fueras un diseñador partiendo de un cuarto pelón, usando **SOLO EL RESULTADO** sin memoria.
- NO puedes decir: "vuelve a poner las cosas", "coloca en su lugar", ni mencionar de dónde salieron.
- **Nivel de detalle Extremo (Excelente CE1):** Requiere especificar colores precisos, materiales de muebles, texturas relativas, y direcciones.

### *Ejemplo de calidad Excelente:*
*"Coloque un candelabro de metal oscuro colgando de las vigas de madera sobre la mesa del comedor al fondo. Coloque una manta tejida azul oscuro sobre el borde izquierdo del sofá blanco. Coloque una cesta en la esquina junto al centro de entretenimiento con una manta asomando por el frente, y un cuenco con pequeñas plantas artificiales verdes sobre la mesa de centro negra."*
