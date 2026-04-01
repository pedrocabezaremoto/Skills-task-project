# Historial Task — 1 de Abril 2026

## Tarea Outlier
- **Plataforma:** app.outlier.ai — Real Coder
- **Task ID:** 69ca7d806f42469d31cb4f79
- **Task Rate:** $27/hr
- **Deadline:** 2 abril 2026, 4:01 a.m.
- **Task Type:** Data Science
- **Coding Language:** Python
- **Turn:** 1/1

---

## Descripción de la Tarea Original

La tarea original pedía construir una aplicación de data science en Python que:
- Procese datos de proveedores, registros históricos de entregas, ubicaciones geográficas y logs de lead time
- Construya un modelo de scoring de riesgo que identifique qué proveedores representan mayor riesgo de disrupción
- Genere un reporte de riesgo ordenado con acciones de mitigación (safety stock increases, alternative supplier identification)
- Implemente 5 módulos avanzados:
  1. Simulación de escenarios (what-if analysis)
  2. Mapeo multi-nivel de proveedores
  3. Detección de patrones estacionales
  4. Estimación de impacto de costo
  5. Scoring de diversidad de proveedores

**Restricciones:** Sin fetching de datos en vivo. Sin descarga de datasets externos. Dataset mock generado localmente.

---

## Proceso Completo — Paso a Paso

### Iteración 1 — Prompt inicial (FALLA QC)

Pedro creó el primer prompt con los siguientes problemas detectados en revisión QC:

**Fallas Críticas:**
1. Faltaban interfaces para 2 módulos requeridos: `SeasonalDetector` y `MultiTierMapper`
2. Estilo de escritura incorrecto: `"You are a Data Scientist tasked with..."` — debe ser voz de cliente freelance

**Problemas Moderados:**
3. Esquema de datos mock vago — sin nombres de columnas definidos
4. `DiversityScorer.flag_over_reliance` sin umbral cuantitativo definido
5. `simulate_failure` mezclaba conceptos de multi-tier sin claridad

**Veredicto:** ❌ FALLA — No enviar

---

### Iteración 2 — Prompt mejorado (PASA MÍNIMO, observaciones)

Pedro corrigió las 2 fallas críticas. Nueva revisión QC detectó 4 problemas moderados:

1. `simulate_financial_impact` devuelve `float` sin fórmula de cálculo definida
2. `SeasonalDetector.get_high_risk_months` — "high risk" sin criterio exacto
3. `MultiTierMapper.get_indirect_impacts` — profundidad de traversal no especificada (¿solo nivel 1 o recursivo?)
4. Tech Stack sin versiones de librerías (viola Regla de Determinismo G1)

**Veredicto:** ⚠️ PASA MÍNIMO — score probable 3/5 sin correcciones

---

### Iteración 3 — Prompt final corregido (LISTO PARA ENVIAR)

Se aplicaron los 5 fixes:

| # | Fix | Ubicación |
|---|---|---|
| 1 | Fórmula exacta: `sum(cost_per_unit * lead_time_days)` para dependientes directos e indirectos | Key Req §4 + interface `simulate_financial_impact` |
| 2 | Criterio exacto: "month is high risk if avg `on_time_delivery_rate` is strictly below global average" | Key Req §4 + interface `get_high_risk_months` |
| 3 | Traversal recursivo explícito: "returns all transitive downstream supplier IDs at every level" | Key Req §4 + interface `get_indirect_impacts` |
| 4 | Versiones completas agregadas: pandas 2.2, numpy 1.26, scikit-learn 1.4, pytest 8.1 | Tech Stack |
| 5 | Sin `etc.` — columnas listadas explícitas en descripción de `generate_sample_data` | Expected Interface |

---

## Prompt Final (Versión Aprobada)

```markdown
# Supply Chain Disruption Risk Scoring & Mitigation System

## Description / Context
I am looking for a Python developer to build a local data science 
application. This application MUST process supplier data, historical 
delivery records, geographic locations, and lead time logs to build 
a risk scoring model. The model MUST identify which suppliers and 
supply chain links pose the greatest disruption risk to a business.

The system MUST generate a ranked risk report containing recommended 
mitigation actions. It MUST specifically include two types of 
mitigation actions: safety stock increases and alternative supplier 
identification.

Additionally, the application MUST implement all of the following 
advanced analytical modules:
1. Scenario simulation for what-if analysis on supplier failures.
2. Multi-tier supplier mapping to expose indirect dependencies.
3. Seasonal risk pattern detection.
4. Cost impact estimation per disruption scenario.
5. Supplier diversity scoring module to flag over-reliance on single 
   regions and single vendors.

The application MUST NOT use live data fetching. It MUST NOT require 
downloading datasets. A local mock dataset MUST be generated within 
the codebase so the application can run locally without external 
internet access.

## Tech Stack
- Python 3.10
- pandas 2.2
- numpy 1.26
- scikit-learn 1.4
- pytest 8.1

## Key Requirements

### 1. Mock Data Generation
The application MUST include a script that generates a local CSV file 
named `supply_chain_data.csv`. This dataset MUST contain exactly the 
following columns: `supplier_id`, `supplier_name`, `region`, `tier`, 
`dependent_on_supplier_id`, `delivery_date`, `on_time_delivery_rate`, 
`lead_time_days`, and `cost_per_unit`.

### 2. Risk Scoring Execution
The application MUST implement a risk scoring model that calculates a 
disruption risk score (float between 0.0 and 1.0) for each supplier 
based on the generated CSV data.

### 3. Ranked Risk Report
The application MUST output a ranked risk report that sorts suppliers 
from highest risk to lowest risk. The report MUST include the risk 
score and the specified mitigation actions.

### 4. Advanced Analysis Features
The application MUST implement the following analytical modules:

- **Scenario Simulator:** MUST evaluate the estimated financial cost 
  impact when a specific supplier fails. The cost is calculated as 
  the sum of `cost_per_unit * lead_time_days` across all suppliers 
  that directly or indirectly depend on the failed supplier.

- **Multi-Tier Mapper:** MUST analyze the `dependent_on_supplier_id` 
  column to find all downstream suppliers impacted when a root 
  supplier fails. The traversal MUST be recursive, returning all 
  transitive dependents at every level of the dependency chain.

- **Seasonal Detector:** MUST analyze the `delivery_date` column to 
  identify months with elevated delivery delay risk. A month is 
  considered high risk if its average `on_time_delivery_rate` is 
  strictly below the global average `on_time_delivery_rate` 
  calculated across all records in the dataset.

- **Diversity Scorer:** MUST identify regions where the concentration 
  of suppliers exceeds a user-defined threshold. Concentration is 
  calculated as the count of suppliers in that region divided by the 
  total number of suppliers in the dataset.

## Expected Interface

- Path: `dataset_generator.py`
- Name: `generate_sample_data`
- Type: function
- Input: `None`
- Output: `None`
- Description: Automatically generates the local `supply_chain_data.csv` 
  file with the exact schema defined in Key Requirements §1: 
  `supplier_id`, `supplier_name`, `region`, `tier`, 
  `dependent_on_supplier_id`, `delivery_date`, 
  `on_time_delivery_rate`, `lead_time_days`, `cost_per_unit`.

- Path: `risk_model.py`
- Name: `RiskScoringModel`
- Type: class
- Input: `data_path: str`
- Output: `None`
- Description: Initializes the risk scoring model by loading the CSV 
  data from `data_path`.

- Path: `risk_model.py`
- Name: `RiskScoringModel.generate_ranked_report`
- Type: method
- Input: `None`
- Output: `list[dict]`
- Description: Returns a ranked list of dictionaries sorted by 
  descending risk score. Each dictionary MUST contain 
  `supplier_id` (str), `risk_score` (float between 0.0 and 1.0), 
  and `mitigation_actions` (list[str]).

- Path: `analysis_modules.py`
- Name: `ScenarioSimulator`
- Type: class
- Input: `data_path: str`
- Output: `None`
- Description: Initializes the scenario simulation module by loading 
  the CSV data from `data_path`.

- Path: `analysis_modules.py`
- Name: `ScenarioSimulator.simulate_financial_impact`
- Type: method
- Input: `failed_supplier_id: str`
- Output: `float`
- Description: Returns the estimated financial cost impact when the 
  given supplier fails. Calculated as the sum of 
  `cost_per_unit * lead_time_days` for all suppliers that directly 
  or indirectly depend on `failed_supplier_id` via the 
  `dependent_on_supplier_id` column.

- Path: `analysis_modules.py`
- Name: `MultiTierMapper`
- Type: class
- Input: `data_path: str`
- Output: `None`
- Description: Initializes the dependency mapping module by loading 
  the CSV data from `data_path`.

- Path: `analysis_modules.py`
- Name: `MultiTierMapper.get_indirect_impacts`
- Type: method
- Input: `failed_supplier_id: str`
- Output: `list[str]`
- Description: Traverses the `dependent_on_supplier_id` dependency 
  graph recursively and returns a list of all transitive downstream 
  supplier IDs at every level of the dependency chain when the given 
  supplier fails.

- Path: `analysis_modules.py`
- Name: `SeasonalDetector`
- Type: class
- Input: `data_path: str`
- Output: `None`
- Description: Initializes the seasonal risk pattern module by 
  loading the CSV data from `data_path`.

- Path: `analysis_modules.py`
- Name: `SeasonalDetector.get_high_risk_months`
- Type: method
- Input: `None`
- Output: `list[int]`
- Description: Returns a list of month numbers (1-12) where the 
  average `on_time_delivery_rate` for that month is strictly below 
  the global average `on_time_delivery_rate` across all records 
  in the dataset.

- Path: `analysis_modules.py`
- Name: `DiversityScorer`
- Type: class
- Input: `data_path: str`
- Output: `None`
- Description: Initializes the supplier diversity scoring module by 
  loading the CSV data from `data_path`.

- Path: `analysis_modules.py`
- Name: `DiversityScorer.flag_over_reliance`
- Type: method
- Input: `concentration_threshold: float`
- Output: `list[str]`
- Description: Returns a list of region names where the percentage 
  of total suppliers located in that region is strictly greater than 
  `concentration_threshold` (e.g., passing 0.40 returns regions 
  that contain more than 40% of all suppliers in the dataset).

## Current State
Empty repository with test files only.
```

---

## Estado Actual de la Tarea

- ✅ Turn #1 (Prompt) — Completado y pegado en Outlier
- ✅ Linter 1: Determinism Check — PASS (palabra "recommended" → "specific", fórmula de risk_score definida)
- ✅ Linter 2: Expected Interface Eval (1) — FAIL (Falta fórmula y descripciones exactas de mitigación) → **Corregido**
- ✅ Linter 3: Linter Re-check — FAIL (Trampa de alcance abierto "at least one") → **Corregido** a "exactly two".
- ✅ Linter 4: Expected Interface Eval (2) — FAIL (Artifacts de Markdown en las rutas como `[generator.py]`) → **Overflag ignorado**
- ✅ Linter 5: Logical Flaw Checkpoint — PASS (Score 90). Tuvo 2 advertencias (Signal-to-Message Mismatch por granularidad y Seed Alignment por scikit-learn) pero al ser PASS permitieron avanzar.
- 🔄 Turn #2 (F2P Tests) — **EN CURSO** (Infraestructura TDD definida. Pendiente: escribir test_main.py, correr en empty codebase, subir screenshots).
- ⏳ Turn #3 (Rúbricas) — Pendiente
- ⏳ Turn #4 (Golden Patch) — Pendiente
- ⏳ Validación F2P (before.json / after.json) — Pendiente
- ⏳ Submit final — Pendiente

---

## Iteraciones del Evaluador de la Plataforma (Detalle 1 Abril)

1. **Expected Interface (Misleading Description):** El linter notó que faltaba la fórmula matemática del Score y los 2 tipos de mitigación requeridos por el usuario en `generate_ranked_report`. Se corrigió inyectando eso en la descripción.
2. **Open-Ended Scope Trap ("at least one"):** El linter detectó como crítico pedir "al menos una" acción de mitigación porque rompía la regla de determinismo (el LLM podía generar 1 o 50). Se corrigió pidiendo **"exactly two"**.
3. **Markdown Link Artifacts en Paths (Overflag):** El editor de la plataforma auto-formateaba `.py` como enlaces (ej. `dataset_[generator.py](http...)`). Esto provocó un FAIL masivo en la interfaz. Se marcó como **Overflag** respondiendo "Yes" a ignorarlo.
4. **Logical Flaw Checkpoint (PASS 90/100):** 
   - *Data Granularity:* El CSV para `SeasonalDetector` requiere muchas filas, pero el `risk_score` asume 1 fila por proveedor.
   - *Seed Alignment:* Se pide `scikit-learn` en el stack pero se usó una fórmula determinista pesada (hardcoded) en lugar de un modelo entrenado.
   - **Veredicto:** A pesar de los warnings, el estado dio **PASS**, lo que permite continuar sin reescribir todo (son mejoras sugeridas).

---

## Lecciones Aprendidas

1. **Estilo del prompt** — Siempre en primera persona como cliente freelance, nunca dirigirse al agente directamente
2. **Expected Interface** — Todo módulo mencionado en Key Requirements DEBE tener su entrada en Expected Interface con los 6 campos
3. **Fórmulas explícitas** — Cualquier cálculo que devuelva un número debe tener la fórmula escrita en la descripción
4. **Determinismo Lingüístico** — Jamás usar frases como "at least one" o "or". Todo debe ser exacto (ej. "exactly two").
5. **Overflags** — El editor de la plataforma puede corromper texto convirtiendo `.py` en hipervínculos. Marcar siempre como overflag si lógicamente tu path era correcto.
6. **Tech Stack con versiones** — Siempre incluir versión exacta de cada librería

---

---

## Turn #2 — TDD Phase (F2P Tests)

### Pasos completados en la plataforma (1 Abril)

| Paso | Estado | Detalle |
|------|--------|---------|
| Double check design | ✅ | Respondido "Yes" — warnings son overflags, PASS 90/100 |
| Rate Difficulty | ✅ | Seleccionado **Hard** (múltiples módulos, fórmulas, data models; sin auth ni real-time) |
| Full-Stack Requirements Decomposition | ✅ | Plataforma generó 44 unit test requirements + 30 rubric items |
| Provide F2P tests (Current) | 🔄 | Pendiente: escribir test_main.py, correr en empty codebase, subir evidencia |

### Infraestructura TDD requerida por la plataforma

**Folder structure esperada:**
```
/app/
|-- Dockerfile        (usar template oficial, NO usar COPY command)
|-- tests.zip         (suite de tests: test_main.py + run.sh + parsing.py)
|-- codebase.zip      (Golden Patch — se construye después)
|-- run.sh            (script que corre los tests)
|-- parsing.py        (script que parsea output a JSON)
```

**run.sh (template a completar):**
```bash
#!/bin/bash
### COMMON SETUP; DO NOT MODIFY ###
set -e

run_all_tests() {
  # Para Python + pytest:
  pip install pytest pandas numpy scikit-learn --quiet
  cd /app/tests
  pytest test_main.py -v --tb=short 2>&1
}

### COMMON EXECUTION; DO NOT MODIFY ###
run_all_tests
```

**parsing.py — lógica a implementar:**
- Parsear stdout de pytest para extraer cada test con su resultado
- Mapear a `PASSED`, `FAILED`, `SKIPPED`, `ERROR`
- Output: JSON con lista de `{name, status}`

**Regla crítica del Dockerfile:**
- NO usar el comando `COPY` 
- Solo agregar dependencias una por una con `RUN pip install ...`

### F2P Requirement: Before vs After Golden Patch

- **Before (empty codebase):** Correr tests → todos deben mostrar `FAILED` (NO `ERRORED`)
- **After (Golden Patch):** Correr tests → todos deben mostrar `PASSED`
- La plataforma pide 3 evidencias:
  1. Screenshot de `run.sh` con todos los tests FAILED
  2. JSON output de `parsing.py`  
  3. Pegado del código de `test_main.py` para Overly-Specific Eval

### 44 Requisitos Unitarios (F2P Coverage)

| ID | Requisito | Fuente |
|----|-----------|--------|
| 1 | `dataset_generator.py` tiene función `generate_sample_data` sin argumentos que devuelve None | Expected Interface §1 |
| 2 | `generate_sample_data()` crea archivo `supply_chain_data.csv` en directorio local | Key Req §1 |
| 3 | CSV tiene exactamente las columnas: supplier_id, supplier_name, region, tier, dependent_on_supplier_id, delivery_date, on_time_delivery_rate, lead_time_days, cost_per_unit | Key Req §1 |
| 4 | CSV tiene al menos una fila de datos | Key Req §1 |
| 5 | `on_time_delivery_rate` son floats entre 0.0 y 1.0 | Key Req §1, §2 |
| 6 | `lead_time_days` son números positivos | Key Req §1 |
| 7 | `cost_per_unit` son números positivos | Key Req §1 |
| 8 | `delivery_date` son strings de fecha parseables | Key Req §1 |
| 9 | `risk_model.py` tiene clase `RiskScoringModel` instanciable con `data_path: str` | Expected Interface §2 |
| 10 | `RiskScoringModel.__init__` carga CSV del `data_path` | Expected Interface §2 |
| 11 | `generate_ranked_report()` devuelve `list[dict]` | Expected Interface §3 |
| 12 | Cada dict tiene `supplier_id` (str) | Expected Interface §3 |
| 13 | Cada dict tiene `risk_score` (float entre 0.0 y 1.0) | Expected Interface §3 |
| 14 | Cada dict tiene `mitigation_actions` (list[str]) | Expected Interface §3 |
| 15 | `mitigation_actions` tiene exactamente 2 entradas | Expected Interface §3 |
| 16 | Una acción recomienda safety stock increase | Expected Interface §3 |
| 17 | Una acción recomienda alternative supplier identification | Expected Interface §3 |
| 18 | `risk_score` se calcula con fórmula exacta para input conocido | Key Req §2 |
| 19 | Report ordenado descendente por `risk_score` | Key Req §3 |
| 20 | `analysis_modules.py` tiene `ScenarioSimulator` instanciable con `data_path: str` | Expected Interface §4 |
| 21 | `simulate_financial_impact(failed_supplier_id)` devuelve float | Expected Interface §4 |
| 22 | Impacto financiero = sum(cost_per_unit * lead_time_days) para dependientes directos e indirectos | Key Req §4 |
| 23 | Devuelve 0.0 cuando proveedor no tiene dependientes | Key Req §4 |
| 24 | `MultiTierMapper` instanciable con `data_path: str` | Expected Interface §5 |
| 25 | `get_indirect_impacts(failed_supplier_id)` devuelve `list[str]` | Expected Interface §5 |
| 26 | Traversal recursivo correcto para dependency graph conocido | Key Req §4 |
| 27 | Devuelve lista vacía si no hay dependientes | Key Req §4 |
| 28 | Maneja cadenas multi-nivel (A→B→C devuelve [B, C] cuando A falla) | Key Req §4 |
| 29 | `SeasonalDetector` instanciable con `data_path: str` | Expected Interface §6 |
| 30 | `get_high_risk_months()` devuelve `list[int]` | Expected Interface §6 |
| 31 | Cada elemento es entero entre 1 y 12 | Expected Interface §6 |
| 32 | Mes incluido si y solo si avg OTR < global avg OTR | Key Req §4 |
| 33 | `DiversityScorer` instanciable con `data_path: str` | Expected Interface §7 |
| 34 | `flag_over_reliance(threshold)` devuelve `list[str]` | Expected Interface §7 |
| 35 | Devuelve regiones donde (count/total) > threshold | Key Req §4 |
| 36 | `flag_over_reliance(1.0)` devuelve lista vacía | Key Req §4 |
| 37 | `flag_over_reliance(0.0)` devuelve todas las regiones con al menos 1 proveedor | Key Req §4 |
| 38 | `simulate_financial_impact` incluye dependientes transitivos, no solo directos | Key Req §4 |
| 39 | CSV incluye proveedores con distintos valores de `tier` | Key Req §1, §4 |
| 40 | CSV incluye `dependent_on_supplier_id` formando cadena multi-nivel (depth ≥ 2) | Key Req §1, §4 |
| 41 | CSV incluye `delivery_date` en múltiples meses | Key Req §1, §4 |
| 42 | CSV incluye proveedores de múltiples regiones | Key Req §1, §4 |
| 43 | Ningún módulo hace fetch de datos externos ni requiere internet | Description/Context |
| 44 | `generate_ranked_report` devuelve 1 entrada por `supplier_id` único | Key Req §3 |

### 30 Rubric Items (Top Gaps — para Golden Patch)

Los rubrics con peso 5 (críticos):
1. `generate_sample_data` no usa fetching externo — solo Python/pandas/numpy
2. Fórmula risk_score implementada exactamente (pesos 0.5, 0.3, 0.2)
3. `get_indirect_impacts` usa BFS/DFS recursivo (cierre transitivo completo)
4. `get_indirect_impacts` maneja ciclos con visited-set (sin infinite loop)
5. `simulate_financial_impact` incluye transitivos, no solo directos
6. Tech stack: solo Python 3.10, pandas 2.2, numpy 1.26, scikit-learn 1.4, pytest 8.1
7. Estructura de archivos exacta: dataset_generator.py, risk_model.py, analysis_modules.py
8. Dataset mock es realista: múltiples regiones, tiers, dependency chains ≥2, meses variados, OTR variado
9. `mitigation_actions` tiene exactamente 2 strings (safety stock + alternative supplier)
10. Columnas CSV con nombres exactos (sin extras ni renombradas)
11. App corre 100% offline sin internet
12. Report agrega a 1 entrada por `supplier_id`
13. Columnas CSV usan nombres exactos especificados

---

## Guías de Referencia Usadas

- `guia1_flujo_principal.md` — Flujo de 16 pasos, Regla de Determinismo
- `guia3_auditoria_especificaciones.md` — Criterios de auditoría QC
- `guia8_errores_comunes_correccion.md` — Errores comunes en prompts y Expected Interface
- `promptchecker.md` — Checklist de revisión de prompts
- `master_guide.md` — Referencia consolidada G1-G9
