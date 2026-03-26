# Workflow: Edición de Imágenes y Generación de Prompts Inversos

**Objetivo:** Elaborar datasets de edición de imagen de altísima calidad en `multimango.com`. Se compone del enmascaramiento de objetos en imágenes únicas, la generación guiada de IA (Forward Prompt), selección rigurosa, y el diseño de un Reverse Prompt maestro para volver al origen en otra iteración ciega. No usar IA.

## Paso 1: Búsqueda y Selección (URL Input)
Seleccionar imágenes con sujetos destacables, limpios, no absurdamente abstractos, y sin baja resolución compresiva ni marcas de agua detectables.
**ALERTA DE DUPLICADOS:** La política es cero tolerancia al reciclaje.
- No re-hostear la imagen.
- No aplicar zoom y reenviar la URL en otro ciclo.
- No hacer un re-phrase estúpido de prompt ("remueve" por "borra") y volver a usarla.

## Paso 2: Creación de Máscara y Prompt Directo
1. Enmascarar con la herramienta cepillo el sujeto objetivo.
2. Inyectar o borrar el sujeto con el **Forward Prompt (Prompt Directo):** *"Reemplazar al muchacho corriendo por una estatua románica blanca."*
> **Nota de Sombras:** La máscara DEBE incluir la sombra original del muchacho y/o su reflejo para ser editados lógicamente, o la estatua quedará sobre una sombra inexistente.

## Paso 3: Aceptación de la Variante (Seleccionando calidad IA)
Dos variantes de render. Inspecciona mediante flip o lupa:
- Solo pudo haber modificado los píxeles DENTRO del espectro del pincel. Si la IA distorsionó hojas de árbol fuera o se destiñó medio cielo lejano al original: **Recházalo**.
- Realismo orgánico. No deformidades plásticas.

## Paso 4: Redacción del "Prompts Inversos" (Reverse Prompt)
Este es el pilar central del éxito del ticket. Una orden a una IA asumiendo que tu imagen recién aceptada es en realidad el origen, y quieres transformarla hacia un resultado "ideal" (Que paradójicamente, es tu imagen cruda real de paso 1).

### Reglas para Reverse Prompts de Calidad:
1. **La dirección es: Generada a Origen.**
2. **No romper la cuarta pared:** Prohibido decir *Restaurar original*, *Quitar lo borrado*, *Deshacer el filtro*, etc.
3. No hacer omisiones fatales o generalizaciones: *"Borra la estatua y pon a un tipo."*. Tienes que detallar todo porque la IA no conoce al tipo.
4. **Incluir contexto residual:** Múltiples aspectos ambientales deben atarse juntos (sombra, destello solar en cristales reemplazados, humedad del asfalto inferior).

### Tabla de Comparación Práctica
| Tipo | Prompt Directo (Lo que hizo la IA) | Prompt Inverso Excelente (Para volver a empezar) |
|---|---|---|
| Cambio Clima | "Añadir un atardecer al cielo." | "Eliminar los colores cálidos del atardecer del cielo y reemplazarlos por un cielo gris nublado. Ajustar la iluminación del suelo para que sea más fría y difusa." |
| Insertar | "Eliminar y reemplazar la persona sentada por una bicicleta." | "Retirar la bicicleta estacionada en la calle y sustituirla por un sujeto joven sentado mirando a la izquierda, vestido con franela amarilla, proyectando una sombra hacia la derecha bajo él." |
