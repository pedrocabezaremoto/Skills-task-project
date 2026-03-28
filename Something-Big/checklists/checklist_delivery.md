# Checklist de Entrega Final — Something Big

> Verificar TODOS los puntos antes de culminar una tarea.

---

## 📋 Calidad del Codigo
- [ ] **Cumple todos los puntos del prompt fielmente.**
- [ ] **Diseño del Código:** ¿Sigue principios SOLID, es modular y eficiente?
- [ ] **Legibilidad:** Nombres de variables descriptivos, estructura lógica.
- [ ] **Seguridad:** ¿Hay fallos catastróficos o vulnerabilidades introducidas?
- [ ] **Complejidad Justificada:** Al clasificar la tarea, justificar con arquitectura.

---

## 📋 Validación del Entorno y Tests
- [ ] **Agnosticismo:** ¿Los tests son F2P estrictos y agnósticos?
- [ ] **Redundancia:** ¿Hay tests irrelevantes solo para aumentar cobertura?
- [ ] **Dockerfile:** ¿Usa SHA del commit base y no tiene comandos `COPY` prohibidos?
- [ ] **run_script.sh:** ¿Es ejecutable (`chmod +x`)?
- [ ] **parsing.py:** ¿Produce JSON válido? (`validado con python3 parsing.py`)
- [ ] **output.json:** ¿Generado al correr Golden Patch? (No escrito a mano).

---

## 📋 Fluidez Nativa (English Level)
- [ ] **Cero Tolerancia:** Menos de 4 errores menores.
- [ ] **Errores Graves:** Cero errores "Egregious" (prohibido).
- [ ] **Tono Profesional:** Inglés técnico de nivel nativo.

---

## 📋 Arquitectura y Prompts
- [ ] **Prompt:** Agnóstico, todos los esquemas completos, inglés nativo.
- [ ] **Rúbrica:** ≥ 10 criterios, pesos 1/3/5 solamente, 5 dimensiones cubiertas.

---

## ⚠️ RECORDATORIO DE SEGURIDAD
- [ ] **IA de Terceros:** NUNCA copiar-pegar texto generado por IA directamente en la plataforma Outlier. Leer → Entender → Escribir con tus propias palabras.
