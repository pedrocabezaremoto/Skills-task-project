# 📊 Rubric Template — Plantilla de Rúbricas para Real Coder

> **Uso:** Crear rúbricas de evaluación experta alineadas con los estándares del proyecto.
> Ref: G1 §Paso 3, G2 §4, G3 §Paso 5/§4, G6 §3, G8 §5, G9 §4.3

---

## 1. Las 5 Dimensiones de Evaluación (G3 §2)

Cada rúbrica **DEBE** cubrir estas dimensiones. El puntaje final se rige por la **Regla de la Dimensión Más Baja** (G9 §5): si una dimensión es 2, el total es 2.

| # | Dimensión | Descripción | Evalúa |
|---|---|---|---|
| 1 | **Seguimiento de Instrucciones** | ¿El código cumple lo que el prompt pidió? | Completitud, fidelidad al brief |
| 2 | **Corrección del Código** | ¿El código funciona sin errores? | Compilación, runtime, lógica |
| 3 | **Calidad del Código** | ¿El código es profesional? | Modularidad, abstracción, naming |
| 4 | **Claridad** | ¿El código es legible? | Comentarios, documentación, estructura |
| 5 | **Eficiencia** | ¿El código es óptimo? | Complejidad algorítmica, recursos |

---

## 2. Escala de Pesos Permitidos (G1 §Paso 3, G8 §5)

> ⚠️ **SOLO** se permiten estos 3 valores. Usar 2 o 4 es un FALLO.

| Peso | Significado | Criterio de Uso |
|---|---|---|
| **5** | **Mandatorio** | No se puede imaginar una respuesta aceptable sin este elemento |
| **3** | **Importante** | La respuesta es sustancialmente mejor con este elemento |
| **1** | **Deseable** | "Nice to have" — Mejora la calidad pero no es esencial |

---

## 3. Reglas de Calidad de Criterios (G2 §4, G3 §4)

### 3.1 Requisitos de Cada Criterio

| Propiedad | Requisito | Ejemplo Correcto ✅ | Ejemplo Incorrecto ❌ |
|---|---|---|---|
| **Atomicidad** | Evalúa UN solo concepto | "El endpoint /api/users retorna 200 OK" | "El endpoint retorna 200 OK y usa validación y tiene logging" |
| **Autonomía** | Autocontenido, sin contexto externo | "El mensaje de error incluye el nombre del archivo" | "Implementa según las instrucciones del prompt" |
| **Precisión** | Exacto y verificable en el código | "Usa bcrypt para hashing de contraseñas" | "Usa un algoritmo de hashing apropiado" |
| **No Redundante** | Sin superposición con otros criterios | Cada criterio valida algo único | Dos criterios que evalúan "el formulario funciona" |
| **Objetividad** | Sin términos vagos | "El componente usa CSS Grid para layout" | "El diseño es limpio y apropiado" |
| **Encuadre Positivo** | Respuesta correcta = "Sí/Verdadero" | "¿Usa React Hooks en vez de clases?" | "¿No usa componentes de clase?" |

### 3.2 Umbrales de Error en la Rúbrica (G3 §4)

| Categoría | Umbral de Fallo (1-2) |
|---|---|
| **Errores Mayores** | > 5% de los criterios tienen problemas graves |
| **Errores Moderados** | > 15% de los criterios tienen problemas moderados+ |
| **Errores Menores** | > 25% de los criterios tienen problemas menores+ |

### 3.3 Clasificación de Problemas

**🔴 Problemas Mayores:**
- Falta de autocontención (requiere consultar prompt externo)
- No atómico (agrupa restricciones no relacionadas)
- Criterio factualmente incorrecto
- Encuadre negativo

**🟡 Problemas Moderados:**
- **Sobreajuste (Overfitting):** Criterios que rechazan implementaciones válidas
- **Subajuste (Underfitting):** Criterios que aceptan soluciones inválidas
- **Subjetividad:** Términos como "apropiado", "mejores prácticas" sin definición
- **Redundancia:** Criterios que evalúan lo mismo

**🟢 Problemas Menores:**
- Redacción mejorable pero funcional
- Etiquetado/anotaciones inconsistentes

---

## 4. Plantilla de Criterio Individual

```markdown
### Criterio [N]: [Título descriptivo]

- **Dimensión:** [Instrucciones | Corrección | Calidad | Claridad | Eficiencia]
- **Peso:** [1 | 3 | 5]
- **Criterio:** [Pregunta cerrada que se responde Sí/No]
- **Verificación:** [Cómo verificar en el código — selectores, funciones, archivos]

Ejemplo:
  Sí → El criterio se cumple (puntaje completo)
  No → El criterio no se cumple (0 puntos)
```

---

## 5. Ejemplo de Rúbrica Completa (Mínimo 5 criterios — G3 §1)

> Para una tarea: "Construir una calculadora web con React"

| # | Dimensión | Peso | Criterio |
|---|---|---|---|
| 1 | Instrucciones | 5 | ¿La aplicación usa React como framework principal (verificar package.json)? |
| 2 | Corrección | 5 | ¿Las operaciones +, -, *, / producen resultados matemáticamente correctos? |
| 3 | Corrección | 3 | ¿La división por cero muestra un mensaje de error en vez de NaN/Infinity? |
| 4 | Calidad | 3 | ¿Los componentes están separados en archivos individuales (no todo en App.js)? |
| 5 | Claridad | 1 | ¿Las funciones de cálculo tienen nombres descriptivos (no `calc1`, `doStuff`)? |
| 6 | Eficiencia | 3 | ¿El estado de la calculadora usa `useState` hooks (no re-renderiza todo el DOM)? |
| 7 | Instrucciones | 5 | ¿La UI tiene un display visible que muestra el número actual y el resultado? |
| 8 | Calidad | 3 | ¿El CSS usa Flexbox o Grid para layout responsivo (no posiciones absolutas)? |
| 9 | Corrección | 3 | ¿Las operaciones encadenadas (2+3*4) respetan la precedencia matemática? |
| 10 | Claridad | 1 | ¿El componente principal tiene al menos un comentario explicando su función? |

---

## 6. Reglas de Agrupación (G2 §4)

- ✅ **Permitido agrupar** requisitos generales de tecnología:
  - "¿La aplicación usa Vue 3 + Vite + Express como stack tecnológico?"
- ❌ **Prohibido agrupar** funcionalidades específicas:
  - "¿El formulario valida email Y tiene CAPTCHA Y envía notificaciones?"

---

## 7. Cobertura Obligatoria (G2 §2, G8 §5)

```
┌───────────────────────────────────────────────────────┐
│  Pruebas Unitarias + Rúbricas = 100% de cobertura    │
│                                                       │
│  Backend → Pruebas unitarias (prioridad)              │
│  Frontend → Rúbricas (método principal)               │
│  UX/Diseño → Rúbricas únicamente                      │
│  Solapamiento → Aceptable                             │
│  Gaps → PROHIBIDOS (fallo crítico)                    │
└───────────────────────────────────────────────────────┘
```

> **Regla G9 §4.4:** Realizar un cruce programático entre prompt, pruebas y rúbricas para verificar que NO existan "requisitos huérfanos".
