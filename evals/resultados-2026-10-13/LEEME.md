# Resultados del 13-10-2026 (v4.0.0)

4 de 4 casos superados, con los canarios rechazados antes de evaluar.

Cómo se obtuvieron: el CLI `claude` del equipo no tenía sesión iniciada, así que cada caso lo ejecutó un subagente de Claude Code (Claude Opus 5.5) al que se le dio la skill instalada y la carpeta de trabajo del caso, con la instrucción de comportarse como en una sesión real y devolver su primera respuesta. Las respuestas se evaluaron con `python evals/run_evals.py --grade-only`. No es lo mismo que una ejecución con el CLI: el subagente también tenía el contexto general del usuario. Repetir con `python evals/run_evals.py` en cuanto el CLI tenga sesión.

Incidencias, para que no se lean como un verde limpio:
- `datos-en-primer-mensaje` falló en la primera ejecución: no nombraba la ruta. Se añadió a M0 que, si el primer mensaje ya deja clara la situación, nombre la ruta y pida confirmación; la repetición pasó. La respuesta afirma "consulta" cuando el usuario no lo dijo: detalle a vigilar.
- `retomar-activador`: el comprobador exigía literalmente "investigación de mercado" y la respuesta correcta decía "investigación de canales". Se amplió a "investigación" tras ese falso negativo; el canario sigue rechazando la respuesta mala.
- Línea base 3.0.0 en las mismas condiciones: `sin-ficha` falla (pregunta de una en una sin ofrecer las situaciones); `retomar-activador` pasa, porque el modelo lee la ficha 4.0 que encuentra en la carpeta aunque la 3.0 nunca la habría escrito.
