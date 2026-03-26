# Módulo 6: Estándares de Rúbricas — Creación y Evaluación (Onboarding)

> **Documento de Entrenamiento (training1)**
> Basado en: *Directrices de creación de rúbricas del Real Coder Intro Course (Página 12) y casos QC reales (Páginas 15-19).*

---

## 📌 Propósito de este Módulo

Este módulo define los **estándares obligatorios** para la creación de rúbricas de evaluación en tareas Real Coder. Las rúbricas complementan los tests F2P cubriendo aspectos que la automatización no puede verificar: calidad subjetiva, mantenibilidad, y adherencia a buenas prácticas.

**Principio rector:** Las rúbricas evalúan lo que los tests no pueden. Si un test F2P ya verifica algo, la rúbrica no debe duplicarlo.

---

## 📐 Las 5 Dimensiones Obligatorias

Toda rúbrica debe organizar sus criterios en exactamente estas **5 categorías**:

### 1. Instruction Following (Cumplimiento de Instrucciones)
- Verifica que el código respeta las restricciones explícitas del prompt.
- **Ejemplos:** Usar la librería especificada, respetar formato JSON pedido, usar el lenguaje indicado.
- **Error común:** Categorizar aquí algo que pertenece a Code Correctness.

### 2. Code Correctness (Corrección del Código)
- Verifica que el código realiza la tarea correctamente y produce resultados esperados.
- **Ejemplos:** Lógica de negocio correcta, manejo de edge cases, outputs correctos.
- **Diferencia con Instruction Following:** IF verifica "¿usó lo que se pidió?". CC verifica "¿funciona bien?".

### 3. Code Quality (Calidad del Código)
- Evalúa robustez y mantenibilidad.
- **Ejemplos:** Manejo de errores, evitar código frágil, uso de patrones estables.
- **Foco:** ¿Sobrevivirá este código a cambios futuros sin romperse?

### 4. Code Clarity (Claridad del Código)
- Evalúa legibilidad y organización.
- **Ejemplos:** Nombres descriptivos de variables/funciones, estructura lógica de archivos, comentarios útiles (no redundantes).
- **Foco:** ¿Puede otro desarrollador entender este código sin preguntar al autor?

### 5. Efficiency (Eficiencia)
- Evalúa optimización de rendimiento.
- **Ejemplos:** Complejidad algorítmica adecuada, uso eficiente de memoria, evitar operaciones redundantes.
- **Foco:** ¿Resuelve el problema sin desperdiciar recursos?

---

## ⚖️ Sistema de Pesos

### Pesos Permitidos

| Peso | Significado | Uso |
|---|---|---|
| **5** | Mandatorio | Requisitos críticos que deben cumplirse sin excepción |
| **3** | Importante | Atributos de alta relevancia para la calidad general |
| **1** | Deseable | Características adicionales que aportan valor pero no son obligatorias |

### Pesos Prohibidos

| Peso | Estado |
|---|---|
| **2** | ❌ PROHIBIDO |
| **4** | ❌ PROHIBIDO |
| **0** | ❌ PROHIBIDO |

### Justificación
La escala 1-3-5 fue diseñada para forzar decisiones claras de prioridad. Los pesos intermedios (2 y 4) crean ambigüedad y dificultan la evaluación humana consistente.

---

## 📏 Reglas de Construcción de Criterios

### Regla 1: Atómico
Cada criterio debe evaluar **un solo constraint**. No combinar múltiples verificaciones en un criterio.

```
✅ CORRECTO (Atómico):
   C#1: "El endpoint /api/users retorna un array JSON" [Peso: 5]
   C#2: "El endpoint /api/users soporta paginación con query params page y limit" [Peso: 3]

❌ INCORRECTO (Compuesto):
   C#1: "El endpoint /api/users retorna un array JSON y soporta paginación" [Peso: 5]
```

### Regla 2: Self-Contained (Autosuficiente)
Cada criterio debe poder evaluarse **sin necesidad de referencias externas**. El evaluador no debería necesitar leer el prompt original para entender qué evaluar.

```
✅ CORRECTO: "La función calculate_total() retorna un float con 2 decimales de precisión"
❌ INCORRECTO: "La función cumple con los requisitos de precisión mencionados en el prompt"
```

### Regla 3: Implementation-Agnostic (Agnóstico a la Implementación)
Los criterios **no deben** estar diseñados para que solo el Golden Patch los cumpla. Cualquier implementación válida debe poder pasar.

```
✅ CORRECTO: "El sistema exporta datos en formato CSV con headers en la primera fila"
❌ INCORRECTO: "El sistema usa la función write_csv_with_pandas() para exportar datos"
```

### Regla 4: Positively Framed (Formulación Positiva)
Los criterios deben evaluarse como **PASS** cuando la respuesta es buena.

```
✅ CORRECTO: "El código maneja excepciones de conexión sin crashes" → PASS si lo hace
❌ INCORRECTO: "El código NO crashea al perder conexión" → Doble negación confusa
```

### Regla 5: No Duplicar Tests F2P
Si un test F2P ya verifica un comportamiento, la rúbrica **no debe** incluir un criterio que evalúe lo mismo.

```
✅ CORRECTO: Rúbrica evalúa "legibilidad de nombres de variables" (no testeable por F2P)
❌ INCORRECTO: Rúbrica evalúa "la función retorna el resultado correcto" (ya verificado por F2P)
```

---

## 🔢 Cantidades Requeridas

| Parámetro | Valor |
|---|---|
| Mínimo de criterios | **5** |
| Recomendado | **15 – 20** |
| Máximo absoluto | **30** |

### Regla de Purga
Si el sistema necesita más de 30 criterios, se deben **eliminar los de Peso 1** (deseables) primero. Los criterios de Peso 5 (mandatorios) y Peso 3 (importantes) **jamás** se eliminan en favor de uno de Peso 1.

---

## ⚠️ Errores de Rúbrica Identificados en Auditorías

### Overfitting (Rúbrica demasiado estricta)

| Ejemplo Real | Problema | Página |
|---|---|---|
| "El código debe incluir Type Annotations" | El prompt no exigía type hints; en Python son opcionales | P15 |
| "El chunk size debe ser una constante nombrada" | El prompt pedía "fixed-size chunks", no constantes nombradas | P19 |

**Regla:** Si el prompt no lo exige explícitamente, la rúbrica no puede penalizarlo.

### Underfitting (Rúbrica demasiado laxa)

| Ejemplo Real | Problema | Página |
|---|---|---|
| "No network access" con redacción laxa | Un modelo podría escribir a archivo local Y llamar a API remota y pasar | P19 |

**Regla:** El criterio debe ser lo suficientemente preciso para que una violación real no pase desapercibida.

### Categorización Incorrecta

| Ejemplo Real | Problema | Página |
|---|---|---|
| Algo etiquetado como "Instruction Following" que en realidad es "Code Correctness" | Categoría incorrecta distorsiona la evaluación | P14 |

**Regla:** Revisar que cada criterio esté en la dimensión correcta según su naturaleza.

---

## 📄 Template de Rúbrica

```markdown
# Rúbrica de Evaluación — [Nombre del Proyecto]

## 1. Instruction Following

| # | Criterio | Peso |
|---|---|---|
| C1 | [Descripción atómica y autosuficiente] | 5 |
| C2 | [Descripción atómica y autosuficiente] | 3 |

## 2. Code Correctness

| # | Criterio | Peso |
|---|---|---|
| C3 | [Descripción atómica y autosuficiente] | 5 |
| C4 | [Descripción atómica y autosuficiente] | 3 |

## 3. Code Quality

| # | Criterio | Peso |
|---|---|---|
| C5 | [Descripción atómica y autosuficiente] | 3 |
| C6 | [Descripción atómica y autosuficiente] | 1 |

## 4. Code Clarity

| # | Criterio | Peso |
|---|---|---|
| C7 | [Descripción atómica y autosuficiente] | 3 |
| C8 | [Descripción atómica y autosuficiente] | 1 |

## 5. Efficiency

| # | Criterio | Peso |
|---|---|---|
| C9 | [Descripción atómica y autosuficiente] | 3 |
| C10 | [Descripción atómica y autosuficiente] | 1 |
```

---

## ✅ Checklist de Validación de Rúbrica

Antes de entregar, verificar que la rúbrica:

- [ ] Tiene mínimo **5 criterios** (idealmente 15-20, máximo 30)
- [ ] Usa **solo pesos 1, 3, o 5** (nunca 2 o 4)
- [ ] Cubre las **5 dimensiones** obligatorias
- [ ] Cada criterio es **atómico** (un solo constraint)
- [ ] Cada criterio es **self-contained** (evaluable sin leer el prompt)
- [ ] Cada criterio es **agnóstico** a la implementación del Golden Patch
- [ ] Cada criterio está **positivamente formulado** (PASS = buena respuesta)
- [ ] **No duplica** lo que los tests F2P ya verifican
- [ ] **No exige** lo que el prompt no pidió (evitar overfitting)
- [ ] **No permite** violaciones obvias (evitar underfitting)
- [ ] Cada criterio está en la **dimensión correcta**
- [ ] Los criterios de Peso 5 son verdaderamente mandatorios
