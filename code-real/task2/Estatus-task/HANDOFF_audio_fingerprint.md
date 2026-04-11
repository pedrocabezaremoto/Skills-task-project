# HANDOFF - Audio Fingerprinting Library (Task 69d82c44)

## Contexto del Proyecto
Desarrollo de una librería de identificación de audio (tipo Shazam) en Python 3.11 que utiliza STFT, detección de picos espectrales y alineación temporal mediante SQLite.

## Estado Actual
- **Fase 1 (Prompt) ✅ COMPLETADA:** El prompt ha sido validado contra el checker de Outlier. Se encuentra en: `/root/skills-task-project/code-real/task2/workspace/task-69d82c44-audio-fingerprint/codebase/prompt.md`.
- **Fase 2 (TDD) 🟡 BASELINE LISTO:** Los stubs de la librería y los tests F2P (Fail-to-Pass) iniciales están creados en `codebase/audio_fingerprint/` y `codebase/tests/test_f2p.py`. Ya se validó que fallan contra el codebase vacío.
- **Fase 3 (Rubrics) 🔵 EN PROCESO:** Estamos creando y validando las rúbricas definitivas.

## Archivos Clave
- **Prompt Final:** `codebase/prompt.md`
- **Rúbrica Borrador:** `codebase/rubricas.md`
- **Auditores Copiados:** 
    - `codebase/rubricChecker.md` (Para auditar la calidad de la rúbrica).
    - `codebase/rubricndTestcoverage.md` (Para asegurar cobertura total prompt vs tests/rubric).
    - `codebase/promptchecker.md` (Referencia del checker de Phase 1).

## Instrucción para el nuevo chat
"Actúa como un experto en QA y Auditoría Técnica para Outlier. Estamos en la **Fase 3 (Rubrics)** del proyecto Audio Fingerprint (Task 69d82c44).

Tu tarea inmediata es:
1. Leer el `prompt.md` en `/root/skills-task-project/code-real/task2/workspace/task-69d82c44-audio-fingerprint/codebase/`.
2. Analizar el borrador de `rubricas.md` y auditarlo usando las reglas de `rubricChecker.md`.
3. Asegurar que cada requerimiento del prompt esté mapeado en la matriz `rubricndTestcoverage.md`.

**Detalles Críticos a mantener:**
- Air-gap estricto (no internet).
- Chirp-based synthetic samples.
- Bit-shift formula: `(freq1 & 0x1FFF) << 23 | (freq2 & 0x1FFF) << 10 | (delta_time & 0x3FF)`.
- SQLite Index: `idx_fingerprints_hash`.
"

## Estructura del Workspace (Referencia Screenshot)
El workspace está organizado con todos los validadores centralizados en la raíz de `codebase/` para facilitar el acceso en Cursor.
