# G4 — Guía Completa de Rúbricas (Rubric Guidelines)

> Cómo crear rúbricas profesionales para tareas de Refactoring/Maintainability (R/M).

---

## 1. Requisitos Generales de la Rúbrica

- **Cantidad:** Mínimo **15**, máximo **20** criterios
- **Cobertura:** Debe cubrir TODO lo que pide el prompt y que NO verifican ya los scripts
- **Agnóstica:** Debe evaluar CUALQUIER solución correcta, no solo el Golden Patch
- ⚠️ Las rúbricas generadas por LLM son un **punto de partida** que DEBE editarse exhaustivamente

---

## 2. Requisitos de cada Criterio

| Propiedad | Regla |
|-----------|-------|
| **Rubric-Specific** | No verificar lo que ya verifican `run_script` o `reproduction_script` |
| **Atomic** | 1 criterio = 1 sola idea. No mezclar conceptos |
| **Objective** | PASS o FAIL sin ambigüedad subjetiva |
| **Correctly Framed** | Respuesta buena = "Yes" / "True" = PASS |
| **Positive** | "Code includes..." ✅ | "Code doesn't forget..." ❌ |
| **Accurate** | Coincidir exactamente con lo que pide el prompt |
| **Scoped** | Solo evaluar lo que está pedido explícita o implícitamente en el prompt |
| **Self-Contained** | Evaluable solo con el criterio + el diff de la respuesta. Sin necesidad de leer el prompt, PR, scripts, u otro material externo |
| **Unique** | Sin redundancia entre criterios |
| **Not Over/Underfitting** | Ni tan específico que rechace soluciones válidas, ni tan genérico que acepte basura |

---

## 3. Pesos Permitidos

| Peso | Significado | Cuándo Usarlo |
|------|-------------|---------------|
| **5** | **Mandatory** | Requisito central del prompt. Imposible aceptar respuesta sin esto |
| **3** | **Important** | Mejora sustancial. Implícitamente esperado por el prompt |
| **1** | **Nice to have** | Necesario para respuesta perfecta, no crítico |

> ⚠️ **PROHIBIDO ABSOLUTAMENTE** usar pesos `2` o `4`. Solo: `1`, `3`, `5`.

---

## 4. Reglas de Formateo

| ❌ Prohibido | ✅ Correcto |
|-------------|------------|
| Tiempo pasado ("The code implemented...") | Presente ("The code implements...") |
| Preguntas ("Does the code...?") | Afirmaciones ("The code includes...") |
| Empezar con "The model..." | Empezar con "The code/solution/implementation..." |

---

## 5. Sistema de Scoring

| Resultado | Significado |
|-----------|-------------|
| **PASS** | Criterio completamente cumplido |
| **FAIL** | Criterio no cumplido |

> **Regla de Oro:** El Golden Patch DEBE tener **TODOS** los criterios en **PASS**.

---

## 6. Categorías de Criterios

| Categoría | Qué Evalúa |
|-----------|------------|
| **Instruction Following** | Adherencia a instrucciones explícitas: formato, constraints, lenguaje, librerías |
| **Code Correctness** | El código realiza la tarea correcta y produce resultados correctos |
| **Code Clarity** | Legibilidad, nombres descriptivos, estructura organizada, formateo |
| **Efficiency** | Concisión, sin pasos innecesarios, sin redundancia |
| **Risk Security** | Seguridad, sin contenido inapropiado o dañino |

---

## 7. Ejemplo de Criterio Bien Escrito vs. Mal Escrito

### ❌ MAL (viola múltiples reglas)
> "Did the model correctly implement the sorting logic on the input array?" 
> - Usa pregunta, "the model", no es self-contained

### ✅ BIEN (cumple todas las reglas)
> "The solution implements merge sorting logic on the array that is received as input in the `sort_data` function located in `src/utils/sorter.py`."
> - Afirmativo, positivo, self-contained, atómico, scoped

---

## 8. Checklist Pre-Entrega de Rúbrica

- [ ] Tiene entre 15 y 20 criterios
- [ ] Todos los criterios generados por LLM fueron editados manualmente
- [ ] Cada criterio es atómico (1 idea)
- [ ] Cada criterio es self-contained (se entiende sin leer el prompt)
- [ ] No evalúa cosas que ya verifican los scripts
- [ ] Solo usa pesos 1, 3, o 5 (NUNCA 2 o 4)
- [ ] Escrito en presente, afirmativo, sin "The model..."
- [ ] El Golden Patch pasa TODOS los criterios con PASS
- [ ] No tiene criterios redundantes
- [ ] Evalúa cualquier solución correcta, no solo el Golden Patch
