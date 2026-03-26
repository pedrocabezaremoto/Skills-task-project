# Checklist — Tarea R/M (Refactoring/Maintainability)

> Verificar TODOS los puntos antes de correr `e2e.sh` y entregar.

---

## 📋 Artefactos Requeridos

- [ ] **Dockerfile** creado
- [ ] **Prompt** escrito
- [ ] **Run Script** (`run_script.sh`) configurado
- [ ] **Parsing File** (`parsing.py`) implementado
- [ ] **Golden Patch** (`golden.patch`) creado
- [ ] **User-Facing Problem Description** escrita
- [ ] **Rúbrica** con 15-20 criterios

---

## 📋 Validación del Dockerfile

- [ ] Usa SHA del commit padre (NO branch name)
- [ ] Agnóstico a arquitectura (no x86_64, no AArch64)
- [ ] NO tiene COPY de: `run_script.sh`, `reproduction_script.sh`, `golden.patch`, `parsing.py`
- [ ] Instala TODAS las dependencias necesarias
- [ ] `WORKDIR /app` y `ENTRYPOINT ["/bin/bash"]` presentes
- [ ] Construye sin errores

---

## 📋 Validación del Prompt

- [ ] Sigue la plantilla: Context → Problem → Requirements → Success Criteria → Files → Notes
- [ ] Autocontenido (no necesita info externa)
- [ ] Sin pistas ni soluciones
- [ ] Sin referencias al PR, scripts, rúbricas o Golden Patch
- [ ] Sin segunda persona ("you")
- [ ] No solicita cambios que alteren funcionalidad observable

---

## 📋 Validación del Golden Patch

- [ ] Formato unified diff con extensión `.patch`
- [ ] Se aplica limpiamente sobre el commit del Dockerfile
- [ ] Solo cambios estrictamente necesarios
- [ ] Sigue mejores prácticas de codificación

---

## 📋 Validación del Run Script

- [ ] Solo ejecuta pruebas que YA PASABAN antes del parche
- [ ] Incluye build/compile si aplica
- [ ] Incluye linting si aplica

---

## 📋 Validación del Parsing

- [ ] Solo se modificó `parse_test_output()`
- [ ] Genera JSON con estructura correcta: `{"tests": [{"name": "...", "status": "..."}]}`

---

## 📋 Validación de la Rúbrica

- [ ] Tiene entre 15 y 20 criterios
- [ ] Criterios generados por LLM fueron editados exhaustivamente
- [ ] Cada criterio es atómico (1 idea)
- [ ] Cada criterio es self-contained
- [ ] No evalúa cosas que ya verifican los scripts
- [ ] Solo usa pesos 1, 3, o 5 (NUNCA 2 o 4)
- [ ] Escrito en presente, afirmativo, sin "The model..."
- [ ] Golden Patch pasa TODOS los criterios con PASS
- [ ] Sin criterios redundantes
- [ ] Evalúa cualquier solución correcta

---

## 📋 Validación E2E

- [ ] Archivos organizados: `e2e.sh` en raíz, todo en carpeta `app/`
- [ ] `e2e.sh` corre sin errores ni intervención manual
- [ ] `before.json` generado con todos los tests PASSED
- [ ] `after.json` generado con todos los tests PASSED
- [ ] `before.json` y `after.json` son idénticos en pruebas pasadas
