# Guía G1: Diseño de Prompts — Something Big

## El Principio Fundamental: Enfoque "Agnóstico" (Implementation-Agnostic)

*   **QUÉ y no CÓMO:** Toda instrucción debe enfocarse exclusivamente en el comportamiento público de las interfaces (entradas y salidas). 
*   **Prohibido Dictar el "CÓMO":** Jamás obligues al modelo a usar un ciclo específico, diccionarios internos, o nombres de variables ocultas.
*   **Pruebas de Caja Negra (Black-Box):** La cobertura total debe lograrse mediante pruebas unitarias que evalúen la superficie externa. No se permite testear métodos privados. Comprobar el manejo de errores (ej. `ValueError`) es válido.

## Estructura Obligatoria de un Prompt

Todo prompt debe simular una solicitud humana real, ser natural y específico. Deben incluirse 4 secciones:

1.  **Objetivo (The Objective):** Meta principal de alto nivel.
2.  **Estrategia (The Strategy):** El enfoque técnico específico (ej. "usar una arquitectura modular").
3.  **Restricciones (The Constraints):** Requisitos técnicos obligatorios (seguridad, tecnologías).
4.  **Interfaz Esperada (Expected Interface):** La parte crítica e innegociable. Por cada archivo, clase o función a crear, especificar de manera agnóstica:
    *   **Path:** Ruta exacta del archivo.
    *   **Name:** Nombre de la clase o función.
    *   **Type:** Tipo (clase, método, función).
    *   **Input:** Parámetros y sus tipos.
    *   **Output:** Tipo de retorno.
    *   **Description:** Qué hace la interfaz.

### Checklist de Calidad del Prompt:
- [ ] No se mencionan nombres de variables internas.
- [ ] No se describen pasos algorítmicos específicos ("usa un loop", "usa recursión").
- [ ] Cada componente tiene los 6 campos del schema de interfaz.
- [ ] Todas las restricciones son conceptuales, no a nivel de implementación.
- [ ] El inglés es de nivel nativo (cero errores gramaticales).
- [ ] Los patrones de diseño solo se mencionan si el prompt los exige.

---
*Contexto Onboarding:* 
- **Prompt Agnóstico (WHAT):** Describe comportamiento público. (Estándar obligatorio).
- **Prompt Específico (HOW):** No dictar algoritmos, estructuras o campos privados (ej. `self._tokens`).
