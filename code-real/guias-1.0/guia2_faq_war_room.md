# 📋 Guía 2 — FAQ War Room (Sesión de Preguntas y Respuestas)
> **Traducción oficial al español** | Fuente: `g2instructions` | Fecha original: 28/03/2026
>
> Esta guía es un resumen de las respuestas oficiales del equipo a las preguntas más frecuentes de los contribuidores. Complementa y en algunos puntos clarifica la Guía 1.
>
> ⚠️ **Diferencias con tu proyecto actual** están marcadas con `[⚡ DIFERENTE]`

---

## ❓ Bloque 1: Preguntas sobre el Script de Validación y Entregables

**P1: ¿Está bien cambiar la ruta principal de la app en el script de verificación para que funcione?**

✅ Sí, pero solo esa línea puede cambiarse, no el resto del script.

---

**P2: ¿Qué debemos hacer con la salida del script de verificación?**

Si tienes una tarea de taxonomía antigua:
- Por ahora, simplemente copia y pega el `before.json` y `after.json`.
- La taxonomía se actualizará más adelante para que puedas re-enviarlos como archivos adjuntos.

---

**P3: Cobertura — En el documento QC Spec hay dos dimensiones de cobertura. ¿Cuál es la más actualizada?**

Las dos dimensiones mencionadas en el QC Spec son:

**a) Cobertura del Verificador:** Las pruebas (si existen) y los criterios de rúbrica, considerados juntos, deben verificar todas las solicitudes del prompt reescrito.

**b) Cobertura de Rúbricas:** TODOS los requisitos explícitos del query de la tarea deben estar cubiertos por rúbricas.

**Respuesta oficial:**
- Algunos requisitos son cubribles por pruebas unitarias, otros por rúbricas. Pueden superponerse, pero ninguno debe perderse.
- Usar pruebas unitarias para cubrir todos los requisitos del backend.
- Usar rúbricas para cubrir todos los requisitos del frontend + cosas que no pueden cubrirse por pruebas unitarias.
  - Puedes escribir pruebas unitarias de frontend también, pero las rúbricas deben cubrir CUALQUIER COSA que las pruebas unitarias no puedan verificar.
- La Expected Interface también debe testearse.
- No quieres que una solución falle por nombres de archivo diferentes cuando no se especifican en el prompt — ¡no seas excesivamente específico en pruebas unitarias a menos que sea necesario!

---

**P4: Prueba F2P — Aclaración sobre cómo se ejecuta la suite de pruebas:**

El equipo ejecutará la suite completa de pruebas contra una base de código vacía y obtendrá todos FAIL. Luego ejecutará la misma suite de pruebas sobre el Golden Patch para asegurarse de que todos obtienen PASS.

> ⚠️ **IMPORTANTE:** Asegúrate de que las pruebas = FAIL en lugar de crashear el programa.

---

**P5: ¿Cómo se deben crear las rúbricas y para qué proceso/resultados deben crearse? ¿Las rúbricas deben basarse en el prompt reescrito del CB y cubrir cada requisito explícito?**

✅ Sí, las rúbricas deben basarse en el prompt reescrito del CB y cubrir cada requisito explícito del prompt.

---

## ❓ Bloque 2: Preguntas sobre Docker y Herramientas

**P6: ¿Podemos cambiar el Dockerfile?**

✅ ¡Se puede agregar dependencia adicional si es necesario!

---

**P7: ¿Hay que usar WSL o Docker es suficiente?**

WSL facilita construir imágenes y ejecutar Docker en Windows. También puedes usar PowerShell o git bash. Puedes revisar las instrucciones sobre cómo configurar Docker en Windows.

---

**P8: ¿Debemos crear casos de prueba para frontend y backend?**

- **Backend:** Es el requisito base (obligatorio).
- **Frontend:** No requiere pruebas unitarias. Usar rúbricas en su lugar.

---

**P9: ¿Qué frameworks están permitidos? (ej. Next.js, Nuxt, React, Flask, Django)**

- Cualquier framework detallado en el prompt.
- Si el prompt no tiene detalles sobre el stack tecnológico, elegir tu stack favorito siempre que resuelva el problema.

---

**P10: ¿Qué modelo usar en Cursor al hacer tareas y qué modo usar?**

- Cualquier modelo, cualquier agente.
- Puede que sea mejor usar Claude 4.6.

---

## ❓ Bloque 3: Preguntas sobre Rúbricas y Cobertura

**P11: ¿Cuál es el criterio necesario para escribir rúbricas de criterios que ya están cubiertos en los casos de prueba?**

✅ Sí puedes incluirlos, pero eso será raro.

---

**P12: ¿Estamos limitados al stack tecnológico mencionado en la tarea o podemos usar otros?**

- Sí, debes intentar seguir el stack tecnológico especificado en el prompt.
- Pero si el prompt no tiene detalles sobre el stack tecnológico, elegir tu stack favorito siempre que resuelva el problema.

---

**P13: ¿El prompt reescrito tiene que ser completamente cerrado (close-ended)?**

✅ Sí.

---

**P14: ¿Hay fallos relacionados con:**
- ¿uso de iconos con copyright?
- ¿alguna API no permitida?
- ¿contenido no permitido?
- ¿alguna librería explícitamente no permitida?

**Respuesta:** Debe evitarse cualquier cosa que requiera configuración, como claves de API, etc. Las entradas de imágenes también son desafiantes, así que es mejor evitarlas.

---

**P15: ¿Hay fallos relacionados con clonar una UI o diseño de sitio web?**

No deberías tener esas tareas. Si las encuentras, reportarlas al equipo PT.

---

**P16: ¿Podemos escribir presupuestos o cronogramas aleatorios si no se mencionan en la descripción de la tarea?**

❌ No. El presupuesto o cronograma no son parte de la descripción de la tarea ni del prompt reescrito. Son solo metadatos, y solo deben incluirse cuando estén disponibles (es decir, cuando vengan de un sitio web freelance real).

---

**P17: ¿Hay fallos relacionados con UX?**

Si los requisitos del prompt se satisfacen técnicamente, pero la experiencia del usuario podría mejorarse o es mala, esto no debería causar automáticamente un fallo. En cambio, la calidad de UX debe evaluarse a través de las rúbricas.

---

## ❓ Bloque 4: Preguntas sobre Casos de Prueba

**P18: ¿Cómo se implementarán los casos de prueba cuando existan tanto pruebas específicas de la tarea como pruebas F2P?**

**Escenario de ejemplo:**
- La descripción de la tarea requiere 5 casos de prueba específicos.
- El proceso F2P resulta en 80 casos de prueba totales.

**Respuesta:** Pruebas unitarias para backend, rúbricas para frontend/cualquier cosa que las pruebas unitarias no puedan capturar. No es necesario separar en carpetas diferentes — van todas en la misma carpeta `/tests`.

---

**P19: Si el prompt especifica 5-10 casos de prueba pero una vez construida la solución se sienten necesarios más, ¿pueden añadir nuevos casos de prueba sin mencionarlos en el prompt?**

✅ Los casos de prueba y rúbricas no deben incluirse en el prompt reescrito. No son parte de los requisitos del prompt. En cambio, sirven como mecanismos de evaluación externos usados para verificar la integridad y corrección de la respuesta del modelo.

---

**P20: ¿Pueden agruparse múltiples requisitos similares en una rúbrica?**

**Ejemplo:**
> "La solución usa el stack especificado (Vue 3, Vite, Pinia, Express, SQLite, Sequelize, Vitest, Supertest)."

**Respuesta:**
- Para requisitos generales como el stack tecnológico, este tipo de agrupación es aceptable.
- Para requisitos no generales o características específicas, intentar separarlos en criterios individuales siempre que sea posible.

**Dimensiones de la rúbrica a consultar en el documento QC:**
- Atomicidad
- Autocontenida
- Precisión
- Superposición / Redundancia
- Etiquetas / Anotaciones
- Criterio Objetivamente Incorrecto
- Criterios Contraproducentes
- Criterios Irrelevantes

---

## 📌 Resumen Rápido de las Reglas Clave Confirmadas en el War Room

| Tema | Regla Confirmada |
|---|---|
| Script de validación | Solo editar la línea de la ruta del app path |
| Pruebas F2P | Las pruebas deben FAIL (no crashear) con base de código vacía |
| Rúbricas | Basadas en el prompt reescrito; cubrir TODOS los requisitos explícitos |
| Docker | Se pueden agregar dependencias adicionales |
| Coverage | Backend → pruebas unitarias; Frontend → rúbricas |
| Stack tecnológico | Seguir el del prompt; si no especifica, elegir libremente |
| Prompt cerrado | Sí, debe ser completamente close-ended (determinista) |
| Imágenes/APIs externas | Evitar cualquier cosa que requiera setup externo |
| Presupuesto/cronograma | No incluir si no viene del brief del cliente real |
| UX pobre | No falla automáticamente; evaluarlo en rúbricas |
| Modelo en Cursor | Cualquier modelo; se recomienda Claude 4.6 |
| Agrupación en rúbricas | OK para stack general; separar para características específicas |

---

> 📌 **Nota:** Esta guía es el complemento de Q&A de la Guía 1. Refleja las aclaraciones directas del equipo PT/QM en sesiones de War Room. Fecha de la sesión: 28/03/2026.
