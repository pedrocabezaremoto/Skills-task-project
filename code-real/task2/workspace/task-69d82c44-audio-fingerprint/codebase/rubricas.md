# Rubrics — Audio Fingerprinting Library (Task 69d82c44)

> 30 criterios auditados contra rubricChecker.md y rubricndTestcoverage.md.
> Ninguno duplica cobertura de los unit tests (test_f2p.py).
> Pesos: 5 = Mandatory, 3 = Important, 1 = Nice to have.

---

## Category 1 — Instruction Following (7 criteria)

| ID  | Criterion | Weight |
|:----|:----------|:------:|
| IF1 | The `fingerprint` function loads WAV files using `scipy.io.wavfile.read` (verifiable by reading `fingerprint.py`). | 5 |
| IF2 | The STFT is computed using `scipy.signal.stft` (verifiable by reading `fingerprint.py`). | 5 |
| IF3 | The `audio_fingerprint/` directory contains a valid `__init__.py` file, making it a proper importable Python package. | 5 |
| IF4 | The CLI subcommands use exactly the flags specified: `build --dir --db`, `query --clip --db`, `test --file --db`. | 5 |
| IF5 | All configurable parameters (`window_size`, `hop_length`, `threshold_factor`, `fan_out_time`) are forwarded to the `scipy.signal.stft` call — not hardcoded inside the STFT invocation. | 5 |
| IF6 | The `generate_samples` function generates audio using only numpy and scipy — without external audio synthesis libraries. | 5 |
| IF7 | The CLI stdout output for a no-match result is exactly `"No match found"` — case-sensitive, no extra punctuation or trailing characters. | 5 |

---

## Category 2 — Code Correctness (11 criteria)

| ID  | Criterion | Weight |
|:----|:----------|:------:|
| CC1 | Stereo WAV files are converted to mono by computing the arithmetic mean across channels — not by selecting a single channel. | 3 |
| CC2 | Audio samples are normalized to float64 by dividing by the maximum absolute value of the source dtype (e.g., 32768.0 for int16). | 3 |
| CC3 | `mean_energy` in peak detection is the arithmetic mean of all magnitude values in the current time frame — not RMS, maximum, or median. | 5 |
| CC4 | The `time_offset` stored per hash tuple is the frame index of the anchor (first/earlier) peak in the pair — not the second peak. | 5 |
| CC5 | The `DELETE FROM fingerprints WHERE song_name = ?` statement uses a parameterized placeholder (`?`) — not string formatting or f-string interpolation. | 5 |
| CC6 | The `query` function groups hash matches using a composite key of both `song_name` AND `offset_diff` together — not by `song_name` alone. | 5 |
| CC7 | `offset_diff` is computed as `db_offset - clip_offset` (database offset minus query clip offset) — not the reverse. | 5 |
| CC8 | `test_mode` calls `np.random.seed(42)` before computing the random segment start position. | 5 |
| CC9 | The Gaussian noise amplitude in `test_mode` is computed using the 20 dB SNR relationship between signal RMS and noise RMS. | 3 |
| CC10 | No two chirp components within the same generated WAV file share the same start frequency. | 3 |
| CC11 | No two chirp components within the same generated WAV file share the same end frequency. | 3 |

---

## Category 3 — Code Quality (5 criteria)

| ID  | Criterion | Weight |
|:----|:----------|:------:|
| CQ1 | SQLite connections are managed with `with sqlite3.connect(...)` context manager or with explicit `.close()` calls after use. | 5 |
| CQ2 | The temporary WAV file in `test_mode` is reliably deleted after use even in error conditions — via `try/finally` or `NamedTemporaryFile` with proper cleanup semantics. | 5 |
| CQ3 | The implementation successfully avoids module-level mutable state — no module-level variables are written to during function execution. | 3 |
| CQ4 | All SQL statements across all modules use parameterized placeholders (`?`) for every dynamic value passed to the database. | 5 |
| CQ5 | The SQL lookup in `query` uses a `WHERE hash = ?` parameterized clause to match fingerprint hashes — not a full table iteration. | 5 |

---

## Category 4 — Code Clarity (5 criteria)

| ID  | Criterion | Weight |
|:----|:----------|:------:|
| CL1 | Each module has a single clearly scoped responsibility: signal processing in `fingerprint.py`, persistence in `database.py`, test logic in `matcher.py`, CLI routing in `__main__.py`. | 3 |
| CL2 | The hash bit-packing expression includes a comment or named constants documenting the 13-bit/13-bit/10-bit encoding layout. | 1 |
| CL3 | Variable names in the query matching logic clearly distinguish between `db_offset`, `clip_offset`, and `offset_diff`. | 3 |
| CL4 | The CLI argument parser includes `help=` description strings for each argument (`--dir`, `--db`, `--clip`, `--file`). | 1 |
| CL5 | The `generate_samples` function separates chirp parameter definition, signal synthesis, and file writing into distinct logical sections. | 1 |

---

## Category 5 — Code Efficiency (2 criteria)

| ID  | Criterion | Weight |
|:----|:----------|:------:|
| CE1 | The `build_database` function uses `executemany()` for inserting fingerprint rows in bulk — not calling `execute()` per individual row inside a loop. | 3 |
| CE2 | The STFT magnitude array is computed once per file and reused for both peak detection and hash generation — not recalculated separately for each step. | 3 |

---

## Audit Summary

| Check | Status |
|:------|:------:|
| Total criteria: 30 (min 5, max 30) | ✅ |
| All weights are 1, 3, or 5 | ✅ |
| All 5 categories covered | ✅ |
| No duplication with unit tests (test_f2p.py) | ✅ |
| All criteria use positive framing | ✅ |
| All criteria are atomic and self-contained | ✅ |

**rubricChecker result: PASS — ready for Outlier submission.**
