# Estado de la Tarea — Audio Fingerprint (Task ID: 69d82c44)

## Fecha inicio: 2026-04-11
## Deadline: 2026-04-11 06:31
## Fase Actual: FASE 1 ✅ COMPLETADA → FASE 2 — TDD (siguiente)

---

## Resumen General
Tarea: **Audio Fingerprinting & Matching Library**
Task ID: `69d82c4413b79ccd4d0ba380`
Tipo: Data Science | Python
Reemplaza: church-mgmt `69d691f7` (workspace viejo conservado)

---

## Hitos Completados

- [x] Workspace creado: `task-69d82c44-audio-fingerprint/`
- [x] TASK.md llenado con metadata completa
- [x] raw_description.txt guardado en fase-1-prompt/inputs/
- [x] logs inicializados (decisions, time-tracking, errors-fixed)
- [x] Estado registrado en Estatus-task/
- [x] **FASE 1 — Prompt estructurado escrito** → `fase-1-prompt/outputs/prompt.md`
  - Patrón: **Pattern B** (Current State en posición 6 — greenfield)
  - Tech Stack: Python 3.11 / numpy 1.26 / scipy 1.13 / soundfile 0.12 / sqlite3 stdlib
  - Requirements: **14 numerados, determinísticos, testeables**
  - Expected Interface: **6 componentes** con 6 campos cada uno
  - Promptchecker: **8/8 bloques PASS** — resultado en `codebase/promptchecker_resultado.md`
  - 1 WARNING aceptable: hash formula en Req 4 es over-specific pero viene del seed original

---

## Fases Pendientes

- [x] Fase 1 — Prompt estructurado ✅
- [ ] Fase 2 — TDD: tests que fallan en empty, pasan con golden patch
- [ ] Fase 3 — Expert rubric
- [ ] Fase 4 — Golden Patch: implementación completa en Python
- [ ] Fase 5 — Validación (before.json + after.json)
- [ ] Fase 6 — Submit

---

## Arquitectura de la Solución (Definida en Prompt)

```
audio_fingerprint/
├── __main__.py         # CLI: build / query / test subcommands
├── fingerprint.py      # STFT → peaks → hashes (fingerprint fn)
├── database.py         # build_database + query functions
├── matcher.py          # test_mode function
├── sample_data/        # WAV files generados por generate_samples.py
generate_samples.py     # crea ≥2 WAV sintéticos de ≥15s con numpy
tests/
└── test_*.py
```

## Interfaz Pública (Definida en Expected Interface)

| Componente | Path | Firma |
|---|---|---|
| `fingerprint` | `audio_fingerprint/fingerprint.py` | `(wav_path, threshold_factor=5.0, fan_out_time=10, window_size=4096, hop_length=2048) -> list[tuple[int,int]]` |
| `build_database` | `audio_fingerprint/database.py` | `(wav_dir, db_path) -> None` |
| `query` | `audio_fingerprint/database.py` | `(wav_path, db_path) -> tuple[str, int]` |
| `test_mode` | `audio_fingerprint/matcher.py` | `(wav_path, db_path) -> bool` |
| CLI | `audio_fingerprint/__main__.py` | subcommands: build / query / test |
| `generate_samples` | `generate_samples.py` | `(output_dir="sample_data") -> None` |

## Librerías Clave
- `numpy 1.26` — arrays, sine wave generation
- `scipy 1.13` — STFT via `scipy.signal.stft`, peak detection
- `sqlite3` — stdlib, sin dependencias externas
- `soundfile 0.12` — leer WAV files

---

## Notas Importantes
- NO live fetching — sample WAVs van en el codebase
- NO pedir al modelo que descargue datasets
- Test mode: segmento 10s aleatorio + ruido → debe identificar correctamente
- Confidence = count de hashes alineados por offset
