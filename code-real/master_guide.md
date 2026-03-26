# 📘 Guía Maestra Real Coder — Referencia Consolidada G1-G9

> **Documento de referencia obligatoria** para todo el equipo del proyecto Real Coder.
> Consolida las 9 guías oficiales en un solo punto de acceso rápido.
> 
> **Archivos complementarios del módulo:**
> - [`promptchecker.md`](promptchecker.md) — Checklist de revisión de prompts
> - [`rubric_template.md`](rubric_template.md) — Plantilla y estándares de rúbricas
> - [`delivery_checklist.md`](delivery_checklist.md) — Checklist de entrega final
> - [`validation.sh`](validation.sh) — Script F2P automatizado
> - [`Dockerfile`](Dockerfile) — Entorno Docker (ubuntu:22.04)
> - [`run.sh`](run.sh) — Ejecutor de pruebas
> - [`parsing.py`](parsing.py) — Traductor JSON

---

## 1. Objetivo del Proyecto (G1)

Generar soluciones de software de alta calidad, verificadas y listas para implementación, partiendo de descripciones de tareas de estilo freelance. El producto final es un **Golden Patch** — una implementación de referencia completamente funcional.

### Pilares Críticos

| # | Pilar | Descripción |
|---|---|---|
| 1 | **Reescritura de Prompts** | Brief del cliente → especificación técnica estructurada |
| 2 | **Verificación de Doble Capa** | Pruebas F2P + Rúbricas Expertas |
| 3 | **Fidelidad al Entorno** | Docker obligatorio (ubuntu:22.04) |
| 4 | **Cumplimiento Legal** | Activos 100% comerciales, sin Unsplash |

---

## 2. Herramientas Permitidas (G1, G2)

| Herramienta | Condición |
|---|---|
| **OpenCode** | Recomendado (gratuito, vinculable a cuentas Pro LLM) |
| **Cursor** | Reembolso solo tras primera tarea exitosa (QC ≥ 3/5). Plan $20 inicial. |
| **Claude 4.6** | Modelo recomendado dentro de Cursor |
| **Docker** | Obligatorio para toda ejecución y validación |
| **Tara Eval** | Mandatorio para revisores (taraeval.vercel.app) |

### Activos Visuales Permitidos (G1 §2)

| ✅ Permitido | ❌ Prohibido |
|---|---|
| Google Fonts | Unsplash |
| Lucide / Heroicons | Iconos con copyright |
| Pexels | APIs no autorizadas |
| Placeholders (ante duda) | Clonación de UI existentes |

---

## 3. Flujo de Trabajo Completo: 6 Pasos (G1 §3)

```
Paso 0 → Paso 1 → Paso 2 → Paso 3 → Paso 4 → Paso 5
Comprender   Prompt    F2P      Rúbrica   Build    Verify
```

### Paso 0: Comprensión de Requerimientos
Revisar 4 secciones de la tarea semilla:
- **Tipo de Tarea** — Categoría (herramienta, pipeline, app web)
- **Lenguaje** — Si no se especifica, elegir stack adecuado
- **Descripción Corta** — Restricciones globales
- **Descripción de Tarea** — Brief del cliente a expandir

### Paso 1: Generación del Prompt Reescrito
Prompt Markdown que incluye:
- **Título + Contexto** — Nombre y objetivos
- **Tech Stack** — Lenguajes/frameworks explícitos (nunca "Any")
- **Key Requirements** — Funcionalidades detalladas
- **Expected Interface** — 6 campos obligatorios por entrada

> 📝 Usar [`promptchecker.md`](promptchecker.md) para validar

### Paso 2: Pruebas F2P (Fail-to-Pass)
1. Crear pruebas unitarias ANTES de la solución (TDD)
2. Ejecutar sobre repo vacío → todas deben **FALLAR** (FAILED, no ERROR)
3. Las pruebas deben ser **agnósticas** — no dictan arquitectura interna

### Paso 3: Rúbricas Expertas
- 5 dimensiones + pesos 1/3/5 + atomicidad
- Cubren lo que las pruebas no pueden: UI/UX, calidad, diseño

> 📝 Usar [`rubric_template.md`](rubric_template.md) como plantilla

### Paso 4: Construcción del Golden Patch
1. Generar solución inicial con agente IA
2. Refinar hasta perfección

### Paso 5: Verificación Final
1. Ejecutar pruebas → todas PASAN
2. Validar contra rúbrica
3. Ejecutar `validation.sh` → genera `before.json` + `after.json`

> 📝 Usar [`delivery_checklist.md`](delivery_checklist.md) antes del Submit

---

## 4. Expected Interface — Los 6 Campos (G3, G6, G8)

Cada componente público DEBE documentar:

| Campo | Descripción | Obligatorio |
|---|---|---|
| **Path** | Ruta del archivo | ✅ |
| **Name** | Nombre función/clase/endpoint | ✅ |
| **Type** | function / class / API endpoint | ✅ |
| **Input** | Parámetros con tipos | ✅ (N/A si no aplica) |
| **Output** | Tipo de retorno / respuesta HTTP | ✅ (N/A si no aplica) |
| **Description** | Qué validará la prueba | ✅ |

### Principios de Diseño de la Interfaz (G6 §1)
- **Superficie mínima** — Solo elementos primordiales
- **Tipado estricto** — Tipos explícitos siempre
- **Agnóstica** — No mencionar internals

---

## 5. Pruebas F2P en Detalle (G1, G2, G3, G6, G8)

### Proceso de Validación Dual

| Fase | Entrada | Resultado Esperado |
|---|---|---|
| **Before (Baseline)** | Codebase vacía | Todos los tests → FAILED |
| **After (Golden Patch)** | Codebase completa | Todos los tests → PASSED |

### Reglas Críticas de las Pruebas

| Regla | Ref |
|---|---|
| Tests deben marcar FAIL, nunca ERROR ni crash | G2 §3 |
| Sin sobre-especificidad (> 5% = fallo) | G8 §4 |
| Sin mocking de componentes internos | G6 §2 |
| Excepciones estrechas (no `except Exception`) | G8 §4 |
| Sin nombres hardcoded no pedidos en el prompt | G8 §4 |
| Tests son "caja negra" — solo usan la Expected Interface | G6 §2 |
| Prohibido parchear rutas internas de importación | G8 §4 |

### Scripts de Evaluación (G6 §2)
- Interactúan SOLO a través de la Expected Interface
- Verifican I/O: entrada → salida esperada
- Cubren: casos estándar, edge cases, entradas inválidas
- Para DB/filesystem: verifican estado resultante

### Rúbricas como "Caja Blanca" (G6 §3)
- Acceso total al código fuente
- Validan: restricciones de librerías, patrones de diseño, seguridad, UI/UX
- Evalúan: legibilidad, documentación, estilo

---

## 6. Rúbricas Expertas en Detalle (G2, G3, G8, G9)

### Las 5 Dimensiones

| Dimensión | Qué Evalúa |
|---|---|
| Seguimiento de Instrucciones | Completitud vs. prompt |
| Corrección del Código | Funcionalidad, compilación, runtime |
| Calidad del Código | Modularidad, abstracción, naming |
| Claridad | Legibilidad, comentarios, estructura |
| Eficiencia | Complejidad algorítmica, recursos |

### Escala de Pesos (SOLO 1, 3, 5)

| Peso | Criterio |
|---|---|
| **5** = Mandatorio | Sin este, la respuesta es inaceptable |
| **3** = Importante | Sustancialmente mejor con este |
| **1** = Deseable | Nice to have |

### Umbrales de Error (G3 §4)

| Errores Mayores | > 5% → Fallo |
|---|---|
| Errores Moderados | > 15% → Fallo |
| Errores Menores | > 25% → Fallo |

> 📝 Ver [`rubric_template.md`](rubric_template.md) para plantilla completa

---

## 7. Docker y Estructura de Archivos (G4, G5, G7)

### Estructura Obligatoria de /app (G7 §1)

```
app/
├── Dockerfile       ← Ubuntu 22.04, dependencias, sin COPY
├── tests.zip        ← Contiene tests/ como primer nivel
├── codebase.zip     ← Archivos directos, SIN carpeta raíz
├── run.sh           ← Ejecutor de pruebas (LF obligatorio)
└── parsing.py       ← Traductor → results.json
```

> ⚠️ Exactamente 5 archivos. Nada más, nada menos.

### Regla de Oro de Compresión (G7 §2)

| Archivo | Estructura |
|---|---|
| `tests.zip` | → `tests/` como carpeta de primer nivel |
| `codebase.zip` | → archivos directos (sin carpeta contenedora) |

### Dockerfile — Reglas (G4, G5)

| ✅ Permitido | ❌ Prohibido |
|---|---|
| Instalar dependencias con `apt-get` | Usar `COPY` o `ADD` para código |
| Instalar paquetes Python con `pip` | Cambiar imagen base |
| Añadir frameworks/runtimes | Modificar `WORKDIR /app` |
| Sección de dependencias delimitada | Alterar entrypoints |

### Dependencias Obligatorias del Sistema (G4 §1)
`git`, `python3`, `python3-pip`, `python3-setuptools`, `python-is-python3`, `unzip`

### run.sh — Reglas (G4 §2, G5 §2)
- Solo editar `run_all_tests()` para especificar el comando de pruebas
- `set -e` es configuración protegida (DO NOT MODIFY)
- NO instalar dependencias en runtime
- Guardar con finales de línea **LF** (no CRLF)

### parsing.py — Estructura (G4 §3)
- `Enum TestStatus`: PASSED(1), FAILED(2), SKIPPED(3), ERROR(4)
- `dataclass TestResult`: name + status
- Solo editar `parse_test_output()` — resto protegido

---

## 8. Comandos de Ejecución (G4 §Protocolo, G5)

### Construcción
```bash
docker build -t real-coder-<task-id> .
```

### Ejecución Interactiva
```bash
docker run -it real-coder-<task-id>:latest /bin/bash
```

### Ejecución de Pruebas (dentro del contenedor)
```bash
bash run.sh
```

### Validación F2P Automatizada
```bash
bash validation.sh
```

### Windows PowerShell
```powershell
docker build -t real-coder-env ./app
docker run --name rc-test -v "${PWD}\app:/app" -w /app -it real-coder-env bash -Ic "chmod +x run.sh && ./run.sh"
```

---

## 9. Protocolo de Auditoría — Revisores (G3, G9)

### Flujo de 5 Pasos del Revisor (G9 §2)

| Paso | Acción | Descripción |
|---|---|---|
| 1 | Crear Entorno | Configuración local + descarga de archivos |
| 2 | Ejecutar Tara Eval | Informe inicial de calidad (taraeval.vercel.app) |
| 3 | Corregir Tarea | Revisión manual de prompt, tests, rúbricas, código |
| 4 | Validación Final | Re-ejecutar validation.sh para determinismo |
| 5 | Entrega y Feedback | Puntajes + retroalimentación constructiva |

### Estructura de Directorios del Revisor (G9 §3)

```
proyecto/
├── app/                ← Archivos base (5 componentes)
├── without_solution/   ← Baseline: Dockerfile + tests + run.sh + parsing.py
└── with_solution/      ← Golden: todo lo anterior + codebase extraído
```

### Los 6 Pasos de Auditoría (G3 §2)

1. **Revisión de Instrucciones** — Asimilar tarea original
2. **Evaluación del Prompt** — Expected Interface obligatoria con 6 campos
3. **Evaluación del Golden Patch** — Lógica + Docker correctos
4. **Evaluación de Pruebas F2P** — JSON deterministas (before/after)
5. **Auditoría de la Rúbrica** — Atómica, verificable, autocontenida
6. **Calificación Final** — Escala 1-5, regla de dimensión más baja

---

## 10. Sistema de Calificación (G3 §5, G9 §5)

### Reglas de Precedencia

| Regla | Descripción |
|---|---|
| **Dimensión Más Baja** | La tarea se califica por su dimensión con puntaje más bajo |
| **Turno Más Bajo** | En multi-turno, el puntaje más bajo de cualquier turno define el total |
| **1 vs 2** | 1 = poco/ningún esfuerzo; 2 = esfuerzo con fallo crítico |
| **3 vs 4** | Juicio profesional sobre gravedad del problema menor |
| **Regla del 5** | Solo 5 si TODAS las dimensiones son perfectas |

### Criterios de Fallo por Dimensión (G3 §3)

| Dimensión | Fallo (1-2) |
|---|---|
| Compilación | No compila o errores de runtime |
| Rendimiento | O(n³) cuando O(n log n) es posible |
| Legibilidad | Sin modularidad, variables engañosas |
| Prompt | Interfaces ausentes, errores factuales |
| Rúbrica | > 5% errores mayores |

---

## 11. Errores Más Comunes — Referencia Rápida (G8)

### Golden Patch
| Error | Impacto |
|---|---|
| Omisión de instrucciones explícitas | Funcionalidad incompleta |
| Funciones solo por API, no por UI | No cumple el prompt |
| DB se reinicia en cada arranque | Pérdida de datos |
| Rutas sin autenticación devuelven 302 | Vulnerabilidad de seguridad |
| Sin comentarios en lógica compleja | Ilegibilidad |

### Pruebas
| Error | Impacto |
|---|---|
| Nombres hardcoded no pedidos | Sobre-especificidad |
| Mocks de rutas internas | Pruebas frágiles |
| `except Exception` genérico | Tests pasan accidentalmente |
| Tests que verifican "hay respuesta" sin contenido | Cobertura falsa |

### Docker
| Síntoma | Causa | Solución |
|---|---|---|
| `python3\r: No such file` | Formato CRLF | Convertir a LF |
| Import falla | Dependencia faltante | Añadir en Dockerfile |
| Montaje falla | Ruta incorrecta | PowerShell: `"${PWD}\dir:/app"` |
| Build falla | COPY prohibido | Usar montaje por volumen |

---

## 12. Tabla de Referencia por Guía

| Guía | Tema Principal | Archivos Relevantes |
|---|---|---|
| **G1** | Flujo de trabajo completo, estructura | `master_guide.md`, `README.md` |
| **G2** | Cobertura pruebas vs rúbricas | `rubric_template.md` |
| **G3** | Auditoría, calificación, umbrales | `rubric_template.md`, `delivery_checklist.md` |
| **G4** | Docker setup, plantillas | `Dockerfile`, `run.sh`, `parsing.py` |
| **G5** | Docker Mac/Windows, CRLF | `validation.sh`, `delivery_checklist.md` |
| **G6** | Interfaz Esperada, caja negra/blanca | `promptchecker.md`, `master_guide.md` |
| **G7** | Estructura de archivos, ZIPs | `delivery_checklist.md`, `validation.sh` |
| **G8** | Errores comunes, 6 campos | `promptchecker.md`, `delivery_checklist.md` |
| **G9** | Protocolo de revisores | `delivery_checklist.md`, `master_guide.md` |
