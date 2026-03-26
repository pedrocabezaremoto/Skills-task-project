# Módulo 3: Directrices v3 e Ingeniería Avanzada (Video 3)

> **Documento de Entrenamiento (training1)**
> Basado en: *Directrices Operativas y Actualizaciones del Proyecto de Ingeniería de Software (v3).*

---

## 🌐 1. Alcance Técnico y Dominios Soportados
El entorno Real Coder está enfocado en emular ingeniería de software tipo *Upwork/freelancer*, tomando descripciones vagas y produciendo sistemas deterministas. Soporta desde el nivel **Básico** hasta **Experto**.

**Dominios autorizados:**
- Desarrollo Backend y Full Stack.
- Aplicaciones CLI (Línea de comandos).
- **Machine Learning e Ingeniería de Datos:** Regla rígida → Solo utilizar *datasets* abiertos (open-source) y modelos base libres de derechos para evitar riesgos de propiedad intelectual y licencias.
- **Prohibido:** Tareas de clonación de plataformas vivas (ej. clon exacto de Reddit), así como sistemas que busquen interactuar con o depender de *endpoints* / APIs privadas o secretas. Se evitan en este flujo las imágenes como entradas clave debido a su complejidad técnica actual.

---

## 🏗️ 2. El Prompt: Equilibrio de Especificidad y Granularidad
El Prompt no debe micro-gestionar el código de la IA. El objetivo del prompt es:
- **Ser veraz y factible:** No pedir sistemas imposibles ni arquitecturas no viables (debe poder compilar).
- **Control de Ingeniería:** Mostrar *qué* se quiere en arquitectura, pero **no el cómo** hiper-específico (No se fuerza a la IA a usar ciertas variables internas auxiliares minúsculas o a capitalizar un *string* interno a menos que la semilla inicial del usuario así lo dicte imperativamente).

**La "Expected Interface" es la Ley:**
- Cubre entre el 60% y el 70% del peso en el prompt.
- Exige incluir no solo nombres y rutas, sino adaptaciones de lenguaje (ej. Herencias obligadas, embeddings o anotaciones específicas si se fuerza Go/Java).

---

## ⚖️ 3. El Problema Número 1: "Especificidad Excesiva" (Over-specificity)
Las actualizaciones de Control de Calidad (QC) introducen una tolerancia cero para las pruebas injustas.

**¿Qué es una prueba excesivamente específica?**
- Validar comportamientos no nombrados u ocultos en el prompt. 
- *Ejemplo Punitivo:* Obligar a tener configurado *ESLint*, forzar el uso de ciertas reglas gramaticales u obligar a manejar específicamente un fallo de red concreto si el Prompt original nunca requirió manejar de red, sino solo persistencia local.

🚨 **Umbral de Falla por QC:** El Control de Calidad exige que **menos del 5%** de la tarea total contenga pruebas excesivamente específicas. Superar este número resulta en tarea rechazada.

---

## 📊 4. Optimización de Rúbricas (Límite Máximo)
Evaluar la carga cognitiva del revisor humano es vital y afecta los tiempos de evaluación (AHT).

- **Límite Estricto:** La lista de rúbricas no debe tener más de **30 criterios**.
- **Jerarquía y Purga:** Si al analizar los comportamientos descubres que tu sistema necesitará 40 criterios para validar subjetivamente la entrega, **estás obligado a purgar y omitir los criterios de Nivel 1 (Deseables)**.
- Los requisitos obligatorios (Nivel 5) y los requisitos funcionales de la lógica (Nivel 3) jamás pueden omitirse en favor de meter un requisito secundario. 
- Al ser el propio desarrollador que valida el código que produjo la máquina, las breves justificaciones funcionan como un control mental y no son perseguidas, por ahora, de forma agresiva por QC.

---

## 🐳 5. Actualizaciones de Entorno: Validación y Docker (Tolerancia Cero)
La reproducibilidad no es negociable; el código de la solución debe ser inyectado transparente.

- **Proscripción del COPY:** **ESTÁ ESTRICTAMENTE PROHIBIDO** usar el comando `COPY` para integrar los archivos del proyecto dentro de la fase `RUN` del archivo Dockerfile (o de cualquier *stage* constructivo que inyecte código estático dentro de la imagen base generada sin volumen).
- **Dependencias Fijas:** El Dockerfile contiene *hardcodeadas* (en piedra) las instalaciones de los paquetes y herramientas (a través de *apt-get*, *pip*, etc.).
- **Script Maestro:** El evaluador (agente o humano) siempre deberá utilizar el script maestro más reciente de orquestación, el cual emitirá sus registros. Si un archivo JSON final resulta emitido "en vacío" (*empty file* o formato corrupto), se considerará un error automático en estado L8 y desestimará el parche.
