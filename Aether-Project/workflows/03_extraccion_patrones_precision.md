# Workflow: Extracción de Patrones de Precisión Píxel por Píxel

**Objetivo:** Crear una máscara "estrecha pero generosa" (perfecta pero que solape milimétricamente hacia el fondo) sobre un objeto para permitir a la IA intercambiar patrones decorativos de manera fluida (Ej. Navidad por Halloween). Tarea realizada en `multimango.com`. Total prohibición de uso de IA como ChatGPT.

## 1. Verificación Inicial (Encuadre)
Asegurarse de que el encuadre (Aspect Ratio) de la imagen es óptimo.
1. La etiqueta del artículo debe coincidir con la de la imagen a procesar.
2. Comprobar que el "Collapse" o la caja límite incluya al objeto completo.
3. Si la imagen está absurdamente recortada de origen, **Skip This Entry**.

## 2. Definición del Patrón a Enmascarar (Máscara Inicial)
El proceso de máscara requiere un trabajo exhaustivo para rellenar completamente el objeto, sin huecos (islas) dentro).
- **Herramienta Inteligente (`Magic Selector` y `Smart Expand`):** Seleccionar haciendo clic. Arrastrar hacia fuera de los límites aumenta tolerancia de colores; hacia el centro, la reduce.
- **Limpieza (`Brush +/-`):** Borrar (Remove) partes extras del encuadre como sombras artificiales proyectadas, paredes traseras, el suelo, accesorios colgantes colindantes o cualquier cosa que la IA vaya a modificar por error.
- **Prevención de Bordes Fantasma (`Grow/Shrink`):** Expandir **(Grow)** ligeramente la máscara final por unos pocos píxeles. Una máscara ligerísimamente salida garantiza mejor adherencia a la imagen. La presencia de huecos o píxeles originales en el borde resultará en rechazo automático.

## 3. Validación Interna y Autoevaluación
Es obligatorio alternar filtros antes de dar clic al botón de siguiente paso.
- Usa los filtros de vista "With Pattern" y "Without Pattern".
- Pregunta crítica A: ¿Solo seleccioné el objeto que voy a cambiar?
- Pregunta crítica B: ¿Se ha borrado alguna otra parte de toda la toma?
- Usa el filtro *White Mask* (Máscara blanca) para detectar píxeles perdidos o ruido sin seleccionar en medio del objeto.

## 4. Generación y Selección de la Variante Perfecta
El prompt directo de transformación ya estará indicado (Ej: "Remover el patrón a base de Halloween e incrustar calabazas").
1. Ejecutar las 4 iteraciones del Prompt Directo (Forward).
2. Analizar detenidamente cada una.
3. La elegida DEBE SER PERFECTA: Transición fluida, sin pedazos de textura del objeto original, y que encaje maravillosamente en los bordillos.
4. Si todas las variantes son horribles y la IA arruina sistemáticamente la imagen, usa `Skip This Entry` (opción "All generated results are bad").

## Cuándo usar SKIP (Saltar Tarea)
- La textura/patrón base no era repetitiva o regular ("Not a repeating tile").
- Imposible hacer máscara por aberración técnica.
- Resultados generados malísimos.
- La imagen es muy pequeña o comprimida (resolución pobre).
