import os
import sqlite3
from .fingerprint import fingerprint

def build_database(
    wav_dir: str, 
    db_path: str, 
    threshold_factor: float = 2.0, 
    fan_out_time: int = 10, 
    window_size: int = 4096, 
    hop_length: int = 2048
) -> None:
    """
    Builds or updates a SQLite database with fingerprints from WAV files.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Requirement 7: Create table and index
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fingerprints (
            hash INTEGER, 
            offset INTEGER, 
            song_name TEXT
        )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_fingerprints_hash ON fingerprints(hash)")
    conn.commit()
    
    # Process files
    if not os.path.exists(wav_dir):
        conn.close()
        return

    for filename in os.listdir(wav_dir):
        if filename.lower().endswith(".wav"):
            song_name = os.path.splitext(filename)[0]
            wav_path = os.path.join(wav_dir, filename)
            
            # Requirement 6: Delete existing entries for this song
            cursor.execute("DELETE FROM fingerprints WHERE song_name = ?", (song_name,))
            
            # Compute fingerprints
            hashes = fingerprint(
                wav_path, 
                threshold_factor=threshold_factor, 
                fan_out_time=fan_out_time, 
                window_size=window_size, 
                hop_length=hop_length
            )
            
            # Insert triples
            data = [(h, offset, song_name) for h, offset in hashes]
            cursor.executemany("INSERT INTO fingerprints (hash, offset, song_name) VALUES (?, ?, ?)", data)
            conn.commit()
            
    conn.close()

def query(
    wav_path: str, 
    db_path: str, 
    min_confidence: int = 5, 
    threshold_factor: float = 2.0, 
    fan_out_time: int = 10, 
    window_size: int = 4096, 
    hop_length: int = 2048
) -> tuple[str, int]:
    """
    Queries the database to identify a clip.
    """
    hashes = fingerprint(
        wav_path, 
        threshold_factor=threshold_factor, 
        fan_out_time=fan_out_time, 
        window_size=window_size, 
        hop_length=hop_length
    )
    
    if not hashes or not os.path.exists(db_path):
        return ("no_match", 0)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # group results by (song_name, offset_diff)
    # offset_diff = db_offset - clip_offset
    matches = {} # (song_name, offset_diff) -> count
    
    for hash_val, clip_offset in hashes:
        cursor.execute("SELECT offset, song_name FROM fingerprints WHERE hash = ?", (hash_val,))
        rows = cursor.fetchall()
        for db_offset, song_name in rows:
            diff = db_offset - clip_offset
            key = (song_name, diff)
            matches[key] = matches.get(key, 0) + 1
            
    conn.close()
    
    if not matches:
        return ("no_match", 0)
    
    # Find the best song
    # Aggregate confidence per song_name - actually the requirement says 
    # group by (song_name, offset_diff) and identify pair with highest confidence.
    
    best_song = "no_match"
    max_confidence = 0
    
    for (song_name, diff), confidence in matches.items():
        if confidence > max_confidence:
            max_confidence = confidence
            best_song = song_name
            
    if max_confidence >= min_confidence:
        return (best_song, max_confidence)
    else:
        return ("no_match", 0)
