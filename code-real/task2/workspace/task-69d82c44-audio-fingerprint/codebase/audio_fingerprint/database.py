def build_database(wav_dir: str, db_path: str) -> None:
    """Builds the SQLite database from a directory of WAV files."""
    pass

def query(wav_path: str, db_path: str, min_confidence: int = 5) -> tuple[str, int]:
    """Queries the database for the best matching song."""
    return ("no_match", 0)
