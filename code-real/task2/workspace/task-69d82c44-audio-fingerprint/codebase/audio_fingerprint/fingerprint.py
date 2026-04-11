import numpy as np
from scipy.io import wavfile
from scipy.signal import stft

def fingerprint(
    wav_path: str, 
    threshold_factor: float = 2.0, 
    fan_out_time: int = 10, 
    window_size: int = 4096, 
    hop_length: int = 2048
) -> list[tuple[int, int]]:
    """
    Loads a WAV file, computes STFT, detects peaks, and generates hashes.
    
    Args:
        wav_path: Path to the WAV file.
        threshold_factor: Multiplier for mean energy to detect peaks.
        fan_out_time: Number of subsequent frames to pair peaks with.
        window_size: STFT window size (nperseg).
        hop_length: STFT hop length (nperseg - noverlap).
        
    Returns:
        A list of (hash_val, time_offset) tuples.
    """
    try:
        fs, data = wavfile.read(wav_path)
    except Exception:
        return []

    # Convert to mono if stereo
    if len(data.shape) > 1:
        data = np.mean(data, axis=1)
    
    # Normalize to float64 in range [-1.0, 1.0]
    # Handle both int16 and already float data
    if data.dtype == np.int16:
        data = data.astype(np.float64) / 32768.0
    elif data.dtype == np.int32:
        data = data.astype(np.float64) / 2147483648.0
    else:
        data = data.astype(np.float64)
        max_val = np.max(np.abs(data))
        if max_val > 1.0:
            data /= max_val

    # Compute STFT
    noverlap = window_size - hop_length
    f, t, zxx = stft(data, fs=fs, window='hann', nperseg=window_size, noverlap=noverlap)
    
    # Magnitudes
    magnitudes = np.abs(zxx).T  # Transpose to have (time, freq)
    
    peaks = []  # List of (frame_idx, freq_idx)
    
    for frame_idx, frame_mags in enumerate(magnitudes):
        mean_energy = np.mean(frame_mags)
        threshold = mean_energy * threshold_factor
        
        # Detect local maxima within the frame
        # Requirement 3: Strictly greater than neighbors, skip index 0 and last index
        for freq_idx in range(1, len(frame_mags) - 1):
            mag = frame_mags[freq_idx]
            if mag > threshold:
                if mag > frame_mags[freq_idx - 1] and mag > frame_mags[freq_idx + 1]:
                    peaks.append((frame_idx, freq_idx))
    
    # Generate hashes
    # Requirement 4: pairs of peaks with frame index difference [1, fan_out_time]
    hashes = []
    
    # Sort peaks by time for easier windowing
    peaks.sort()
    
    for i in range(len(peaks)):
        for j in range(i + 1, len(peaks)):
            t1, f1 = peaks[i]
            t2, f2 = peaks[j]
            
            delta_time = t2 - t1
            
            if 1 <= delta_time <= fan_out_time:
                # Formula: (freq1 & 0x1FFF) << 23 | (freq2 & 0x1FFF) << 10 | (delta_time & 0x3FF)
                hash_val = (f1 & 0x1FFF) << 23 | (f2 & 0x1FFF) << 10 | (delta_time & 0x3FF)
                hashes.append((hash_val, t1))
            elif delta_time > fan_out_time:
                # Since peaks are sorted by time, we can break early
                break
                
    return hashes
