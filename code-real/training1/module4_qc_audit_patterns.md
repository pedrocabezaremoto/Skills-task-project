# Módulo 4: Patrones de Auditoría QC — Anti-Patrones Reales (Onboarding)

> **Documento de Entrenamiento (training1)**
> Basado en: *Casos reales de fallos QC presentados en el Real Coder Intro Course (Páginas 15-19).*

---

## 📌 Propósito de este Módulo

Este módulo documenta los **anti-patrones más comunes** que causan el rechazo de tareas por parte del equipo de Control de Calidad (QC) de Outlier. Cada caso proviene de un ejemplo real presentado durante el onboarding. La calificación de fallo en todos los casos fue **QC 2/5 FAIL**.

**Regla fundamental:** Un fallo QC no siempre significa que el código no funciona. Significa que la **ingeniería del prompt, los tests o las rúbricas** no cumplen el estándar de calidad requerido.

---

## 🚨 Anti-Patrón 1: Tests Excesivamente Específicos (Overfitting en Tests)

**Fuente:** Página 15 del Onboarding

### Descripción del Fallo
- 4 de 24 tests en `test_main.py` exigían el argumento exacto `--folder`.
- El prompt original solo pedía: *"aceptar un folder path como argumento de línea de comandos"*.
- Cualquier solución válida usando `--directory`, `--path`, o `--input` fallaría injustamente.

### Violación Técnica
Los tests imponen una **elección de implementación** (el nombre del argumento) que el prompt no definió. Esto castiga a la IA por tomar decisiones válidas alternativas.

### Umbral QC
> ⚠️ Si más del **5%** de los tests totales son excesivamente específicos, la tarea es **rechazada automáticamente**.

### Regla Correcta
```
✅ Testear: "El programa acepta un argumento posicional o con flag para una ruta de carpeta"
❌ No testear: "El programa usa exactamente el flag --folder"
```

---

## 🚨 Anti-Patrón 2: Pruebas Front-End Superficiales (Shallow Testing)

**Fuente:** Página 16 del Onboarding

### Descripción del Fallo
- Los tests solo verificaban si ciertos strings (como `isActive`) existían en el código fuente.
- No renderizaban componentes ni interactuaban con el DOM.
- **Ejemplo concreto:** El prompt pedía que un componente Confetti se renderizara cuando `isActive === true`. El test solo buscaba si la string `isActive` aparecía en el archivo, sin renderizar el componente.

### Violación Técnica
Un test que busca texto en el código fuente no verifica funcionalidad. Es equivalente a hacer `grep` en vez de ejecutar el programa.

### Regla Correcta
```
✅ Test funcional: Renderizar componente → cambiar estado isActive → verificar que Confetti aparece en el DOM
❌ Test superficial: Buscar si la string "isActive" existe en el archivo .tsx
```

### Implicación para Rúbricas
En tareas de **frontend**, las rúbricas deben ser significativamente más robustas. Si el verificador (F2P) es superficial, la rúbrica debe compensar cubriendo los aspectos funcionales que los tests no alcanzan.

---

## 🚨 Anti-Patrón 3: Mocks con Rutas de Importación Rígidas

**Fuente:** Página 17 del Onboarding

### Descripción del Fallo
- Tests usaban `mock.patch("src.file_sync.paramiko.SSHClient")` y `mock.patch("src.file_sync.Observer")`.
- Si un modelo importaba con `from paramiko import SSHClient` en vez de `import paramiko`, **8 tests fallaban**.
- Tests adicionales verificaban funcionalidades no pedidas en el prompt:
  - `test_sftp_client_upload_file_ensures_remote_parent_dir_exists` — El prompt decía "ensure OR handle errors", no ambos.
  - `test_sftp_client_disconnect_is_idempotent` — La idempotencia no era un requisito.

### Violación Técnica
Los `mock.patch` con rutas absolutas de módulos asumen una estructura de importación específica. Esto es un anti-patrón clásico de **acoplamiento a la implementación**.

### Regla Correcta
```
✅ Mockear la interfaz: Verificar que se establece una conexión SSH y se sube un archivo
❌ Mockear la ruta: mock.patch("src.file_sync.paramiko.SSHClient")
```

### Regla General para Mocks
> Los mocks deben verificar **comportamiento** (qué hace el código), no **estructura** (cómo importa los módulos).

---

## 🚨 Anti-Patrón 4: Instrucciones Conflictivas en el Prompt

**Fuente:** Página 18 del Onboarding

### Descripción del Fallo
- El prompt exigía: **"No internet"** durante runtime.
- El README del proyecto decía: *"NLTK data is downloaded automatically on first run"*.
- Ambas instrucciones se contradicen directamente.
- El Golden Patch usaba `download_nltk_data()`, violando la restricción de "no internet".

### Violación Técnica
Un prompt con instrucciones contradictorias crea una **trampa lógica** donde cualquier implementación válida viola al menos una regla.

### Regla Correcta
```
✅ "No internet. Todos los datasets deben estar pre-instalados en el Dockerfile o incluidos como fixtures locales."
❌ "No internet" + README: "NLTK data se descarga automáticamente en el primer uso"
```

### Checklist de Consistencia
Antes de entregar un prompt, verificar que:
- [ ] El prompt y el README no se contradicen.
- [ ] Si se prohíbe internet, todas las dependencias de datos están pre-cargadas.
- [ ] Los edge cases definidos son alcanzables bajo las restricciones declaradas.

---

## 🚨 Anti-Patrón 5: Lógica Técnicamente Imposible

**Fuente:** Página 19 del Onboarding

### Descripción del Fallo
- El prompt mandaba un formato binario estricto para encriptación:
  `Magic Bytes (4) + Version (1) + Salt (16) + Nonce (12) + Ciphertext (variable) + Auth Tag (16)`
- También exigía mensajes de error **distintos** para "wrong passphrase" y "tampered/corrupted data".
- **Esto es técnicamente IMPOSIBLE** con AES-256-GCM sin un verificador de clave dedicado. El algoritmo no puede distinguir entre ambos escenarios.

### Problemas Adicionales en Rúbricas
- **C#1 (Underfitting):** Pedía "no network access" pero la redacción era tan laxa que un modelo podría escribir a archivo local Y llamar a una API remota, y aún así pasar.
- **C#3 (Overfitting):** Exigía que el chunk size fuera una constante nombrada, pero el prompt solo pedía "Read and write in fixed-size chunks" sin mencionar constantes.

### Regla Correcta
```
✅ Verificar viabilidad técnica del prompt ANTES de escribir tests/rúbricas
✅ Si AES-GCM no puede distinguir errores, usar un esquema con verificador de clave (HMAC) o no exigir mensajes distintos
❌ Pedir al Golden Patch algo imposible y forzar workarounds
```

---

## 📊 Tabla Resumen de Anti-Patrones

| # | Anti-Patrón | Causa Raíz | Solución | Página |
|---|---|---|---|---|
| 1 | Tests Overly Specific | Imponer nombres de argumentos no definidos en el prompt | Testear comportamiento, no nombres exactos | P15 |
| 2 | Shallow Frontend Testing | Buscar strings en vez de interactuar con DOM | Renderizar, mutar estado, verificar DOM | P16 |
| 3 | Mocks Rígidos | `mock.patch` con rutas de importación exactas | Mockear interfaces, no rutas de módulos | P17 |
| 4 | Instrucciones Conflictivas | Prompt y README se contradicen | Alinear todas las fuentes de verdad | P18 |
| 5 | Lógica Imposible | Exigir algo técnicamente inviable | Validar viabilidad técnica antes de redactar | P19 |

---

## ✅ Checklist Pre-Entrega (Inspirado en Anti-Patrones)

Antes de entregar cualquier tarea Real Coder, verificar:

- [ ] **Tests agnósticos:** Ningún test impone nombres de variables, flags, o rutas de importación no definidas en el prompt.
- [ ] **Tests funcionales:** Los tests de frontend interactúan con el DOM, no solo buscan strings.
- [ ] **Mocks flexibles:** Los mocks verifican comportamiento, no estructura de importación.
- [ ] **Consistencia documental:** El prompt, README, y cualquier documentación están alineados sin contradicciones.
- [ ] **Viabilidad técnica:** Todo lo que exige el prompt es técnicamente posible con las tecnologías especificadas.
- [ ] **Rúbricas calibradas:** Ningún criterio es tan laxo que permita violaciones (underfitting) ni tan estricto que penalice implementaciones válidas (overfitting).
- [ ] **Umbral del 5%:** Menos del 5% de los tests son excesivamente específicos.
