# 🔄 CONTINUITY PROMPT — Audio Fingerprinting Task (TDD Baseline Ronda 2)

**Actúa como un Senior AI Coding Assistant asistiendo a Pedro en un task de Outlier Real Coder.**

---

## 🎯 CONTEXTO DEL PROYECTO

- **Task ID:** 69d82c44 — Audio Fingerprinting and Matching Library (tipo Shazam)
- **Plataforma:** Outlier Real Coder — $27/hr
- **Entorno:** Python 3.11/3.12, numpy 1.26, scipy 1.13, sqlite3, air-gapped (sin red)
- **Workspace:** `/root/skills-task-project/code-real/task2/workspace/task-69d82c44-audio-fingerprint/`
- **Repo GitHub:** `git@github.com:pedrocabezaremoto/Skills-task-project.git` (SSH, nunca HTTPS)

---

## ✅ LO QUE YA ESTÁ HECHO

### Fase 1 — Prompt Engineering
- `prompt.md` auditado y limpio, score 91/100

### Fase 2 — TDD Test Suite
- `codebase/tests/test_f2p.py` — 71 tests cubriendo 78 requerimientos atómicos al 100%

### Fase 3 — Baseline Run (Before)
- Stubs vacíos creados en `/tmp/baseline_run/`
- Resultado: **39 FAILED, 32 PASSED, 0 ERROR** ✅
- Archivos generados en `/app/`:
  - `before.json`, `before_stdout.txt`, `before_stderr.txt`
  - `after.json` (71 PASSED), `after_stdout.txt`, `after_stderr.txt`

### Fase 4 — Submission Outlier (EN PROGRESO)
- Campo 1 screenshot: ✅ subido
- Campo 2 before.json: ✅ subido
- Campo 3 unit tests: ✅ pegados
- **3/3 completed** pero con error de AI checker

---

## 🛑 BLOQUEADO AQUÍ — Overly Specific Tests

La interfaz de Outlier tiene un AI checker automático que rechaza tests demasiado específicos. Ya van **2 rondas de rechazo**.

### Ronda 1 rechazó:
1. `test_main_module_importable` → `assert hasattr(m, "main")` 
2. `test_req76_filesystem_io_only` → string matching con `open(` / `sqlite3`

### Ronda 2 rechazó (último estado):
1. `test_req49_invokable_as_module` → `assert callable(audio_fingerprint.__main__.main)`
2. `test_req78_no_forbidden_module_imports` → `assert f"import {bad}" not in src`

### Fixes ya aplicados en el archivo actual:
- `test_req49`: ahora usa `subprocess.run([sys.executable, "-m", "audio_fingerprint", "--help"])` — verifica invocabilidad sin asumir `main()`
- `test_req78`: ahora usa `ast.parse()` para detectar imports reales sin string matching

**El archivo actualizado está en:** `codebase/tests/test_f2p.py` (751 líneas)

---

## 🔜 LO QUE FALTA HACER

1. **Copiar el contenido de `test_f2p.py`** (actualizado) y reemplazarlo en el campo 3 de la interfaz Outlier
2. **Hacer Re-check** — si pasa → presionar Next
3. Si hay una **Ronda 3** de rechazos, corregir los tests señalados siguiendo la misma lógica:
   - Nunca usar string matching sobre source code
   - Nunca asumir nombres internos de funciones
   - Siempre testear COMPORTAMIENTO (inputs/outputs), no IMPLEMENTACIÓN
4. Una vez aprobado → continuar con la siguiente fase (Golden Patch Verification)

---

## 📂 Estructura del /app/ (ya lista)

```
app/
├── before.json          ✅ 39 FAILED, 32 PASSED
├── before_stdout.txt    ✅
├── before_stderr.txt    ✅
├── after.json           ✅ 71 PASSED, 0 FAILED
├── after_stdout.txt     ✅
├── after_stderr.txt     ✅
├── codebase.zip         ✅ golden patch
├── tests.zip            ✅ test suite
├── Dockerfile           ✅
├── run.sh               ✅
└── parsing.py           ✅
```

---

## ⚠️ REGLAS CRÍTICAS

- Git push **siempre vía SSH** (`git@github.com:...`), nunca HTTPS
- **NO modificar archivos existentes sin permiso explícito de Pedro**
- Los tests deben testear comportamiento, no implementación interna
- El checker de Outlier tiene **zero tolerance** con overly specific tests

---

## 🛑 INSTRUCCIÓN PARA EL AGENTE

**Tu única tarea por ahora es leer y asimilar este contexto.**
- **NO** realices ninguna acción de codificación
- **NO** modifiques archivos
- **NO** propongas mejoras ni planes todavía

**Confirma que entendiste y QUÉDATE A LA ESPERA DE LA ORDEN DIRECTA DE PEDRO.**
