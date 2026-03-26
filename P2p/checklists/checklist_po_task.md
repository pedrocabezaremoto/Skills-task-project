# Checklist — Tarea PO (Performance Optimization)

> Verificar TODOS los puntos antes de correr `e2e.sh` y entregar.

---

## 📋 Artefactos Requeridos

- [ ] **Dockerfile** creado
- [ ] **Prompt** escrito
- [ ] **Run Script** (`run_script.sh`) configurado
- [ ] **Parsing File** (`parsing.py`) implementado
- [ ] **Golden Patch** (`golden.patch`) creado
- [ ] **User-Facing Problem Description** escrita
- [ ] **Target Functions** listadas (con ruta + clase + función)
- [ ] **Reproduction Script** (`reproduction_script.sh`) creado

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

---

## 📋 Validación del Golden Patch

- [ ] Formato unified diff con extensión `.patch`
- [ ] Se aplica limpiamente sobre el commit del Dockerfile
- [ ] Solo cambios estrictamente necesarios
- [ ] Optimiza el código de forma tangible y medible

---

## 📋 Validación del Run Script

- [ ] Solo ejecuta pruebas que YA PASABAN antes del parche
- [ ] Incluye build/compile si aplica

---

## 📋 Validación del Parsing

- [ ] Solo se modificó `parse_test_output()`
- [ ] Genera JSON con estructura correcta

---

## 📋 Validación del Reproduction Script

- [ ] Ejecuta el código REAL del repositorio (NO benchmarks simulados/dummies)
- [ ] Mide una métrica relevante (tiempo, memoria, latencia, ops/sec)
- [ ] Es determinista (seeds fijas, warm-up, mediana)
- [ ] Salida en formato exacto: `METRIC_VALUE: <número>`
- [ ] Muestra mejora tangible después de aplicar el Golden Patch

---

## 📋 Validación de Target Functions

- [ ] Funciones listadas con formato: `ruta/archivo::Clase::función`
- [ ] Son las funciones REALES donde está el cuello de botella
- [ ] Son las funciones que el Golden Patch optimiza

---

## 📋 Validación E2E

- [ ] Archivos organizados: `e2e.sh` en raíz, todo en carpeta `app/`
- [ ] `e2e.sh` corre sin errores ni intervención manual
- [ ] `before.json` generado con todos los tests PASSED
- [ ] `after.json` generado con todos los tests PASSED
- [ ] `reproduction_before_stdout.txt` generado
- [ ] `reproduction_after_stdout.txt` generado
- [ ] La métrica en `reproduction_after_stdout.txt` muestra mejora vs `reproduction_before_stdout.txt`
