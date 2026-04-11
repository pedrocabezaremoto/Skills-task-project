# 🔄 CONTINUITY PROMPT — Audio Fingerprinting Task (Fase 6 — Submission Final)

**Actúa como un Senior AI Coding Assistant asistiendo a Pedro en un task de Outlier Real Coder.**

---

## 🎯 CONTEXTO DEL PROYECTO

- **Task ID:** 69d82c44 — Audio Fingerprinting and Matching Library (tipo Shazam)
- **Plataforma:** Outlier Real Coder — $27/hr
- **Deadline:** 2026-04-11 a las 10:47 a.m.
- **Entorno:** Python 3.11/3.12, numpy 1.26, scipy 1.13, sqlite3, air-gapped (sin red)
- **Workspace:** `/root/skills-task-project/code-real/task2/workspace/task-69d82c44-audio-fingerprint/`
- **Repo GitHub:** `git@github.com:pedrocabezaremoto/Skills-task-project.git` (SSH, nunca HTTPS)

---

## ✅ TODO LO QUE ESTÁ HECHO

### Fase 1 — Prompt Engineering ✅
- `codebase/prompt.md` auditado, score 91/100

### Fase 2 — TDD Test Suite ✅
- `codebase/tests/test_f2p.py` — 71 tests, 78 reqs cubiertos al 100%
- Aprobado tras 3 rondas de corrección del AI checker

### Fase 3 — Rubrics ✅
- `codebase/rubricas.md` — 30 criterios, 5 categorías, pesos 1/3/5
- Aprobado por Outlier

### Fase 4 — Golden Patch ✅
- Implementación completa en `codebase/audio_fingerprint/`
- **71/71 tests PASSING**

### Fase 5 — Validación ✅
- `codebase/after_stdout.txt` — output del run (71 PASSED)
- `codebase/after_stderr.txt` — stderr del run
- `codebase/after.json` — JSON generado por parsing.py
- `codebase/tests.zip` — ZIP con `tests/test_f2p.py`

---

## 🔵 FASE 6 — SUBMISSION (EN PROGRESO)

### Formulario Outlier — 5 campos:
1. Pegar `test_f2p.py` completo en el campo de texto
2. "Did you make sure tests are NOT overly specific?" → **Yes**
3. Subir screenshot de terminal mostrando **71 passed**
4. Subir screenshot del `after.json` (parsing results)
5. Subir `tests.zip` desde `codebase/tests.zip`

---

## 📂 Archivos para submission

| Archivo | Ruta completa |
|---------|---------------|
| test_f2p.py | `codebase/tests/test_f2p.py` |
| after.json | `codebase/after.json` |
| tests.zip | `codebase/tests.zip` |

---

## ⚠️ REGLAS CRÍTICAS

- Git push **siempre vía SSH** (`git@github.com:...`), nunca HTTPS
- **NO modificar archivos existentes sin permiso explícito de Pedro**
- `pytest-json-report` NO está instalado — usar `app/parsing.py` para JSONs
- Tests corren desde `codebase/` directory

---

## 🛑 INSTRUCCIÓN PARA EL AGENTE

**Confirma que entendiste y QUÉDATE A LA ESPERA DE LA ORDEN DIRECTA DE PEDRO.**
