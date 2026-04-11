# Task Metadata

**Task ID:** 69d82c4413b79ccd4d0ba380
**Platform:** app.outlier.ai → Real Coder
**Rate:** $27/hr
**Deadline:** 2026-04-11 06:31 (extended +5min)
**Type:** Data Science
**Language:** Python
**Status:** 🔄 IN PROGRESS

## Brief Description
Build an audio fingerprinting and matching library in Python (Shazam-style, simplified).
STFT-based spectrogram → spectral peaks → hash pairs → SQLite DB → query matching by time-offset alignment.

## Key Requirements
- WAV input → STFT spectrogram → local maxima peaks → hash pairs (freq1, freq2, time_delta)
- SQLite DB storing hashes + time offsets keyed by hash value
- `db_builder`: fingerprint a directory of WAV files
- `query`: take a short WAV clip → return best match + confidence score
- `test_mode`: extract random 10s segment + add noise → verify system identifies it
- Must work with noisy clips and clips starting at different points

## Tech Stack
- Python (version: 3.10+)
- numpy, scipy (STFT, signal processing)
- sqlite3 (stdlib)
- NO live fetching — sample dataset included in codebase

## Timeline
- Start: 2026-04-11 ~00:30
- Phase 1 (Prompt): 
- Phase 2 (TDD): 
- Phase 3 (Rubrics): 
- Phase 4 (Golden Patch): 
- Phase 5 (Validation): 
- Phase 6 (Submit): 
- Submission: 

## Economic Result
- Tasking time: _h × $27/hr = $___
- Exceeded time: _h _min × $8.10/hr = $___
- **Total:** $___
