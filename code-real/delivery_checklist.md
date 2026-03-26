# ✅ Delivery Checklist — Lista de Verificación para Entrega Final

> **Uso:** Verificar CADA punto antes de hacer Submit en la plataforma.
> Ref: G1 §5, G3 §Paso 6, G5 §3, G7 §1-2, G8 §Lista Final, G9 §5

---

## 🔴 Pre-Entrega: Verificaciones Obligatorias

### 1. Golden Patch (G1 §Paso 4-5, G8 §1)

- [ ] El código compila y ejecuta sin errores de runtime
- [ ] Cada funcionalidad del prompt está implementada y accesible
- [ ] Cada requisito del prompt es rastreable hasta el código
- [ ] Las funcionalidades son accesibles desde la UI (no solo API)
- [ ] Probados todos los flujos de usuario, no solo el "camino feliz"
- [ ] Probados casos de borde: entradas vacías, comillas, reinicios
- [ ] Activos 100% comerciales (Google Fonts, Lucide, Pexels — nunca Unsplash)
- [ ] Sin bibliotecas prohibidas
- [ ] Modularidad y abstracción correcta (no todo en un archivo)
- [ ] Variables con nombres descriptivos y no engañosos
- [ ] Comentarios en lógica compleja (máquinas de estado, fórmulas)
- [ ] El Golden Patch pasa todos los criterios de la rúbrica

### 2. Prompt Reescrito (G1 §Paso 1, G8 §2)

- [ ] Tiene las 4 secciones: Título, Tech Stack, Requirements, Expected Interface
- [ ] Expected Interface tiene los 6 campos por entrada: Path, Name, Type, Input, Output, Description
- [ ] Estilo "solicitud de cliente" (no imperativo)
- [ ] Sin referencias internas ni notas de tarea
- [ ] Sin meta-datos (presupuesto, cronograma)
- [ ] Restricciones realistas y compatibles entre sí
- [ ] Stack tecnológico explícito (no "Any")

### 3. Pruebas F2P (G1 §Paso 2, G2 §3, G8 §4)

- [ ] **before.json**: TODAS las pruebas muestran FAILED (no ERROR ni PASS)
- [ ] **after.json**: TODAS las pruebas muestran PASSED
- [ ] Pruebas ejecutadas dentro de Docker (ubuntu:22.04)
- [ ] Sin sobre-especificidad (no fuerzan nombres internos no pedidos)
- [ ] Sin mocking de componentes internos del código
- [ ] Excepciones estrechas (no `except Exception` genérico)
- [ ] Cobertura: cada comportamiento backend tiene al menos 1 prueba

### 4. Rúbricas (G1 §Paso 3, G2 §4, G3 §4)

- [ ] Mínimo 5 criterios (recomendado 10+)
- [ ] Cada criterio es atómico (1 concepto)
- [ ] Cada criterio es autocontenido
- [ ] Encuadre positivo (respuesta correcta = Sí)
- [ ] Pesos solo 1, 3 o 5 (nunca 2 o 4)
- [ ] Sin términos vagos ("apropiado", "limpio", "significativo")
- [ ] Cubre las 5 dimensiones: Instrucciones, Corrección, Calidad, Claridad, Eficiencia
- [ ] Neutral a la implementación (no penaliza soluciones válidas alternativas)

### 5. Cobertura Total (G2 §2, G8 §5)

- [ ] Cada requisito del prompt está cubierto por una prueba O una rúbrica
- [ ] No existen "requisitos huérfanos" sin validación
- [ ] Backend cubierto por pruebas unitarias
- [ ] Frontend cubierto por rúbricas (y pruebas si es posible)

---

## 📦 Estructura de Archivos (G7 §1-2)

### Directorio /app — Exactamente 5 componentes

- [ ] `Dockerfile` presente
- [ ] `tests.zip` presente
- [ ] `codebase.zip` presente
- [ ] `run.sh` presente
- [ ] `parsing.py` presente
- [ ] **Ningún otro archivo** en `/app` (no suites de prueba sueltas)

### Regla de Oro de Compresión (G7 §2)

- [ ] `tests.zip` → contiene `tests/` como primer nivel de jerarquía
- [ ] `codebase.zip` → contiene archivos directamente (SIN carpeta raíz anidada)
  - ✅ Correcto: `codebase.zip → archivo.py, src/, ...`
  - ❌ Incorrecto: `codebase.zip → codebase/ → archivo.py`

---

## 🐳 Docker y Entorno (G4, G5, G8 §6)

- [ ] Imagen base: `ubuntu:22.04` (obligatoria, no modificable)
- [ ] Sin comando `COPY` ni `ADD` para código del proyecto
- [ ] `WORKDIR /app` configurado
- [ ] `DEBIAN_FRONTEND=noninteractive` configurado
- [ ] Todas las dependencias del Golden Patch instaladas en el Dockerfile
- [ ] **`run.sh` usa finales de línea LF** (no CRLF)
  - Verificar con: `file run.sh` → debe decir "ASCII text" no "CRLF"
- [ ] **`parsing.py` usa finales de línea LF**
- [ ] Secciones `DO NOT MODIFY` intactas en `run.sh` y `parsing.py`
- [ ] No se instalan dependencias en runtime (`run.sh`)

---

## 📸 Evidencias de Entrega (G1 §5)

- [ ] Captura de pantalla de `run.sh` mostrando fallos iniciales (before)
- [ ] Captura de pantalla de `run.sh` mostrando éxitos finales (after)
- [ ] Archivo `before.json` generado
- [ ] Archivo `after.json` generado
- [ ] `codebase.zip` actualizado
- [ ] `tests.zip` actualizado
- [ ] `Dockerfile`, `run.sh`, `parsing.py` finales
- [ ] Captura de timestamp de última edición de cada archivo

---

## 📊 Calificación Final (G3 §5, G9 §5)

> **Regla de la Dimensión Más Baja**: El puntaje final = la dimensión con el puntaje más bajo.

| Puntaje | Condición |
|---|---|
| **5** | TODAS las dimensiones son perfectas. Sin errores de ningún tipo. |
| **4** | Problemas menores, la solución es buena pero no perfecta. |
| **3** | Problemas moderados pero la funcionalidad core está presente. |
| **2** | Fallo en una dimensión crítica. |
| **1** | Poco o ningún esfuerzo, múltiples fallos. |

> ⚠️ Si hay un error 3 o 4 en cualquier dimensión → la tarea **NO puede** recibir un 5.
