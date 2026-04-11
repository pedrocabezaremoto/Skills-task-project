import os
import numpy as np
import tempfile
from scipy.io import wavfile
from .database import query

def test_mode(
    wav_path: str, 
    db_path: str, 
    threshold_factor: float = 2.0, 
    fan_out_time: int = 10, 
    window_size: int = 4096, 
    hop_length: int = 2048, 
    min_confidence: int = 5
) -> bool:
    """
    Simulates identification of a noisy segment from an existing file.
    """
    try:
        fs, data = wavfile.read(wav_path)
    except Exception:
        return False

    # Extract 10s segment
    np.random.seed(42)
    duration_samples = int(fs * 10)
    
    if len(data) > duration_samples:
        start_idx = np.random.randint(0, len(data) - duration_samples)
        segment = data[start_idx : start_idx + duration_samples]
    else:
        segment = data
    
    # Ensure float for noise addition
    original_segment = segment.astype(np.float64)
    
    # Calculate Power of Signal
    # SNR = 10 * log10(P_signal / P_noise)
    # 20 = 10 * log10(P_signal / P_noise) -> 2 = log10(P_signal / P_noise) -> 100 = P_signal / P_noise
    # P_noise = P_signal / 100
    p_signal = np.mean(original_segment**2)
    p_noise = p_signal / 100.0
    
    # Standard deviation of noise
    std_noise = np.sqrt(p_noise)
    
    # Add Gaussian white noise
    noise = np.random.normal(0, std_noise, original_segment.shape)
    noisy_segment = original_segment + noise
    
    # Baseline filename without path/ext
    base_name = os.path.splitext(os.path.basename(wav_path))[0]
    
    # Temp file for query
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp_path = tmp.name
        # Convert back to int16 if needed, or stay float
        # wavfile.write can handle float32
        wavfile.write(tmp_path, fs, noisy_segment.astype(np.float32))
    
    try:
        song_name, confidence = query(
            tmp_path, 
            db_path, 
            min_confidence=min_confidence, 
            threshold_factor=threshold_factor, 
            fan_out_time=fan_out_time, 
            window_size=window_size, 
            hop_length=hop_length
        )
        return song_name == base_name
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
