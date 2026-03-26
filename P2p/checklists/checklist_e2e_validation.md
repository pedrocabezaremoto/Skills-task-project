# Checklist — Validación E2E (End-to-End Script)

> Checklist específico para la ejecución del script `e2e.sh`.

---

## 📋 Pre-Ejecución

- [ ] Script `e2e.sh` está en la raíz del directorio
- [ ] Carpeta `app/` existe en la raíz
- [ ] Dentro de `app/` están TODOS estos archivos:
  - [ ] `Dockerfile`
  - [ ] `golden.patch`
  - [ ] `parsing.py` (renombrado correctamente)
  - [ ] `run_script.sh`
  - [ ] `reproduction_script.sh` (solo PO)
- [ ] NO se ha modificado el script `e2e.sh`
- [ ] Docker daemon está corriendo

---

## 📋 Durante la Ejecución

- [ ] No se requiere NINGUNA intervención manual
- [ ] El Dockerfile construye la imagen sin errores
- [ ] El container se ejecuta correctamente
- [ ] `run_script.sh` ejecuta y todas las pruebas pasan (Pre-parche)
- [ ] `parsing.py` procesa la salida sin errores
- [ ] `golden.patch` se aplica limpiamente
- [ ] `run_script.sh` vuelve a ejecutar y las mismas pruebas siguen pasando (Post-parche)
- [ ] `parsing.py` procesa la nueva salida sin errores

---

## 📋 Post-Ejecución

- [ ] El script termina con mensaje **"OK"**
- [ ] `before.json` fue generado y copiado al directorio local
- [ ] `after.json` fue generado y copiado al directorio local
- [ ] Las pruebas en `before.json` y `after.json` son idénticas (todas PASSED)

### Solo para tareas PO:
- [ ] `reproduction_before_stdout.txt` fue generado
- [ ] `reproduction_after_stdout.txt` fue generado
- [ ] La métrica muestra mejora cuantificable

---

## 📋 Si el Script FALLA

1. **NUNCA** modificar `e2e.sh`
2. Revisar los archivos dentro de `app/`:
   - ¿El Dockerfile construye correctamente?
   - ¿El `run_script.sh` ejecuta las pruebas correctas?
   - ¿El `parsing.py` parsea correctamente la salida del framework?
   - ¿El `golden.patch` se aplica limpiamente?
3. Corregir nuestros archivos y volver a ejecutar `e2e.sh`
