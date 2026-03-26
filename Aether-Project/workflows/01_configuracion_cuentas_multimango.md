# Guía: Configuración de Cuentas Off-Platform en Multimango y Hubstaff

**Resumen:** Para trabajar en Aether, es fundamental configurar correctamente las credenciales "wfe-" para Multimango y rastrear el tiempo de forma obligatoria en Hubstaff con el proyecto `aether-bill-auditsandsheetwork`.

## 1. Obtención de Credenciales WFE
1. Dirígete al panel de **Outlier** -> **Profile** -> **My Account** -> **Off-Platform Credentials**.
2. Las credenciales deben tener el formato `wfe-xxxxxxxxxxxxxxxx@outlier.ai`.
3. Si no están habilitadas, solicita la activación en la comunidad de Outlier (Latam Coders).

## 2. Registro en Multimango (multimango.com)
Este es el portal donde se ejecutan realmente las tareas del proyecto.
- **Correo Electrónico:** Debes registrarte EXCLUSIVAMENTE con el correo `wfe-xxxxxxxxxxxxxxxx@outlier.ai`. No usar correo personal.
- **Nombre de Usuario:** Usa la parte inicial del correo WFE antes del `@` o tu ID de Outlier si está ocupado.
- **Contraseña:** Puedes usar tu contraseña de Outlier o crear una nueva para Multimango.

### Verificación 2FA
Al crear la cuenta, el código de verificación NO llegará a la bandeja de entrada del correo WFE, sino a la bandeja del **correo electrónico personal** asociado a tu cuenta de Outlier.
- Espera de 10 a 30 minutos.
- Revisa la bandeja de Spam.

## 3. Validación y Registro en Curso de Outlier
- Ingresa las credenciales creadas (WFE y contraseña) dentro del curso/formulario de Outlier para propósitos organizacionales (tracking) y de confirmación del onboarding.
- **Valida el acceso:** Revisa que el correo WFE aparezca en la parte inferior izquierda de Multimango. Si aparece tu correo personal, la configuración está fallida, cierra sesión y repite el proceso.

## 4. Gestión en Hubstaff
- **Proyecto a seleccionar:** `aether-bill-auditsandsheetwork`.
- Inicio de tiempo al arrancar la tarea, detención inmediata al enviarla (Submit/Skip).
- El límite es colectivo para el proyecto Aether; el servidor reinicia el presupuesto a las 6:00 AM PST a diario.
