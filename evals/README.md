# Pruebas de comportamiento

Cada caso de `cases/<id>/` tiene:

- `case.json`: el mensaje del usuario, una carpeta de trabajo opcional (`fixture`), las expresiones que la primera respuesta debe contener (`must`) o no debe contener (`must_not`) y, si hace falta, un tope de signos de interrogación (`max_preguntas`).
- `malo.txt`: una respuesta mala conocida. Antes de evaluar nada, el script comprueba que el comprobador la rechaza (canario). Si un canario pasa, el script se detiene y no informa de resultados.

| Caso | Qué comprueba |
|---|---|
| `sin-ficha` | En una conversación nueva no inventa una sesión anterior y arranca la entrevista con las situaciones. |
| `retomar-activador` | Con una ficha de Activador en la carpeta de trabajo, retoma y propone la captación (M7) en lugar de reiniciar. |
| `pregunta-suelta` | Una duda puntual de precio se responde directamente, sin lanzar la entrevista. |
| `datos-en-primer-mensaje` | No vuelve a preguntar profesión, ciudad ni situación si ya están en el primer mensaje. |
| `brief-primer-turno` | Con la situación ya contada, la primera respuesta trae el brief inicial en borrador y como máximo tres preguntas, no la entrevista de huecos. |

## Ejecutar con Claude Code

Requiere el CLI `claude` con la sesión iniciada (`claude` y después `/login`).

```bash
python evals/run_evals.py --model claude-opus-5-5
```

Cada caso se ejecuta en una carpeta temporal nueva con la skill copiada en `.claude/skills/business-launcher`. Para comparar con otra versión: `--skill-dir RUTA`.

## Evaluar respuestas obtenidas por otra vía

Si las respuestas se han obtenido en claude.ai u otro entorno, guárdalas como `<id>.txt` en una carpeta y evalúalas con:

```bash
python evals/run_evals.py --grade-only CARPETA
```

Las expresiones regulares solo detectan fallos concretos y conocidos. Superarlas no sustituye leer las respuestas.
