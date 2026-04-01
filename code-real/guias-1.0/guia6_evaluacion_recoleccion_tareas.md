# Guía 6 — Lineamientos para la Evaluación y Recolección de Tareas de Ingeniería de Software

## Resumen Ejecutivo
El objetivo central de la recolección de tareas de ingeniería de software (SWE) es establecer un marco de verificación robusto que no comprometa la generalización ni filtre la solución al modelo. Para lograr esto, se propone una metodología basada en tres pilares: una Interfaz Esperada claramente definida, Scripts de Evaluación programáticos y objetivos, y Rúbricas para la evaluación cualitativa y estructural. La estrategia busca tratar la solución como una "caja negra" para las pruebas de entrada/salida, mientras se reservan las "rúbricas atómicas" para la inspección directa del código ("caja blanca"), garantizando así el cumplimiento de restricciones arquitectónicas y de diseño sin sobre-especificar la implementación.

---

## La Interfaz Esperada: El Punto de Entrada Natural
La Interfaz Esperada representa el punto de contacto entre el usuario o sistema dependiente y la solución. Su diseño es crítico para evitar la sobre-especificación, la cual podría dictar la arquitectura interna o revelar la solución prevista.

### Principios Fundamentales de la Interfaz
- **Superficie Mínima:** Debe especificar únicamente lo esencial, como la función primaria, la clase principal con sus métodos públicos requeridos, el comando exacto de la CLI o la ruta del punto final de la API.
- **Tipado Estricto:** Es imperativo definir explícitamente los argumentos de entrada, los tipos de datos y los formatos de salida. Esto previene fallos en los scripts de evaluación por discrepancias triviales (ej. retornar una tupla en lugar de una lista).
- **Agnosticismo de Implementación:** No debe mencionar estructuras de archivos (salvo requisitos inherentes), variables de estado interno o funciones de soporte/ayuda.

---

## Metodologías de Verificación
La evaluación de las tareas se divide en dos enfoques complementarios: validación programática objetiva y evaluación cualitativa estructural.

### 1. Scripts de Evaluación (Pruebas de Caja Negra)
Estos scripts son aserciones programáticas que interactúan exclusivamente a través de la Interfaz Esperada. Se prohíbe explícitamente el uso de mocks o parches en los componentes internos de la solución.
- **Enfoque en Entrada/Salida:** Verificación de que entradas específicas produzcan salidas exactas, cubriendo casos de uso estándar, casos de borde e entradas inválidas.
- **Verificación de Efectos Secundarios:** Para tareas que involucren bases de datos, sistemas de archivos o redes, los scripts deben validar el estado resultante del sistema (ej. confirmar la creación de un registro o un archivo).

### 2. Rúbricas (Evaluación de Caja Blanca)
Las rúbricas se utilizan cuando las restricciones no pueden evaluarse de forma determinista o programática. A diferencia de los scripts, estas requieren acceso directo al código fuente.
- **Adherencia a Restricciones:** Verificar que no se utilicen librerías prohibidas (ej. implementar algoritmos desde cero sin librerías de alto nivel).
- **Controles Arquitectónicos:** Validar patrones de diseño y prácticas de seguridad (ej. uso de Hooks en React o algoritmos de hashing para contraseñas).
- **Evaluación Cualitativa:** Revisión de legibilidad del código, documentación y cumplimiento de instrucciones de UI/UX.

---

## Ejemplos de Aplicación por Dominio
La siguiente tabla sintetiza cómo se aplican estos conceptos en diversos campos de la ingeniería de software:

| Dominio | Interfaz Esperada | Enfoque del Test Case | Propósito de la Rúbrica |
|---|---|---|---|
| Algoritmos | `def find_shortest_path(grid: list[list[int]]) -> int:` | Validar el camino más corto o retorno de -1 en casos irresolubles. | Verificar el uso de algoritmos óptimos (BFS/A*) sobre fuerza bruta. |
| Ciencia de Datos | `def train_and_predict(train_csv: str, test_csv: str) -> list[float]:` | Asegurar que la longitud de salida coincida y el RMSE sea < 1.5. | Confirmar el escalado de funciones (feature scaling) antes del entrenamiento. |
| Web Backend | `POST /api/checkout` (JSON con user_id y cart_items). | Assert de código 200 OK y verificación de base de datos mock. | Validar que la inserción y el pago ocurran en una transacción atómica. |
| Frontend/UI | Componente `UserProfile` con prop `user`. | Renderizar en DOM de prueba y confirmar campos de texto (nombre, email). | Verificar que el diseño use Flexbox o Grid para adaptabilidad móvil. |

---

## Conclusiones sobre el Diseño de Tareas
El documento subraya que si una evaluación requiere probar la lógica interna directamente mediante scripts, es un indicador de que la Interfaz Esperada está mal diseñada. En tales casos, los requisitos deben ser verificados mediante rúbricas para mantener la integridad de la evaluación y la libertad de implementación del desarrollador.
