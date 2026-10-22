# Resultados del 22-10-2026 (v4.0.1)

6 de 6 casos superados, con los canarios rechazados antes de evaluar.

Cómo se obtuvieron: en esta máquina no está el CLI `claude`, igual que el 13-10-2026. Cada caso lo ejecutó un subagente con la skill de esta versión, la instrucción de seguir el texto al pie de la letra y devolver solo la primera respuesta. Las respuestas se evaluaron con `python evals/run_evals.py --grade-only evals/resultados-2026-10-22`. `scripts/validate_skill.py` queda en verde cuando la carpeta se llama `business-launcher` (es el nombre que comprueba el validador; este checkout vive en otro directorio).

## El caso nuevo falla con la 4.0.0

`brief-primer-turno-antes.txt` es la primera respuesta de la versión 4.0.0 al mismo mensaje (diseñadora en Sevilla, idea clara, horas y presupuesto). Nombra la ruta Definidor, pide confirmación y pregunta el diferencial. No hay brief. El comprobador la rechaza:

- falta el encabezado del brief inicial
- falta `[PENDIENTE]`
- aparece la pregunta del diferencial, que ahora va después del brief

Esa respuesta solo hace dos preguntas: el fallo de la 4.0.0 no es un cuestionario enorme en el primer mensaje, sino que el entregable no sale y la entrevista ya ha empezado. `malo.txt` del caso añade el cuestionario largo (ocho preguntas) para que el tope de tres también lo rechace.

Con la 4.0.1, la primera respuesta de ese caso es el brief en borrador, con los huecos marcados y sin preguntas.
