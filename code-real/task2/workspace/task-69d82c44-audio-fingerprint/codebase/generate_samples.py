import os
import numpy as np
from scipy.io import wavfile

def generate_samples(output_dir: str = "sample_data") -> None:
    """
    Generates exactly 2 synthetic chirp-based WAV files for testing.
    Each file: 30s, 44100 Hz, 5 simultaneous linear chirps.
    """
    os.makedirs(output_dir, exist_ok=True)
    fs = 44100
    duration = 30
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    
    # Define non-overlapping freq ranges for the two files
    # File 1: 200 - 4000 Hz
    # File 2: 4100 - 8000 Hz
    
    ranges = [
        [(200, 1000), (1000, 1800), (1800, 2600), (2600, 3400), (3400, 4000)],
        [(4100, 4900), (4900, 5700), (5700, 6500), (6500, 7300), (7300, 8000)]
    ]
    
    for i, file_ranges in enumerate(ranges):
        audio = np.zeros_like(t)
        for f_start, f_end in file_ranges:
            # Linear chirp frequency: f(t) = f0 + (f1 - f0) * t / T
            # Phase: phi(t) = 2 * pi * integral(f(t) dt) = 2 * pi * (f0 * t + 0.5 * (f1 - f0) * t^2 / T)
            phase = 2 * np.pi * (f_start * t + 0.5 * (f_end - f_start) * (t**2) / duration)
            audio += np.sin(phase)
        
        # Normalize to prevent clipping
        audio = audio / np.max(np.abs(audio))
        
        # Convert to int16 for WAV storage (though library should normalize back to float64)
        audio_int16 = (audio * 32767).astype(np.int16)
        
        filename = f"sample_{i+1}.wav"
        filepath = os.path.join(output_dir, filename)
        wavfile.write(filepath, fs, audio_int16)

if __name__ == "__main__":
    generate_samples()
