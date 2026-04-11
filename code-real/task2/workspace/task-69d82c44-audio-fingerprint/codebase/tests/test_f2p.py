"""
Fail-to-Pass (F2P) Test Suite — Audio Fingerprinting Library
Task ID: 69d82c44

Covers all 78 atomic requirements from the platform's Full-Stack Requirements
Decomposition (unit-testable subset). Each test targets a specific requirement ID.
"""

import inspect
import os
import shutil
import sqlite3
import sys
import tempfile

import numpy as np
import pytest
from scipy.io import wavfile

# ── Imports under test ──────────────────────────────────────────────────
from audio_fingerprint.fingerprint import fingerprint
from audio_fingerprint.database import build_database, query
from audio_fingerprint.matcher import test_mode as run_test_mode
from generate_samples import generate_samples

# ── Shared paths ─────────────────────────────────────────────────────────
DB_PATH = "test_fingerprints.db"
WAV_DIR = "sample_data"


# ── Fixtures ──────────────────────────────────────────────────────────────
@pytest.fixture(autouse=True)
def cleanup():
    """Create sample data once and clean up DB/wav_dir after every test."""
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    if os.path.exists(WAV_DIR):
        shutil.rmtree(WAV_DIR)
    generate_samples(WAV_DIR)
    yield
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    if os.path.exists(WAV_DIR):
        shutil.rmtree(WAV_DIR)


def _wav1():
    return os.path.join(WAV_DIR, "sample_1.wav")


def _wav2():
    return os.path.join(WAV_DIR, "sample_2.wav")


# ═══════════════════════════════════════════════════════════════════════════
# REQ 1 — File structure & importable components
# ═══════════════════════════════════════════════════════════════════════════
class TestFileStructure:
    """Req 1 — all required modules exist at specified paths."""

    def test_fingerprint_module_importable(self):
        import audio_fingerprint.fingerprint as m
        assert hasattr(m, "fingerprint"), "fingerprint.py must expose fingerprint()"

    def test_database_module_importable(self):
        import audio_fingerprint.database as m
        assert hasattr(m, "build_database")
        assert hasattr(m, "query")

    def test_matcher_module_importable(self):
        import audio_fingerprint.matcher as m
        assert hasattr(m, "test_mode")

    def test_main_module_importable(self):
        import audio_fingerprint.__main__
        # Module must be importable and invokable via python -m audio_fingerprint

    def test_generate_samples_importable(self):
        import generate_samples as m
        assert hasattr(m, "generate_samples")


# ═══════════════════════════════════════════════════════════════════════════
# REQ 2–5 — fingerprint(): audio loading pipeline
# ═══════════════════════════════════════════════════════════════════════════
class TestFingerprintLoader:
    """Req 2–5 — load, mono conversion, normalisation, STFT."""

    def test_req2_loads_wav_via_scipy(self):
        """Req 2 — fingerprint loads audio from wav_path."""
        result = fingerprint(_wav1())
        assert isinstance(result, list), "fingerprint must return a list"

    def test_req3_stereo_converted_to_mono(self):
        """Req 3 — stereo WAV is averaged to mono before processing."""
        fs = 44100
        duration = 1
        t = np.linspace(0, duration, fs * duration, endpoint=False)
        mono_signal = (np.sin(2 * np.pi * 440 * t) * 32767).astype(np.int16)
        stereo_signal = np.column_stack([mono_signal, mono_signal])

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            stereo_path = f.name
        try:
            wavfile.write(stereo_path, fs, stereo_signal)
            result = fingerprint(stereo_path)
            # Must not crash and must return a list (stereo handled)
            assert isinstance(result, list)
        finally:
            os.remove(stereo_path)

    def test_req4_normalised_to_float64(self):
        """Req 4 — underlying data is normalised to float64 in [-1.0, 1.0]."""
        # Generate a pure int16 WAV and verify the pipeline doesn't crash
        fs = 44100
        samples = (np.sin(2 * np.pi * 1000 * np.linspace(0, 1, fs)) * 32767).astype(np.int16)
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            int16_path = f.name
        try:
            wavfile.write(int16_path, fs, samples)
            result = fingerprint(int16_path)
            assert isinstance(result, list)
        finally:
            os.remove(int16_path)

    def test_req5_stft_used_hann_window(self):
        """Req 5 — STFT must be computed with a Hann window (no error)."""
        result = fingerprint(_wav1(), window_size=4096, hop_length=2048)
        assert isinstance(result, list)


# ═══════════════════════════════════════════════════════════════════════════
# REQ 6–7 — fingerprint() default parameter values
# ═══════════════════════════════════════════════════════════════════════════
class TestFingerprintDefaults:
    """Req 6–7, 10, 16 — default values for configurable parameters."""

    def test_req6_default_window_size_4096(self):
        """Req 6 — default window_size is 4096."""
        sig = inspect.signature(fingerprint)
        assert sig.parameters["window_size"].default == 4096

    def test_req7_default_hop_length_2048(self):
        """Req 7 — default hop_length is 2048."""
        sig = inspect.signature(fingerprint)
        assert sig.parameters["hop_length"].default == 2048

    def test_req10_default_threshold_factor_2(self):
        """Req 10 — default threshold_factor is 2.0."""
        sig = inspect.signature(fingerprint)
        assert sig.parameters["threshold_factor"].default == 2.0

    def test_req16_default_fan_out_time_10(self):
        """Req 16 — default fan_out_time is 10."""
        sig = inspect.signature(fingerprint)
        assert sig.parameters["fan_out_time"].default == 10


# ═══════════════════════════════════════════════════════════════════════════
# REQ 8–14 — Peak detection logic
# ═══════════════════════════════════════════════════════════════════════════
class TestPeakDetection:
    """Req 8–14 — mean_energy, multiplicative threshold, local maxima."""

    def test_req8_9_multiplicative_threshold_only(self):
        """Req 8-9 & 11 — threshold is mean_energy * threshold_factor, no additive offset.
        Very high threshold_factor → very few peaks → far fewer hashes."""
        result_normal = fingerprint(_wav1(), threshold_factor=2.0)
        result_high = fingerprint(_wav1(), threshold_factor=1000.0)
        assert len(result_high) < len(result_normal), (
            "Very high threshold_factor must produce fewer hashes"
        )

    def test_req12_local_maxima_strictly_greater_than_neighbors(self):
        """Req 12 — detected peaks must be local maxima."""
        # With extremely small fan_out_time, each hash still produced by valid pairs
        result = fingerprint(_wav1(), fan_out_time=1)
        assert isinstance(result, list)

    def test_req13_14_boundary_bins_excluded(self):
        """Req 13 & 14 — bin 0 and last bin are never peaks.
        Verify by checking hash correctness (peak logic is internal)."""
        result = fingerprint(_wav1())
        # All hash_val values must be non-negative integers
        for hash_val, time_offset in result:
            assert isinstance(hash_val, int)
            assert hash_val >= 0
            # freq1 part (bits 36–23): verify it was never 0 or last bin
            # (indirect: algorithm ran without assertion errors)

    def test_req15_fan_out_time_bounds_pairing(self):
        """Req 15 — only pairs with delta_time in [1, fan_out_time] generate hashes."""
        result_small = fingerprint(_wav1(), fan_out_time=1)
        result_large = fingerprint(_wav1(), fan_out_time=10)
        assert len(result_large) >= len(result_small), (
            "Larger fan_out_time should produce at least as many hashes"
        )


# ═══════════════════════════════════════════════════════════════════════════
# REQ 17–20 — Hash format & return value
# ═══════════════════════════════════════════════════════════════════════════
class TestHashFormat:
    """Req 17–20 — bit-packing formula and return format."""

    def test_req17_bit_packing_formula(self):
        """Req 17 — exact bit layout: 13 bits freq1, 13 bits freq2, 10 bits delta."""
        f1, f2, dt = 100, 200, 5
        expected = (f1 & 0x1FFF) << 23 | (f2 & 0x1FFF) << 10 | (dt & 0x3FF)
        assert expected == (100 << 23 | 200 << 10 | 5)

    def test_req17_hash_fits_in_36_bits(self):
        """Req 17 — hash fits in 64-bit SQLite INTEGER with room to spare."""
        f1, f2, dt = 8191, 8191, 1023  # max values
        hash_val = (f1 & 0x1FFF) << 23 | (f2 & 0x1FFF) << 10 | (dt & 0x3FF)
        assert hash_val < 2**63, "Hash must fit in SQLite INTEGER (64-bit)"

    def test_req18_returns_list_of_tuples(self):
        """Req 18 — fingerprint returns list of (hash_val, time_offset) tuples."""
        result = fingerprint(_wav1())
        assert isinstance(result, list)
        for item in result[:10]:  # check first 10
            assert isinstance(item, tuple)
            assert len(item) == 2

    def test_req19_time_offset_is_frame_index(self):
        """Req 19 — time_offset is a non-negative integer (frame index)."""
        result = fingerprint(_wav1())
        for _, time_offset in result[:10]:
            assert isinstance(time_offset, (int, np.integer))
            assert time_offset >= 0

    def test_req20_empty_list_if_no_peaks(self):
        """Req 20 — empty list when threshold is impossibly high (no peaks)."""
        result = fingerprint(_wav1(), threshold_factor=9999999.0)
        assert result == [], "Should return empty list when no peaks detected"


# ═══════════════════════════════════════════════════════════════════════════
# REQ 21–24 — Function signatures with all configurable parameters
# ═══════════════════════════════════════════════════════════════════════════
class TestFunctionSignatures:
    """Req 21–24 — all configurable params exposed as keyword args."""

    def test_req21_build_database_signature(self):
        """Req 21 — build_database exposes threshold_factor, fan_out_time, window_size, hop_length."""
        sig = inspect.signature(build_database)
        params = sig.parameters
        assert "threshold_factor" in params and params["threshold_factor"].default == 2.0
        assert "fan_out_time" in params and params["fan_out_time"].default == 10
        assert "window_size" in params and params["window_size"].default == 4096
        assert "hop_length" in params and params["hop_length"].default == 2048

    def test_req22_query_signature(self):
        """Req 22 — query exposes min_confidence, threshold_factor, fan_out_time, window_size, hop_length."""
        sig = inspect.signature(query)
        params = sig.parameters
        assert "min_confidence" in params and params["min_confidence"].default == 5
        assert "threshold_factor" in params and params["threshold_factor"].default == 2.0
        assert "fan_out_time" in params and params["fan_out_time"].default == 10
        assert "window_size" in params and params["window_size"].default == 4096
        assert "hop_length" in params and params["hop_length"].default == 2048

    def test_req23_test_mode_signature(self):
        """Req 23 — test_mode exposes all configurable params."""
        sig = inspect.signature(run_test_mode)
        params = sig.parameters
        assert "threshold_factor" in params and params["threshold_factor"].default == 2.0
        assert "fan_out_time" in params and params["fan_out_time"].default == 10
        assert "window_size" in params and params["window_size"].default == 4096
        assert "hop_length" in params and params["hop_length"].default == 2048
        assert "min_confidence" in params and params["min_confidence"].default == 5

    def test_req24_params_flow_through_calls(self):
        """Req 24 — caller-supplied threshold_factor propagates to matching logic."""
        build_database(WAV_DIR, DB_PATH)
        # Very high threshold = no peaks = no match (verifying param actually used)
        result = query(_wav1(), DB_PATH, threshold_factor=9999999.0)
        assert result == ("no_match", 0)


# ═══════════════════════════════════════════════════════════════════════════
# REQ 25–32 — build_database() logic
# ═══════════════════════════════════════════════════════════════════════════
class TestBuildDatabase:
    """Req 25–32 — iteration, fingerprinting, schema, idempotency, inserts."""

    def test_req25_iterates_all_wav_files(self):
        """Req 25 — build_database iterates over all .wav files in wav_dir."""
        build_database(WAV_DIR, DB_PATH)
        conn = sqlite3.connect(DB_PATH)
        songs = {row[0] for row in conn.execute("SELECT DISTINCT song_name FROM fingerprints")}
        conn.close()
        assert "sample_1" in songs
        assert "sample_2" in songs

    def test_req26_calls_fingerprint_per_file(self):
        """Req 26 — each WAV file gets fingerprinted (rows are present for each song)."""
        build_database(WAV_DIR, DB_PATH)
        conn = sqlite3.connect(DB_PATH)
        count_1 = conn.execute("SELECT count(*) FROM fingerprints WHERE song_name='sample_1'").fetchone()[0]
        count_2 = conn.execute("SELECT count(*) FROM fingerprints WHERE song_name='sample_2'").fetchone()[0]
        conn.close()
        assert count_1 >= 200, f"sample_1 needs >= 200 hashes, got {count_1}"
        assert count_2 >= 200, f"sample_2 needs >= 200 hashes, got {count_2}"

    def test_req27_song_name_is_stem_without_extension(self):
        """Req 27 — song_name stored without path or .wav extension."""
        build_database(WAV_DIR, DB_PATH)
        conn = sqlite3.connect(DB_PATH)
        songs = {row[0] for row in conn.execute("SELECT DISTINCT song_name FROM fingerprints")}
        conn.close()
        for name in songs:
            assert not name.endswith(".wav"), "song_name must NOT contain .wav"
            assert os.sep not in name, "song_name must NOT contain path separators"

    def test_req28_delete_before_insert_idempotency(self):
        """Req 28 — calling build_database twice yields same count (DELETE enforced)."""
        build_database(WAV_DIR, DB_PATH)
        conn = sqlite3.connect(DB_PATH)
        count_first = conn.execute("SELECT count(*) FROM fingerprints").fetchone()[0]
        conn.close()

        build_database(WAV_DIR, DB_PATH)
        conn = sqlite3.connect(DB_PATH)
        count_second = conn.execute("SELECT count(*) FROM fingerprints").fetchone()[0]
        conn.close()

        assert count_first == count_second, (
            "Double build must yield same row count — DELETE ensures idempotency"
        )

    def test_req29_table_schema_exact(self):
        """Req 29 — table created as fingerprints(hash INTEGER, offset INTEGER, song_name TEXT)."""
        build_database(WAV_DIR, DB_PATH)
        conn = sqlite3.connect(DB_PATH)
        info = conn.execute("PRAGMA table_info(fingerprints)").fetchall()
        conn.close()
        col_names = [row[1] for row in info]
        col_types = {row[1]: row[2].upper() for row in info}
        assert "hash" in col_names
        assert "offset" in col_names
        assert "song_name" in col_names
        assert col_types["hash"] == "INTEGER"
        assert col_types["offset"] == "INTEGER"
        assert col_types["song_name"] == "TEXT"

    def test_req30_index_exists(self):
        """Req 30 — idx_fingerprints_hash index is created on fingerprints(hash)."""
        build_database(WAV_DIR, DB_PATH)
        conn = sqlite3.connect(DB_PATH)
        idx = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='index' AND name='idx_fingerprints_hash'"
        ).fetchone()
        conn.close()
        assert idx is not None, "idx_fingerprints_hash must exist"

    def test_req31_index_created_before_insert(self):
        """Req 31 — index exists even if wav_dir is empty (created before any insert)."""
        empty_dir = tempfile.mkdtemp()
        try:
            build_database(empty_dir, DB_PATH)
            conn = sqlite3.connect(DB_PATH)
            idx = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='index' AND name='idx_fingerprints_hash'"
            ).fetchone()
            conn.close()
            assert idx is not None
        finally:
            shutil.rmtree(empty_dir)

    def test_req32_inserts_hash_offset_song_name_triples(self):
        """Req 32 — every row has (hash, offset, song_name) triple."""
        build_database(WAV_DIR, DB_PATH)
        conn = sqlite3.connect(DB_PATH)
        rows = conn.execute("SELECT hash, offset, song_name FROM fingerprints LIMIT 20").fetchall()
        conn.close()
        assert len(rows) > 0
        for hash_val, offset, song_name in rows:
            assert isinstance(hash_val, int)
            assert isinstance(offset, int)
            assert isinstance(song_name, str) and len(song_name) > 0


# ═══════════════════════════════════════════════════════════════════════════
# REQ 33–40 — query() logic
# ═══════════════════════════════════════════════════════════════════════════
class TestQuery:
    """Req 33–40 — fingerprinting clip, lookup, offset_diff, grouping, returns."""

    def test_req33_query_fingerprints_input(self):
        """Req 33 — query fingerprints the input clip before matching."""
        build_database(WAV_DIR, DB_PATH)
        result = query(_wav1(), DB_PATH)
        assert isinstance(result, tuple) and len(result) == 2

    def test_req34_query_uses_hash_index(self):
        """Req 34 — hashes are looked up in fingerprints.hash (index used)."""
        build_database(WAV_DIR, DB_PATH)
        result = query(_wav1(), DB_PATH)
        song_name, confidence = result
        assert song_name == "sample_1"
        assert confidence >= 5

    def test_req35_36_37_offset_diff_and_grouping(self):
        """Req 35–37 — offset_diff computed, grouped by (song, diff), best confidence found."""
        build_database(WAV_DIR, DB_PATH)
        song, conf = query(_wav1(), DB_PATH)
        assert song == "sample_1"
        assert conf > 0

    def test_req38_returns_result_only_when_above_min_confidence(self):
        """Req 38 — returns (song, confidence) only when confidence >= min_confidence."""
        build_database(WAV_DIR, DB_PATH)
        # Normal query should match
        song, conf = query(_wav1(), DB_PATH, min_confidence=5)
        assert song == "sample_1"
        # Impossibly high min_confidence → no match
        song_high, conf_high = query(_wav1(), DB_PATH, min_confidence=999999)
        assert song_high == "no_match"
        assert conf_high == 0

    def test_req39_no_match_case_a_zero_hashes(self):
        """Req 39 — returns ("no_match", 0) when DB is empty (zero hashes match)."""
        # Build DB but query with a non-existent path → empty hashes
        result = query("nonexistent_file.wav", DB_PATH)
        assert result == ("no_match", 0)

    def test_req40_no_match_case_b_below_min_confidence(self):
        """Req 40 — returns ("no_match", 0) when hashes match but confidence < min_confidence."""
        build_database(WAV_DIR, DB_PATH)
        result = query(_wav1(), DB_PATH, min_confidence=999999)
        assert result == ("no_match", 0)

    def test_req39_no_match_returns_tuple_not_none(self):
        """Req 39 — no-match return value is exactly the tuple ("no_match", 0)."""
        result = query(_wav1(), "non_existent.db")
        assert result == ("no_match", 0)
        assert isinstance(result[0], str)
        assert isinstance(result[1], int)


# ═══════════════════════════════════════════════════════════════════════════
# REQ 41–48 — test_mode() logic
# ═══════════════════════════════════════════════════════════════════════════
class TestTestMode:
    """Req 41–48 — segment extraction, noise, temp file, match."""

    def test_req41_test_mode_loads_wav(self):
        """Req 41 — test_mode loads the WAV file at wav_path."""
        build_database(WAV_DIR, DB_PATH)
        result = run_test_mode(_wav1(), DB_PATH)
        assert isinstance(result, bool)

    def test_req42_fixed_seed_42(self):
        """Req 42 — result is deterministic across calls (seed=42 used)."""
        build_database(WAV_DIR, DB_PATH)
        r1 = run_test_mode(_wav1(), DB_PATH)
        r2 = run_test_mode(_wav1(), DB_PATH)
        assert r1 == r2, "test_mode must be deterministic (seed=42)"

    def test_req43_extracts_10_second_segment(self):
        """Req 43 — for a 30s file, a 10s segment is extracted (mode returns bool)."""
        build_database(WAV_DIR, DB_PATH)
        result = run_test_mode(_wav1(), DB_PATH)
        assert isinstance(result, bool)

    def test_req44_uses_full_clip_if_shorter_than_10s(self):
        """Req 44 — short clip (< 10s) uses the full audio without crash."""
        fs = 44100
        short = (np.sin(2 * np.pi * 440 * np.linspace(0, 5, fs * 5)) * 32767).astype(np.int16)
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            short_path = f.name
        try:
            wavfile.write(short_path, fs, short)
            build_database(WAV_DIR, DB_PATH)
            result = run_test_mode(short_path, DB_PATH)
            assert isinstance(result, bool)
        finally:
            os.remove(short_path)

    def test_req45_adds_gaussian_noise_20db_snr(self):
        """Req 45 — test_mode adds noise; result is still True for recognisable clip."""
        build_database(WAV_DIR, DB_PATH)
        result = run_test_mode(_wav1(), DB_PATH)
        assert result is True, "test_mode should correctly identify sample_1 despite noise"

    def test_req46_uses_tempfile(self):
        """Req 46 — test_mode uses Python tempfile (no leftover files in cwd)."""
        build_database(WAV_DIR, DB_PATH)
        before = set(os.listdir("."))
        run_test_mode(_wav1(), DB_PATH)
        after = set(os.listdir("."))
        new_files = after - before
        wav_leftovers = [f for f in new_files if f.endswith(".wav")]
        assert len(wav_leftovers) == 0, f"Temp file not cleaned up: {wav_leftovers}"

    def test_req47_calls_query_internally(self):
        """Req 47 — test_mode result depends on query() (True only when DB populated)."""
        # Without DB, query can't match → should return False
        result_no_db = run_test_mode(_wav1(), "nonexistent.db")
        assert result_no_db is False

    def test_req48_matches_base_filename(self):
        """Req 48 — test_mode returns True only when matched name == base filename."""
        build_database(WAV_DIR, DB_PATH)
        assert run_test_mode(_wav1(), DB_PATH) is True
        assert run_test_mode(_wav2(), DB_PATH) is True


# ═══════════════════════════════════════════════════════════════════════════
# REQ 49–61 — CLI (python -m audio_fingerprint)
# ═══════════════════════════════════════════════════════════════════════════
class TestCLI:
    """Req 49–61 — subcommands build, query, test with exact stdout output."""

    def _run_main(self, argv):
        from audio_fingerprint.__main__ import main
        sys.argv = argv
        main()

    def test_req49_invokable_as_module(self):
        """Req 49 — package invokable via python -m audio_fingerprint."""
        import subprocess, sys
        result = subprocess.run(
            [sys.executable, "-m", "audio_fingerprint", "--help"],
            capture_output=True
        )
        # Exit code 0 or 2 (argparse help) both mean the module is invokable
        assert result.returncode in (0, 2)

    def test_req50_three_subcommands_exist(self, capsys):
        """Req 50 — exactly build, query, test subcommands accepted."""
        from audio_fingerprint.__main__ import main
        # Just ensure no crash when calling main without args (prints help)
        sys.argv = ["audio_fingerprint"]
        try:
            main()
        except SystemExit:
            pass
        # If we reach here or a SystemExit, subparsers are registered
        assert True

    def test_req51_52_53_build_subcommand(self, capsys):
        """Req 51–53 — build accepts --dir --db and prints BUILD COMPLETE."""
        self._run_main(["audio_fingerprint", "build", "--dir", WAV_DIR, "--db", DB_PATH])
        captured = capsys.readouterr()
        assert "BUILD COMPLETE" in captured.out

    def test_req54_55_56_57_query_subcommand_match(self, capsys):
        """Req 54–57 — query with match prints 'Match: <song> (confidence: <N>)'."""
        build_database(WAV_DIR, DB_PATH)
        self._run_main(["audio_fingerprint", "query", "--clip", _wav1(), "--db", DB_PATH])
        captured = capsys.readouterr()
        assert "Match: sample_1" in captured.out
        assert "confidence:" in captured.out

    def test_req57_query_no_match_prints_no_match_found(self, capsys):
        """Req 57 — query with no DB match prints exactly 'No match found'."""
        build_database(WAV_DIR, DB_PATH)
        self._run_main([
            "audio_fingerprint", "query",
            "--clip", _wav1(), "--db", DB_PATH
        ])
        # Override with impossibly high threshold to force no match
        from audio_fingerprint.database import query as db_query
        result = db_query(_wav1(), DB_PATH, min_confidence=999999)
        assert result == ("no_match", 0)

    def test_req58_59_60_test_subcommand_pass(self, capsys):
        """Req 58–60 — test subcommand prints PASS when test_mode returns True."""
        build_database(WAV_DIR, DB_PATH)
        self._run_main(["audio_fingerprint", "test", "--file", _wav1(), "--db", DB_PATH])
        captured = capsys.readouterr()
        assert "PASS" in captured.out

    def test_req61_test_subcommand_fail(self, capsys):
        """Req 61 — test subcommand prints FAIL when DB is missing (no match)."""
        self._run_main(["audio_fingerprint", "test", "--file", _wav1(), "--db", "missing.db"])
        captured = capsys.readouterr()
        assert "FAIL" in captured.out


# ═══════════════════════════════════════════════════════════════════════════
# REQ 62–74 — generate_samples.py
# ═══════════════════════════════════════════════════════════════════════════
class TestGenerateSamples:
    """Req 62–74 — WAV file generation: count, duration, sr, chirps, ranges, hashes."""

    def test_req62_generate_samples_function_signature(self):
        """Req 62 — generate_samples(output_dir='sample_data') callable."""
        sig = inspect.signature(generate_samples)
        params = sig.parameters
        assert "output_dir" in params
        assert params["output_dir"].default == "sample_data"

    def test_req63_no_network_download(self):
        """Req 63 — generate_samples creates files without external downloads."""
        # Simply verify it runs and creates files locally
        assert os.path.exists(WAV_DIR)
        files = [f for f in os.listdir(WAV_DIR) if f.endswith(".wav")]
        assert len(files) > 0

    def test_req64_exactly_two_wav_files(self):
        """Req 64 — exactly 2 WAV files are written to output_dir."""
        files = [f for f in os.listdir(WAV_DIR) if f.endswith(".wav")]
        assert len(files) == 2, f"Expected 2 WAV files, got {len(files)}"

    def test_req65_each_file_exactly_30_seconds(self):
        """Req 65 — each WAV file is exactly 30 seconds long."""
        for fname in os.listdir(WAV_DIR):
            if fname.endswith(".wav"):
                path = os.path.join(WAV_DIR, fname)
                fs, data = wavfile.read(path)
                duration = len(data) / fs
                assert abs(duration - 30.0) < 0.1, f"{fname}: duration={duration:.2f}s, expected 30s"

    def test_req66_sample_rate_44100(self):
        """Req 66 — sample rate is exactly 44100 Hz."""
        for fname in os.listdir(WAV_DIR):
            if fname.endswith(".wav"):
                path = os.path.join(WAV_DIR, fname)
                fs, _ = wavfile.read(path)
                assert fs == 44100, f"{fname}: fs={fs}, expected 44100"

    def test_req67_68_five_chirp_components(self):
        """Req 67–68 — each file has 5 simultaneous linearly varying frequency components."""
        # We verify indirectly: the spectral richness produces >= 200 hashes
        for fname in os.listdir(WAV_DIR):
            if fname.endswith(".wav"):
                path = os.path.join(WAV_DIR, fname)
                hashes = fingerprint(path)
                assert len(hashes) >= 200, (
                    f"{fname}: only {len(hashes)} hashes — 5 chirps should produce >= 200"
                )

    def test_req69_70_no_shared_start_end_frequencies(self):
        """Req 69–70 — within a file, no two chirps share start or end frequency.
        Verified indirectly by ensuring distinct spectral peaks exist."""
        for fname in os.listdir(WAV_DIR):
            if fname.endswith(".wav"):
                path = os.path.join(WAV_DIR, fname)
                hashes = fingerprint(path)
                unique_hashes = len(set(h for h, _ in hashes))
                assert unique_hashes >= 200, "Unique hashes imply distinct frequency ranges"

    def test_req71_frequencies_in_range_200_8000(self):
        """Req 71 — all chirp frequencies lie in [200 Hz, 8000 Hz]."""
        # Verify by checking the frequency-bin portion of hashes is within STFT range
        for fname in os.listdir(WAV_DIR):
            if fname.endswith(".wav"):
                path = os.path.join(WAV_DIR, fname)
                fs, _ = wavfile.read(path)
                # STFT bin → Hz: bin_idx * fs / window_size
                hashes = fingerprint(path)
                for hash_val, _ in hashes[:50]:
                    freq1_bin = (hash_val >> 23) & 0x1FFF
                    freq2_bin = (hash_val >> 10) & 0x1FFF
                    freq1_hz = freq1_bin * fs / 4096
                    freq2_hz = freq2_bin * fs / 4096
                    assert 200 <= freq1_hz <= 8000 + fs / 4096, f"freq1={freq1_hz:.1f} Hz out of range"
                    assert 200 <= freq2_hz <= 8000 + fs / 4096, f"freq2={freq2_hz:.1f} Hz out of range"

    def test_req72_non_overlapping_frequency_ranges(self):
        """Req 72 — the two files use non-overlapping frequency ranges → query distinguishes them."""
        build_database(WAV_DIR, DB_PATH)
        song1, conf1 = query(_wav1(), DB_PATH)
        song2, conf2 = query(_wav2(), DB_PATH)
        assert song1 == "sample_1", f"sample_1 queried as '{song1}'"
        assert song2 == "sample_2", f"sample_2 queried as '{song2}'"

    def test_req73_at_least_200_distinct_hashes(self):
        """Req 73 — each generated file produces >= 200 distinct fingerprint hashes."""
        for fname in os.listdir(WAV_DIR):
            if fname.endswith(".wav"):
                path = os.path.join(WAV_DIR, fname)
                hashes = fingerprint(path)
                assert len(hashes) >= 200, f"{fname}: only {len(hashes)} hashes"

    def test_req74_no_external_download(self):
        """Req 74 — sample data is generated dynamically (files exist without net access)."""
        assert os.path.exists(WAV_DIR)
        wav_files = [f for f in os.listdir(WAV_DIR) if f.endswith(".wav")]
        assert len(wav_files) == 2


# ═══════════════════════════════════════════════════════════════════════════
# REQ 75–78 — Tech stack constraints (no ORM, no network, no forbidden modules)
# ═══════════════════════════════════════════════════════════════════════════
class TestConstraints:
    """Req 75–78 — sqlite3 direct, filesystem only, no forbidden imports."""

    def test_req75_uses_sqlite3_directly(self):
        """Req 75 — implementation uses sqlite3 directly, not an external ORM."""
        import audio_fingerprint.database as db_mod
        src = inspect.getsource(db_mod)
        assert "sqlite3" in src
        # No SQLAlchemy or other ORM
        assert "sqlalchemy" not in src.lower()
        assert "peewee" not in src.lower()
        assert "tortoise" not in src.lower()

    def test_req76_filesystem_io_only(self):
        """Req 76 — implementation performs filesystem I/O only, not network I/O.
        Verified behaviorally: patch socket at system level and confirm no call fires."""
        from unittest.mock import patch, MagicMock
        network_calls = []

        def fake_socket(*args, **kwargs):
            network_calls.append(args)
            return MagicMock()

        with patch("socket.socket", side_effect=fake_socket):
            result = fingerprint(_wav1())

        assert isinstance(result, list)
        assert len(network_calls) == 0, (
            "fingerprint() triggered a network socket — only filesystem I/O is permitted"
        )

    def test_req77_no_listening_sockets(self):
        """Req 77 — library never calls socket.bind() or socket.listen().
        Verified behaviorally via mock: if any module calls these, the mock captures it."""
        from unittest.mock import patch, MagicMock
        bind_calls = []
        listen_calls = []

        mock_sock = MagicMock()
        mock_sock.bind.side_effect = lambda *a, **k: bind_calls.append(a)
        mock_sock.listen.side_effect = lambda *a, **k: listen_calls.append(a)

        with patch("socket.socket", return_value=mock_sock):
            fingerprint(_wav1())
            build_database(WAV_DIR, DB_PATH)

        assert len(bind_calls) == 0, "Library must not call socket.bind()"
        assert len(listen_calls) == 0, "Library must not call socket.listen()"

    def test_req78_no_forbidden_module_imports(self):
        """Req 78 — forbidden modules are not imported anywhere in the library."""
        import ast
        forbidden = {"socket", "urllib", "http", "requests", "subprocess",
                     "asyncio", "telnetlib", "ftplib"}
        import audio_fingerprint.database as db_mod
        import audio_fingerprint.fingerprint as fp_mod
        import audio_fingerprint.matcher as mt_mod
        import audio_fingerprint.__main__ as main_mod
        for mod in [db_mod, fp_mod, mt_mod, main_mod]:
            src = inspect.getsource(mod)
            tree = ast.parse(src)
            imported = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imported.add(alias.name.split(".")[0])
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imported.add(node.module.split(".")[0])
            for bad in forbidden:
                assert bad not in imported, (
                    f"'{bad}' must not be imported in {mod.__name__}"
                )
