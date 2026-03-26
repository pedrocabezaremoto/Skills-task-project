# Workflow — Tarea R/M (Refactoring/Maintainability)

> Flujo completo desde que recibes el PR hasta la entrega final.

---

## Fase 1: Análisis del PR

1. **Abrir el PR de GitHub** proporcionado en `source_url`
2. **Leer el PR completo**: commits, diff, discusión, issue vinculado
3. **Identificar el problema** que resuelve el PR
4. **Verificar que es una tarea R/M**: ¿Se trata de refactoring, migración, mejora de estructura, actualización de estándares? Si es optimización de rendimiento → usar `workflow_po_task.md`
5. **Identificar el commit padre**: el commit justo antes del primer commit del PR (anotar el SHA)

---

## Fase 2: Crear el Dockerfile

1. Copiar la plantilla desde `templates/Dockerfile.template`
2. Elegir la imagen base correcta (Python/Node/Ubuntu)
3. Configurar la clonación del repo con el **SHA del commit padre**
4. Instalar TODAS las dependencias necesarias
5. Verificar: NO hay COPY de scripts, NO hay arquitectura específica
6. Probar localmente: `docker build -t hawkins-task:v1 .`

---

## Fase 3: Escribir el Prompt

1. Copiar la plantilla desde `templates/prompt_template.md`
2. Llenar cada sección:
   - **Context**: Describir el proyecto/repo
   - **Problem Statement**: Describir el problema como si no estuviera resuelto
   - **Requirements**: Listar restricciones específicas
   - **Success Criteria**: Criterios medibles
   - **Files to Modify**: Archivos que necesitan cambios
   - **Notes**: Info adicional SIN pistas
3. Verificar: Sin soluciones, sin referencias al PR, sin "you"
4. Escribir la **User-Facing Problem Description** (resumen breve)

---

## Fase 4: Crear el Golden Patch

1. Evaluar si el diff del PR es la "solución perfecta"
   - Si lo es → extraer como `.patch`
   - Si no → crear la solución desde cero
2. Formato: unified diff (`.patch`)
3. Verificar que se aplica limpiamente: `git apply golden.patch`
4. Solo cambios estrictamente necesarios

---

## Fase 5: Crear el Run Script

1. Copiar la plantilla desde `templates/run_script.sh`
2. Identificar qué pruebas PASAN actualmente (antes del parche)
3. Configurar el script para ejecutar SOLO esas pruebas
4. Incluir build/compile y linting si aplica

---

## Fase 6: Implementar parsing.py

1. Copiar la plantilla desde `templates/parsing_template.py`
2. Renombrar a `parsing.py`
3. Implementar `parse_test_output()` para el framework del repo
4. Probar localmente que genera el JSON correcto

---

## Fase 7: Crear la Rúbrica

1. Usar el generador LLM si está disponible (obtener criterios base)
2. **EDITAR EXHAUSTIVAMENTE** cada criterio generado:
   - ¿Es atómico? ¿Es self-contained? ¿Es objetivo?
   - ¿Ya lo verifica un script? → Eliminarlo
   - ¿Es demasiado específico al Golden Patch? → Generalizarlo
3. Ajustar cantidad: mínimo 15, máximo 20
4. Asignar pesos: solo 1, 3, o 5
5. Verificar formateo: presente, afirmativo, sin "The model..."
6. Verificar que el Golden Patch pasa TODOS con PASS
7. Consultar `guides/g4_rubric_guidelines.md` para referencia

---

## Fase 8: Validación Final

1. Organizar archivos:
   ```
   raíz/
   ├── e2e.sh
   └── app/
       ├── Dockerfile
       ├── golden.patch
       ├── parsing.py
       ├── run_script.sh
       └── reproduction_script.sh  (puede estar vacío para R/M)
   ```
2. Ejecutar `e2e.sh`
3. Verificar con `checklists/checklist_rm_task.md`
4. Confirmar: `before.json` y `after.json` idénticos, todo PASSED
5. ✅ **ENTREGAR**
