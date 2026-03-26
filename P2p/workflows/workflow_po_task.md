# Workflow — Tarea PO (Performance Optimization)

> Flujo completo desde que recibes el PR hasta la entrega final.

---

## Fase 1: Análisis del PR

1. **Abrir el PR de GitHub** proporcionado en `source_url`
2. **Leer el PR completo**: commits, diff, discusión, benchmarks mencionados
3. **Identificar el cuello de botella** de rendimiento que el PR resuelve
4. **Verificar que es una tarea PO**: ¿Se trata de optimización de velocidad, memoria, latencia, I/O? Si es refactoring/estructura → usar `workflow_rm_task.md`
5. **Identificar el commit padre**: SHA del commit justo antes del PR
6. **Identificar las Target Functions**: funciones específicas con el bottleneck

---

## Fase 2: Crear el Dockerfile

1. Copiar la plantilla desde `templates/Dockerfile.template`
2. Elegir la imagen base correcta
3. Clonar el repo con el **SHA del commit padre**
4. Instalar TODAS las dependencias (incluyendo las de benchmarking)
5. Verificar: NO hay COPY de scripts, NO hay arquitectura específica
6. Probar localmenete: `docker build -t hawkins-task:v1 .`

---

## Fase 3: Escribir el Prompt

1. Copiar la plantilla desde `templates/prompt_template.md`
2. Llenar cada sección enfocada en el problema de rendimiento:
   - **Context**: Describir el repo y el área con el bottleneck
   - **Problem Statement**: Describir el problema de rendimiento
   - **Requirements**: Restricciones de la optimización
   - **Success Criteria**: Mejora medible y cuantificable
   - **Files to Modify**: Archivos que contienen el bottleneck
   - **Notes**: Info adicional SIN pistas ni algoritmos sugeridos
3. Escribir la **User-Facing Problem Description**

---

## Fase 4: Crear el Golden Patch

1. Evaluar si la optimización del PR es la solución perfecta
   - Si lo es → extraer como `.patch`
   - Si no → crear la optimización desde cero
2. Verificar que la optimización produce mejora TANGIBLE y MEDIBLE
3. Solo cambios estrictamente necesarios para la optimización

---

## Fase 5: Crear el Run Script

1. Copiar la plantilla desde `templates/run_script.sh`
2. Identificar pruebas que PASAN actualmente (antes del parche)
3. Configurar para ejecutar SOLO esas pruebas
4. Incluir build si aplica

---

## Fase 6: Implementar parsing.py

1. Copiar la plantilla desde `templates/parsing_template.py`
2. Renombrar a `parsing.py`
3. Implementar `parse_test_output()` para el framework del repo
4. Probar que genera el JSON correcto

---

## Fase 7: Crear el Reproduction Script

1. Copiar la plantilla desde `templates/reproduction_script.sh`
2. Implementar el benchmark del código REAL del repo:
   - **NO benchmarks simulados ni dummies** (fallo automático)
   - Medir una métrica relevante (tiempo, memoria, latencia, ops/sec)
   - Hacer determinista: semillas fijas, warm-up runs, mediana
3. Verificar la salida en formato exacto: `METRIC_VALUE: <número>`
4. Probar pre-parche y post-parche para confirmar mejora

---

## Fase 8: Listar Target Functions

1. Identificar las funciones con el cuello de botella real
2. Listar con formato completo:
   ```
   ruta/archivo.ext::NombreClase::nombre_función
   ```
3. Ejemplo:
   ```
   src/data/processor.py::DataProcessor::process_batch
   src/utils/parser.py::parse_large_file
   ```
4. Verificar que son las funciones que el Golden Patch optimiza

---

## Fase 9: Validación Final

1. Organizar archivos:
   ```
   raíz/
   ├── e2e.sh
   └── app/
       ├── Dockerfile
       ├── golden.patch
       ├── parsing.py
       ├── reproduction_script.sh
       └── run_script.sh
   ```
2. Ejecutar `e2e.sh`
3. Verificar con `checklists/checklist_po_task.md`
4. Confirmar:
   - `before.json` y `after.json` idénticos (tests PASSED)
   - `reproduction_before_stdout.txt` tiene la métrica pre-parche
   - `reproduction_after_stdout.txt` tiene la métrica post-parche (mejorada)
5. ✅ **ENTREGAR**
