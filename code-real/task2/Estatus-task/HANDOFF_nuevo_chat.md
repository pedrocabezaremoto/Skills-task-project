# HANDOFF — Audio Fingerprint Task | Real Coder Outlier
## Para usar en nuevo chat como prompt de contexto inicial

---

Soy Pedro, trabajo como Real Coder en Outlier ($27/hr). Estoy trabajando en una tarea activa con deadline el **2026-04-11 a las 06:31**. Necesito asistencia en modo agente para completar las fases restantes.

## La Tarea

**Plataforma:** app.outlier.ai → Real Coder  
**Task ID:** `69d82c4413b79ccd4d0ba380`  
**Tipo:** Data Science | Python  
**Goal:** Construir una librería de audio fingerprinting en Python estilo Shazam (simplificado): toma WAVs, computa STFT, detecta peaks espectrales, genera hashes de pares de peaks, los guarda en SQLite, y hace matching por alineación de offset temporal.

## Lo que ya está hecho

- **Workspace:** `/root/skills-task-project/code-real/task2/workspace/task-69d82c44-audio-fingerprint/`
- **Fase 1 — Prompt ✅ COMPLETA** → archivo en `fase-1-prompt/outputs/prompt.md`
  - Pattern B, 14 requirements, 6 componentes en Expected Interface
  - Promptchecker: 8/8 PASS
  - El prompt ya fue pegado en Outlier y estamos en el siguiente turno

## Lo que falta (en orden)

### Fase 2 — TDD (F2P Tests)
Escribir tests en Python (`pytest`) que:
- **Fallan en codebase vacío** (no hay implementación)
- **Pasan con el Golden Patch** (implementación correcta)

Los tests cubren:
- `fingerprint()` → retorna lista de (hash_val, int) dado un WAV
- `build_database()` → crea SQLite con tabla `fingerprints`
- `query()` → retorna `(song_name, confidence)` con confidence > 0 para match correcto
- `query()` → retorna `("no_match", 0)` si no hay match
- `test_mode()` → retorna `True` con grabación conocida
- CLI `python -m audio_fingerprint build/query/test` funciona sin error

### Fase 3 — Expert Rubric
Criterios cualitativos que los tests no pueden cubrir:
- Calidad del código (legibilidad, modularidad)
- Instruction following (¿cumplió el prompt al pie de la letra?)
- Robustez (manejo de edge cases: WAV mono/estéreo, archivo corto, DB vacía)

### Fase 4 — Golden Patch
Implementación completa desde cero:
```
audio_fingerprint/
├── __main__.py
├── fingerprint.py    # STFT + peaks + hashes
├── database.py       # build_database + query
├── matcher.py        # test_mode
sample_data/          # WAVs sintéticos
generate_samples.py   # genera los WAVs con numpy
```

### Fase 5 — Validación
- Correr tests **antes** de aplicar Golden Patch → deben FALLAR → guardar como `before.json`
- Aplicar Golden Patch
- Correr tests **después** → deben PASAR → guardar como `after.json`

### Fase 6 — Submit
- Subir a Outlier en el campo correspondiente

## Archivos clave a leer antes de empezar

```
/root/skills-task-project/code-real/task2/workspace/task-69d82c44-audio-fingerprint/
├── TASK.md                              # metadata del task
├── fase-1-prompt/inputs/raw_description.txt   # descripción original del cliente
├── fase-1-prompt/outputs/prompt.md           # prompt escrito (Fase 1 ya entregada)
├── codebase/promptchecker_resultado.md        # QA del prompt (referencia)
└── logs/decisions.md                          # decisiones técnicas tomadas
/root/skills-task-project/code-real/task2/Estatus-task/estado_audio_fingerprint.md  # estado actual
```

## Reglas importantes

- **NO live fetching** — sample WAVs deben estar en el codebase, generados con numpy (sine waves)
- **NO pedir al modelo que descargue nada**
- Tech stack: Python 3.11 / numpy 1.26 / scipy 1.13 / soundfile 0.12 / sqlite3 stdlib
- Los tests deben usar `pytest` estándar
- Hash formula exacta: `hash_val = (freq1 & 0x1FFF) << 23 | (freq2 & 0x1FFF) << 10 | (delta_time & 0x3FF)`
- Confidence = count de hashes alineados por offset_diff
- `test_mode` usa seed=42, segmento de 10s, SNR=20dB

## Cómo trabajamos

- Te paso imágenes de Outlier cuando hay instrucciones nuevas
- Guardamos registros en `/root/skills-task-project/code-real/task2/Estatus-task/`
- Actualizamos `estado_audio_fingerprint.md` al completar cada fase
- Git push siempre por SSH (HTTPS falla en este VPS)
- Respuestas cortas y directas — no me expliques cosas obvias

**Siguiente acción: empezar Fase 2 — escribir los tests F2P.**  
Espera a que te pase screenshot de Outlier mostrando el turno de F2P Verification para ver si hay instrucciones adicionales.
