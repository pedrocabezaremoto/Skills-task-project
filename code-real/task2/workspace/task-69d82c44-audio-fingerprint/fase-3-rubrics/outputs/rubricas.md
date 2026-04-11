# Rúbrica de Evaluación Técnica — Audio Fingerprinting Library

Esta rúbrica cuantifica la calidad y cumplimiento del "Golden Patch" basándose estrictamente en los requerimientos definidos en el `prompt.md`.

## 1. Tech Stack & Environmental Compliance (Peso: 5)
| ID | Criterio de Evaluación | Peso |
|:---|:---|:---:|
| 1.1 | El proyecto utiliza Python 3.11, numpy 1.26 y scipy 1.13 exclusivamente para el procesamiento y persistencia. | 5 |
| 1.2 | El código NO importa ni utiliza módulos prohibidos: `socket`, `urllib`, `http`, `requests`, `subprocess`, `asyncio`, `telnetlib`, `ftplib`. | 5 |
| 1.3 | El sistema es totalmente "air-gapped": no realiza I/O de red ni descarga datasets externos; toda la data se genera localmente. | 5 |

## 2. Core Signal Processing (Fingerprinting) (Peso: 3)
| ID | Criterio de Evaluación | Peso |
|:---|:---|:---:|
| 2.1 | `fingerprint()` carga WAVs usando `scipy.io.wavfile.read` y normaliza a float64 en el rango [-1.0, 1.0]. | 3 |
| 2.2 | El STFT utiliza exactamente: window=4096, hop=2048 y Hann window. | 3 |
| 2.3 | La detección de picos usa un umbral multiplicativo `mean_energy * threshold_factor` (default 2.0). | 3 |
| 2.4 | Se seleccionan únicamente máximos locales (excluyendo índices 0 y final) donde la magnitud es estrictamente mayor a los vecinos inmediatos. | 3 |
| 2.5 | La generación de hashes utiliza la fórmula de bit-shifting exacta: `(freq1 & 0x1FFF) << 23 | (freq2 & 0x1FFF) << 10 | (delta_time & 0x3FF)`. | 5 |

## 3. Database & Matching Logic (Peso: 5)
| ID | Criterio de Evaluación | Peso |
|:---|:---|:---:|
| 3.1 | La tabla `fingerprints` se crea con la sentencia SQL exacta y posee el índice `idx_fingerprints_hash` sobre la columna `hash`. | 5 |
| 3.2 | `build_database` elimina entradas previas de una canción (`DELETE WHERE song_name = ?`) antes de insertar nuevas para evitar duplicados. | 3 |
| 3.3 | La función `query` computa `offset_diff = db_offset - clip_offset` y agrupa correctamente por `(song_name, offset_diff)`. | 5 |
| 3.4 | El sistema retorna `("no_match", 0)` si no hay hashes coincidentes O si el conteo máximo es menor a `min_confidence` (default 5). | 5 |

## 4. Operational Features & CLI (Peso: 3)
| ID | Criterio de Evaluación | Peso |
|:---|:---|:---:|
| 4.1 | `test_mode` extrae un segmento de 10s con semilla `42`, añade ruido de exactamente 20 dB SNR y usa `tempfile` para el clip ruidoso. | 3 |
| 4.2 | El CLI expone exactamente los subcomandos `build`, `query` y `test` con sus flags correspondientes. | 3 |
| 4.3 | La salida a stdout es exacta: `"BUILD COMPLETE"`, `"Match: <name> (confidence: <N>)"` o `"No match found"`, y `"PASS"`/`"FAIL"`. | 5 |

## 5. Synthetic Data Generation (Peso: 3)
| ID | Criterio de Evaluación | Peso |
|:---|:---|:---:|
| 5.1 | `generate_samples.py` genera exactamente 2 archivos WAV de 30 segundos con 5 chirps lineares cada uno. | 3 |
| 5.2 | Las frecuencias de los chirps están en el rango [200 Hz, 8000 Hz] y no se solapan entre archivos, produciendo al menos 200 hashes por archivo. | 3 |

---
**Puntaje Total Esperado:** 100% de criterios en "Cumple" para aprobación del Golden Patch.
