# Guía G2: Diseño de Rúbricas — Something Big

## Propiedades del Criterio:
*   **Autocontenidos:** Comprensibles sin leer el prompt externo.
*   **Atómicos:** Evalúan un solo aspecto.
*   **Objetivos:** Verificables de forma objetiva (pasa/no pasa).
*   **Explícitos:** Sin lenguaje vago ("buen código", "legible").
*   **No redundantes:** No repiten la misma evaluación entre criterios.
*   **Positivos:** Dicen qué DEBE incluir el código, no qué evitar.

## Pesos Permitidos:
| Peso | Significado | Criterio |
|---|---|---|
| **5** | Mandatorio / Crucial | Requisitos que deben cumplirse sin excepción |
| **3** | Importante | Atributos de alta relevancia para la calidad general |
| **1** | Deseable | Características adicionales que aportan valor pero no son obligatorias |

> 🚨 **Pesos PROHIBIDOS:** 2 y 4 — NUNCA usar estos valores.

## Las 5 Dimensiones a Evaluar:
1.  **Instruction Following** — Seguimiento de instrucciones
2.  **Code Correctness** — Corrección del código
3.  **Code Quality** — Calidad del código, diseño, seguridad y mantenimiento
4.  **Code Clarity** — Claridad, formato descriptivo y legibilidad
5.  **Code Efficiency** — Rendimiento algorítmico apropiado, evitar mala Big-O

## Template de Rúbrica:
```text
| # | Criterio | Categoría | Peso | Cómo Verificar |
|---|---|---|---|---|
| 1  | [afirmación específica y positiva] | Instruction Following | 5 | [verificación objetiva] |
| 2  | [afirmación específica y positiva] | Code Correctness      | 5 | [verificación objetiva] |
| 3  | [afirmación específica y positiva] | Code Quality          | 3 | [verificación objetiva] |
...
| 10 | [afirmación específica y positiva] | [categoría]           | 1 | [verificación objetiva] |
```

---
*Contexto Onboarding:*
- **Rúbricas:** Se consideran válidas si evalúan comportamiento público observable descrito en el prompt (ej: validación de longitud de string), incluso si mencionan el método público (ej: `__call__`).
- **Golden Patch DEBE pasar todos los criterios con PASS.** (Página 10 del Onboarding).
