# Audio Fingerprinting and Matching Library

## Context

A data engineer working with audio recordings needs a Python library that identifies short audio clips by comparing them against a database of known recordings. The system works conceptually like Shazam but is self-contained and simpler: it computes spectral fingerprints from WAV files, stores them in a local SQLite database, and matches unknown clips using temporal offset alignment. The library must handle clips that start at different positions within a recording and clips with added background noise.

---

## Tech Stack

- **Language:** Python 3.11
- **Signal Processing:** numpy 1.26, scipy 1.13 (STFT via `scipy.signal.stft`)
- **Database:** sqlite3 (Python standard library — no external ORM)
- **Audio I/O:** soundfile 0.12 (read WAV files — no external codec required)
- **Noise generation:** numpy.random (no external dependency)
- **Sample data:** WAV files MUST be included in the codebase under `sample_data/` — the system MUST NOT download datasets or access the internet at runtime

---

## Requirements

1. The `fingerprint(wav_path: str) -> list[tuple[int, int]]` function MUST load the WAV file at `wav_path` using soundfile, convert to mono if stereo, and compute a Short-Time Fourier Transform (STFT) using a window size of 4096 samples, hop length of 2048 samples, and a Hann window.
2. For each time frame in the STFT output, the system MUST detect spectral peaks by finding frequency bins whose magnitude exceeds `mean_energy * threshold_factor` where `threshold_factor` is a configurable parameter with default value `5.0`.
3. Peak detection MUST select local maxima only — a bin qualifies as a peak only if its magnitude is strictly greater than both its immediate left and right neighbors.
4. The system MUST generate fingerprint hashes from pairs of peaks within the same time frame or within a configurable `fan_out_time` window (default: 10 frames). Each hash MUST encode `(freq1, freq2, delta_time)` packed into a single integer using bit-shifting: `hash_val = (freq1 & 0x1FFF) << 23 | (freq2 & 0x1FFF) << 10 | (delta_time & 0x3FF)`.
5. The `fingerprint` function MUST return a list of `(hash_val, time_offset)` tuples where `time_offset` is the frame index of the first peak in the pair.
6. The `build_database(wav_dir: str, db_path: str) -> None` function MUST iterate over all `.wav` files in `wav_dir`, call `fingerprint()` on each, and insert every `(hash_val, time_offset, song_name)` triple into a SQLite table named `fingerprints`.
7. The SQLite `fingerprints` table MUST have columns: `hash INTEGER`, `offset INTEGER`, `song_name TEXT`. The table MUST be created if it does not exist. Duplicate rows are allowed.
8. The `query(wav_path: str, db_path: str) -> tuple[str, int]` function MUST fingerprint the input clip, look up each hash in the database, compute `offset_diff = db_offset - clip_offset` for each matching row, group results by `(song_name, offset_diff)`, and return the `(song_name, confidence)` pair with the highest confidence count.
9. If no matching hashes are found, `query` MUST return `("no_match", 0)`.
10. The `test_mode(wav_path: str, db_path: str) -> bool` function MUST load the WAV at `wav_path`, extract a random contiguous 10-second segment (selected with a fixed random seed of `42` for reproducibility), add Gaussian white noise with signal-to-noise ratio of 20 dB, write the noisy clip to a temporary WAV file, call `query()` on it, and return `True` if the returned song name matches the base name (without extension) of `wav_path`.
11. The `build_database` function MUST store `song_name` as the filename without path and without extension (e.g., `"sample_audio"` for `sample_data/sample_audio.wav`).
12. The library MUST expose a CLI entry point via `python -m audio_fingerprint` accepting three subcommands:
    - `build --dir <wav_dir> --db <db_path>` — calls `build_database`
    - `query --clip <wav_path> --db <db_path>` — prints `"Match: <song_name> (confidence: <N>)"` or `"No match found"`
    - `test --file <wav_path> --db <db_path>` — prints `"PASS"` if `test_mode` returns `True`, else `"FAIL"`
13. The codebase MUST include at least 2 sample WAV files under `sample_data/` with a minimum duration of 15 seconds each, generated programmatically (sine wave composition) so no external download is needed. A script `generate_samples.py` MUST create them when run.
14. All configurable parameters (`threshold_factor`, `fan_out_time`, STFT `window_size`, `hop_length`) MUST be keyword arguments with documented default values — they MUST NOT be hardcoded inside logic.

---

## Expected Interface

### Component 1
- **Path:** `audio_fingerprint/fingerprint.py`
- **Name:** `fingerprint`
- **Type:** function
- **Input:** `wav_path: str, threshold_factor: float = 5.0, fan_out_time: int = 10, window_size: int = 4096, hop_length: int = 2048`
- **Output:** `list[tuple[int, int]]` — list of `(hash_val, time_offset)` pairs; empty list if no peaks detected
- **Description:** Loads a WAV file, computes STFT, detects spectral peaks per frame, and generates integer hashes from peak pairs within the fan-out window. Returns all (hash, offset) pairs as the fingerprint of the recording.

### Component 2
- **Path:** `audio_fingerprint/database.py`
- **Name:** `build_database`
- **Type:** function
- **Input:** `wav_dir: str, db_path: str`
- **Output:** `None` — side effect: creates SQLite DB at `db_path` and populates `fingerprints` table
- **Description:** Iterates over all `.wav` files in `wav_dir`, fingerprints each one, and inserts `(hash_val, time_offset, song_name)` rows into the SQLite database. Creates the table if it does not exist.

### Component 3
- **Path:** `audio_fingerprint/database.py`
- **Name:** `query`
- **Type:** function
- **Input:** `wav_path: str, db_path: str`
- **Output:** `tuple[str, int]` — `(song_name, confidence)` where confidence is the count of aligned hashes; returns `("no_match", 0)` if no hashes match
- **Description:** Fingerprints the input clip, looks up each hash in the database, computes offset differences per (song, offset_diff) group, and returns the song with the highest alignment count as the match.

### Component 4
- **Path:** `audio_fingerprint/matcher.py`
- **Name:** `test_mode`
- **Type:** function
- **Input:** `wav_path: str, db_path: str`
- **Output:** `bool` — `True` if the noisy 10-second clip is correctly identified as the source recording, `False` otherwise
- **Description:** Extracts a random 10-second segment from the recording (seed=42), adds 20 dB SNR Gaussian noise, queries the database, and verifies the top match equals the source file's base name.

### Component 5
- **Path:** `audio_fingerprint/__main__.py`
- **Name:** CLI entry point
- **Type:** function (argparse-based module)
- **Input:** `sys.argv` — subcommands `build`, `query`, `test` with their respective flags
- **Output:** Prints to stdout: match result string for `query`, `"PASS"` or `"FAIL"` for `test`, confirmation message for `build`
- **Description:** Provides the command-line interface to the library. Routes `build`, `query`, and `test` subcommands to their respective library functions and formats output for human readability.

### Component 6
- **Path:** `generate_samples.py`
- **Name:** `generate_samples`
- **Type:** function (also executable as script)
- **Input:** `output_dir: str = "sample_data"` — directory where WAV files are written
- **Output:** `None` — side effect: writes at least 2 WAV files of ≥15 seconds using programmatically generated sine wave compositions at 44100 Hz sample rate
- **Description:** Creates synthetic WAV sample files using numpy sine wave generation so the codebase is self-contained. Called at setup time; no internet access required.

---

## Current State

This is a greenfield project. No existing codebase, database, or dependencies are present. Implement the complete library from scratch following the specifications above. Do not reference external audio datasets or APIs — all sample data MUST be generated programmatically.
