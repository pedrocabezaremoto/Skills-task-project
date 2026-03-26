# Módulo 1: Fundamentos y TDD — Formación de IA (Video 1)

> **Documento de Entrenamiento (training1)**
> Informe basado en la sesión informativa: Metodologías para la Generación de Código de Alta Calidad mediante IA.

---

## 📌 El Desafío Principal: La Brecha entre la Intención y la Ejecución
Uno de los mayores obstáculos en el desarrollo de software asistido por IA es la ambigüedad de las instrucciones iniciales. Mientras que un ser humano puede solicitar algo de manera informal, la IA requiere una estructura detallada para evitar resultados frágiles o propensos a errores.

El objetivo no es solo que la IA escriba código que parezca funcionar, sino implementar un sistema para garantizar que el software generado sea de **alta calidad, verificable y sólido**.

**La Premisa Fundamental:** *"Basura entra, basura sale" (Garbage in, garbage out)*. La calidad del resultado final depende directamente de la estructura y el detalle del *prompt* inicial.

---

## 🏗️ Paso 1: El Plano Arquitectónico (La Interfaz Esperada)
Para cerrar la brecha de comunicación, se crea un plano detallado basado en el concepto de **Interfaz Esperada (Expected Interface)**. Actúa como un contrato técnico que define el éxito antes de que se escriba una sola línea de código, eliminando conjeturas.

El plano desglosa el proyecto en campos increíblemente precisos:
- **Rutas de archivos exactas:** Ubicación precisa donde debe residir el código.
- **Nombres de funciones:** Definiciones claras de la nomenclatura a usar.
- **Entradas y Salidas (I/O) específicas:** Definición exacta de qué datos recibe cada función y qué debe retornar.

---

## ⚔️ Paso 2: El "Gauntlet" (Desarrollo Guiado por Pruebas - TDD)
Una vez establecido el plano, el código debe someterse a un riguroso proceso de pruebas (el *"gauntlet"* o desafío) basado en la metodología **Test-Driven Development (TDD)**. Aquí las pruebas se escriben *antes* que el software.

### El Flujo de Trabajo TDD:
1. **Escritura de Pruebas:** Se crean basadas *exclusivamente* en el plano arquitectónico.
2. **Validación del Fallo (Fail):** Se ejecutan sobre un proyecto vacío. Es **obligatorio** que todas fallen para demostrar que el sistema no da "falsos positivos" y establecer una línea base real.
3. **Construcción de la IA:** La IA desarrolla el código con un solo objetivo: superar las pruebas.
4. **Validación del Éxito (Pass):** Se busca una transición total de fallos (rojo) a éxitos (verde).

> *"En este sistema, el fallo no es solo una opción. Es el punto de partida obligatorio".*

### 🏅 El Golden Patch (Parche Dorado)
El resultado de superar con éxito este "gauntlet" es el **Golden Patch**. Se denomina "dorado" porque representa una solución que fue especificada con precisión y probada rigurosamente.

---

## ⚖️ Paso 3: Verificación Humana (Rúbricas de Expertos)
Las pruebas automatizadas, aunque esenciales, tienen limitaciones críticas:
- **Incapacidad para evaluar subjetividad:** Verifican si funciona (corrección), pero no si es eficiente, elegante o fácil de leer.
- **Peligro de pruebas rígidas:** Las pruebas excesivamente específicas pueden castigar la creatividad, forzando una única forma de resolver un problema que tiene múltiples soluciones válidas.

Por ello, se introduce una segunda capa visual mediante **Rúbricas de Expertos Humanos**. Su límite es evaluar hasta **30 de los requisitos más críticos** que la máquina no puede juzgar.

### Sistema de Ponderación (Priority Scoring)
- **5 (Mandatorio):** Elementos que deben estar presentes sin excepción.
- **3 (Importante):** Atributos de alta relevancia para la calidad.
- **1 (Deseable):** Características adicionales que aportan valor pero no son estrictamente obligatorias.

### Dimensiones de Revisión Humana
- **Cumplimiento de instrucciones:** ¿Siguió la IA las directrices?
- **Calidad del código:** ¿Es legible y comprensible para otros desarrolladores?
- **Eficiencia:** ¿Utilizó caminos innecesariamente complejos o es óptimo?
- **Claridad:** Facilidad de mantenimiento a futuro.
- **Funcionalidad subjetiva:** Evaluación de la lógica de ingeniería empleada.

---

### 🚀 Conclusión
Al combinar un plano arquitectónico estricto, una metodología de pruebas (de fallo a éxito absoluto) y el juicio humano experto, se logra un sistema de **Verificación Dual** que garantiza que la IA no solo "construya cosas", sino que las construya de manera íntegra y profesional.
