# Rúbrica de Evaluación Técnica — Audio Fingerprinting Library

Esta rúbrica cuantifica la calidad y cumplimiento del "Golden Patch" basándose estrictamente en los requerimientos del `prompt.md`.

## Dimensión 1: Instruction Following & Environmental Compliance
| ID | Criterio de Evaluación | Peso |
|:---|:---|:---:|
| 1.1 | El código cumple con las dependencias requeridas (Python 3.11, numpy 1.26, scipy 1.13) sin librerías externas adicionales. | 3 |
| 1.2 | El sistema evita exitosamente el uso de módulos de red prohibidos (`socket`, `urllib`, `requests`, etc.) manteniendo un entorno 100% "air-gapped" y operando solo con datos generados localmente. | 5 |

## Dimensión 2: Code Correctness (Signal Processing & Hashes)
| ID | Criterio de Evaluación | Peso |
|:---|:---|:---:|
| 2.1 | `fingerprint()` carga el audio con scipy, lo convierte a mono y normaliza a float64 en el rango especificado [-1.0, 1.0]. | 3 |
| 2.2 | El cálculo de STFT utiliza exactamente los parámetros requeridos: window_size=4096, hop_length=2048 y Hann window. | 5 |
| 2.3 | El algoritmo de detección de picos aplica el umbral multiplicativo de forma exacta (`mean_energy * threshold_factor`). | 3 |
| 2.4 | El código selecciona exitosamente máximos locales verificando los vecinos inmediatos y excluyendo los índices 0 y final. | 3 |
| 2.5 | La generación de hashes aplica la fórmula de bit-shifting exacta: `(freq1 & 0x1FFF) << 23 | (freq2 & 0x1FFF) << 10 | (delta_time & 0x3FF)`. | 5 |

## Dimensión 3: Code Efficiency (Database & Matching Logic)
| ID | Criterio de Evaluación | Peso |
|:---|:---|:---:|
| 3.1 | La base de datos crea exitosamente el índice `idx_fingerprints_hash` garantizando búsquedas eficientes en la tabla `fingerprints`. | 5 |
| 3.2 | La lógica de inserción limpia previamente los registros duplicados (`DELETE FROM fingerprints WHERE song_name = ?`) para mantener la idempotencia en `build_database`. | 3 |
| 3.3 | El sistema procesa correctamente las consultas calculando `offset_diff = db_offset - clip_offset` y agrupando los resultados por recuento de alineaciones. | 5 |

## Dimensión 4: Code Quality (Operations & Testing)
| ID | Criterio de Evaluación | Peso |
|:---|:---|:---:|
| 4.1 | El script guarda el `song_name` de forma limpia (sin rutas ni extensión `.wav`) en la persistencia y durante la evaluación en los matching. | 3 |
| 4.2 | La función `test_mode` controla la semilla (seed 42), añade exactamente 20 dB SNR temporalmente y procesa los clips a través de `tempfile`. | 3 |
| 4.3 | La salida del CLI provee de forma idéntica los prints solicitados (`"BUILD COMPLETE"`, mensajes exactos de match, y `"PASS"`/`"FAIL"`). | 3 |
| 4.4 | `generate_samples.py` genera 2 archivos funcionales de 30s con 5 chirps, proveyendo suficiencia estadística de >200 hashes por archivo. | 3 |

## Dimensión 5: Code Clarity (Documentation & Design)
| ID | Criterio de Evaluación | Peso |
|:---|:---|:---:|
| 5.1 | La implementación expone los parámetros (`threshold_factor`, `fan_out_time`, `window_size`, `hop_length`, `min_confidence`) como keyword arguments con valor por defecto. | 1 |
| 5.2 | Las frecuencias del sintetizador se limitan limpiamente al rango de [200 Hz, 8000 Hz] reflejando claridad en la lógica de generación. | 1 |

---
**Puntaje Total Esperado:** 100% de criterios en "PASS" para aprobación del Golden Patch.
