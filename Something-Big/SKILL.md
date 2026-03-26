---
name: task-big
description: "Asistente y auditor para el proyecto 'Something Big' de Outlier. Contiene las reglas estructurales para rúbricas, evaluación de código agnóstico y el flujo de Docker en VPS. Depende del skill container-env-manager para infraestructura."
---

# Skill: Task Big (Proyecto "Something Big" - Outlier)

Esta skill está diseñada para guiar, auditar y estructurar el trabajo en el proyecto "Something Big" de Outlier, integrando las mejores prácticas para evaluación de IA, diseño de prompts, creación de rúbricas agnósticas a la implementación y el uso del VPS como entorno local.

---

## 🔗 Regla 0 — Dependencia de Infraestructura (OBLIGATORIA)

> **Cada vez que se inicie una evaluación para el proyecto Something Big, este skill DEBE apoyarse obligatoriamente en el skill `container-env-manager` para manejar toda la conexión al VPS y la ejecución de Docker.**

### Secuencia de Activación Automática:

```
🔗 INFRASTRUCTURE DEPENDENCY — AUTOMATIC

Cuando task-big necesite ejecutar código en Docker:
  1. Invocar container-env-manager → Rule 1 (SSH Health Check)
  2. Invocar container-env-manager → Rule 2 (Docker Daemon Verification)
  3. Solo después → Proceder con las fases de task-big (5.1 → 5.4)

Skill de infraestructura: container-env-manager
  Ubicación: .agent/skills/container-env-manager/SKILL.md
  Script SSH: .agent/skills/container-env-manager/scripts/ssh-remote-runtime.md
```

### ¿Por qué esta regla?
- Todo lo que sea "conectar al servidor y Docker" vive en `container-env-manager`.
- Todo lo que sea "evaluar, rúbricas y prompts de Outlier" vive aquí en `task-big`.
- Principal de DRY (Don't Repeat Yourself): la conexión SSH y Docker se mantiene en un solo lugar.
- Si mañana se cambia de VPS, solo se actualiza `container-env-manager`, no todos los skills.

---

## 1. El Principio Fundamental: Enfoque "Agnóstico" (Implementation-Agnostic)

*   **QUÉ y no CÓMO:** Toda instrucción, diseño de pruebas y evaluación debe enfocarse exclusivamente en el comportamiento público de las interfaces (entradas y salidas). 
*   **Prohibido Dictar el "CÓMO":** Jamás obligues al modelo a usar un ciclo específico, diccionarios internos, o nombres de variables ocultas.
*   **Pruebas de Caja Negra (Black-Box):** La cobertura total debe lograrse mediante pruebas unitarias que evalúen la superficie externa. No se permite testear métodos privados. Comprobar el manejo de errores (ej. `ValueError`) es válido, ya que es un estado observable del sistema.

---

## 2. Estructura Obligatoria de un Prompt de Alta Calidad

Todo prompt debe simular una solicitud humana real, ser natural y específico, evitando restricciones absurdas ("ingeniería para el fallo"). Deben incluirse 4 secciones:

1.  **Objetivo (The Objective):** Meta principal de alto nivel.
2.  **Estrategia (The Strategy):** El enfoque técnico específico (ej. "usar una arquitectura modular").
3.  **Restricciones (The Constraints):** Requisitos técnicos obligatorios (seguridad, tecnologías).
4.  **Interfaz Esperada (Expected Interface):** La parte crítica e innegociable. Por cada archivo, clase o función a crear, especificar de manera agnóstica:
    *   **Path:** Ruta exacta del archivo.
    *   **Name:** Nombre de la clase o función.
    *   **Type:** Tipo (clase, método, función).
    *   **Input:** Parámetros y sus tipos.
    *   **Output:** Tipo de retorno.
    *   **Description:** Qué hace la interfaz.

### Checklist de Calidad del Prompt:
```
Antes de enviar el prompt, verificar:

  [ ] No se mencionan nombres de variables internas
  [ ] No se describen pasos algorítmicos específicos ("usa un loop", "usa recursión")
  [ ] Cada componente tiene los 6 campos del schema de interfaz
  [ ] Todas las restricciones son conceptuales, no a nivel de implementación
  [ ] El inglés es de nivel nativo (cero errores gramaticales)
  [ ] Los patrones de diseño solo se mencionan si el prompt los exige
```

---

## 3. Rúbricas de Evaluación (Mínimo 10 Criterios)

Las rúbricas son la "receta dorada" de calificación. Nunca se formulan basadas en el "golden patch", sino en los requerimientos del prompt.

### Propiedades del Criterio:
*   **Autocontenidos:** Comprensibles sin leer el prompt externo.
*   **Atómicos:** Evalúan un solo aspecto.
*   **Objetivos:** Verificables de forma objetiva (pasa/no pasa).
*   **Explícitos:** Sin lenguaje vago ("buen código", "legible").
*   **No redundantes:** No repiten la misma evaluación entre criterios.
*   **Positivos:** Dicen qué DEBE incluir el código, no qué evitar.

### Pesos Permitidos:
| Peso | Significado | Criterio |
|---|---|---|
| **5** | Mandatorio / Crucial | Requisitos que deben cumplirse sin excepción |
| **3** | Importante | Atributos de alta relevancia para la calidad general |
| **1** | Deseable | Características adicionales que aportan valor pero no son obligatorias |

> 🚨 **Pesos PROHIBIDOS:** 2 y 4 — NUNCA usar estos valores.

### Las 5 Dimensiones a Evaluar:
1.  **Instruction Following** — Seguimiento de instrucciones
2.  **Code Correctness** — Corrección del código
3.  **Code Quality** — Calidad del código, diseño, seguridad y mantenimiento
4.  **Code Clarity** — Claridad, formato descriptivo y legibilidad
5.  **Code Efficiency** — Rendimiento algorítmico apropiado, evitar mala Big-O

### Template de Rúbrica:
```
| # | Criterio | Categoría | Peso | Cómo Verificar |
|---|---|---|---|---|
| 1  | [afirmación específica y positiva] | Instruction Following | 5 | [verificación objetiva] |
| 2  | [afirmación específica y positiva] | Code Correctness      | 5 | [verificación objetiva] |
| 3  | [afirmación específica y positiva] | Code Quality          | 3 | [verificación objetiva] |
...
| 10 | [afirmación específica y positiva] | [categoría]           | 1 | [verificación objetiva] |
```

---

## 4. Protocolo de Tests y Golden Loop

### Tipos de Protocolo de Tests:

| Protocolo | Acrónimo | Propósito | Comportamiento Esperado |
|---|---|---|---|
| **Pass-to-Pass** | P2P | Tests de regresión | El código del Estado 1 (antes del parche) DEBE pasar estos |
| **Fail-to-Pass** | F2P | Tests funcionales | DEBEN fallar en Estado 1, DEBEN pasar en Estado 2 (después del parche) |

### El Golden Loop (Ciclo Obligatorio):

```
🔁 GOLDEN LOOP — CICLO DE VALIDACIÓN DEL PARCHE

Paso 1: Escribir Tests
  → Crear scripts de test F2P y P2P basados en el prompt de ingeniería
  → Los tests deben ser independientes de detalles de implementación

Paso 2: Ejecutar Tests Contra el Golden Patch
  → Usar container-env-manager para conexión SSH + Docker
  → Esperado: F2P tests FALLAN en Estado 1, PASAN en Estado 2

Paso 3: Iterar / Reescribir
  → Si el Golden Patch NO pasa los tests F2P: reescribir el parche o los tests
  → Si los tests P2P fallan: corregir regresión en el test suite
  → Repetir hasta que TODOS los tests pasen

Paso 4: Entregar
  → Generar output.json cuando todos los tests pasen

✅ Loop completo cuando: Todos F2P pasan en Estado 2, Todos P2P pasan en Estado 1
```

---

## 5. Entregables Finales

### Archivos Requeridos:

| Archivo | Propósito |
|---|---|
| `run_script.sh` | Configura el entorno y ejecuta tests dentro de Docker |
| `parsing.py` | Convierte logs de test a formato JSON estandarizado |
| `output.json` | Archivo de resultados finales generado al correr el Golden Patch |

### Categorización de Complejidad:

| Nivel | Criterio |
|---|---|
| **Medium** | < 50 líneas cambiadas, lógica directa, uso de librería estándar |
| **High** | 50–150 líneas cambiadas, algoritmos no triviales, múltiples dependencias |
| **Expert** | > 150 líneas cambiadas, arquitectura compleja, algoritmos avanzados |

### Template de Justificación de Complejidad:
```
📋 REPORTE DE COMPLEJIDAD

  Categoría:    [Medium | High | Expert]

  Justificación:
    - Líneas cambiadas:       [N líneas en M archivos]
    - Profundidad conceptual: [descripción breve de la lógica más difícil]
    - Dependencias:           [lista de librerías o sistemas externos]
    - Edge cases:             [N edge cases que requieren manejo específico]

  Clasificación final: [MEDIUM | HIGH | EXPERT]
```

---

## 6. Auditoría Final (Quality Control)

Antes de entregar un trabajo, el evaluador/la IA debe certificar que:

*   ✅ Cumple todos los puntos del prompt fielmente.
*   ✅ El código tiene buen diseño, rendimiento, legibilidad y seguridad sin fallos catastróficos.
*   ✅ Los tests son F2P estrictos y agnósticos (sin tests irrelevantes para aumentar cobertura).
*   ✅ **Fluidez Nativa (Ortografía/Gramática):** Cero tolerancia. 4+ errores menores causan fallo. 2 errores graves "Egregious" causan reprobación automática.
*   ✅ **Complejidad Justificada:** Al clasificar la tarea, justificar con arquitectura por qué recae en Nivel Medio, Alto o Experto.
*   ✅ **IA de Terceros Prohibida:** Todo análisis NO utilizará salidas que parezcan autogeneradas por ChatGPT. La salida generada debe poseer criterio experto propio.

### Checklist de Entrega Final:
```
✅ CHECKLIST DE ENTREGABLES

  [ ] run_script.sh    — Revisado y ejecutable (chmod +x)
  [ ] parsing.py       — Produce JSON válido (validado con python3 parsing.py)
  [ ] output.json      — Generado al correr Golden Patch (no escrito a mano)
  [ ] Prompt           — Agnóstico, todos los esquemas completos, inglés nativo
  [ ] Rúbrica          — ≥ 10 criterios, pesos 1/3/5 solamente, 5 dimensiones cubiertas
  [ ] Complejidad      — Justificada con líneas, profundidad y dependencias

⚠️ RECORDATORIO DE SEGURIDAD:
  NUNCA copiar-pegar texto generado por IA directamente en la plataforma Outlier.
  Leer → Entender → Escribir con tus propias palabras en la plataforma.
```

---

**Nota al Asistente:** Al ser invocado bajo esta skill, actúa como Evaluador y Creador (Task Big). Analiza diffs, diseña prompts y redacta rúbricas ciñéndote ciegamente a estas directivas sin apartarte del enfoque Implementation-Agnostic. Para TODA operación de Docker/VPS, delega al skill `container-env-manager`.
