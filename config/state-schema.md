# Ficha de progreso

Business Launcher se trabaja en varias sesiones. El progreso vive en un único archivo, `ficha-business-launcher.md`, que pertenece a la persona: un resumen legible arriba y el estado en JSON abajo. Con él se retoma otro día o en otro entorno.

## Dónde se lee y se guarda

| Entorno | Leer al empezar | Guardar tras cada checkpoint |
|---|---|---|
| Claude Code o Cowork (hay carpeta de trabajo) | `business-launcher/ficha-business-launcher.md` en la carpeta de trabajo | Edita ese archivo directamente; es la ficha de la persona y no hace falta pedir permiso para actualizarla. |
| claude.ai dentro de un Proyecto | Archivos del Proyecto o adjunto en la conversación | Genera el archivo actualizado y di en una línea que sustituya la versión anterior en el Proyecto. |
| claude.ai sin Proyecto | Adjunto en la conversación | Genera el archivo actualizado y, la primera vez, sugiere crear un Proyecto "Mi negocio" y subirla allí para no perderla. |
| Sin creación de archivos | Bloque de reanudación pegado por la persona | Muestra el bloque de reanudación al cerrar cada módulo para que lo copie. |

Afirma que el progreso está guardado solo cuando el archivo se ha escrito. Si no se puede guardar, dilo en una línea: el progreso solo vale para esta conversación. La memoria de Claude o la búsqueda en chats anteriores pueden dar pistas, pero el estado sale de la ficha.

## Al arrancar

En una sesión nueva la ficha se crea en el mismo turno que el brief inicial, aunque casi todos los campos estén vacíos, en `null` o en cero. Un campo vacío no es motivo para seguir preguntando antes de entregar el brief: los huecos van como `[PENDIENTE]` en el texto del brief y en "Dónde estamos", que debe decir que el brief es un borrador. `progress.current` queda en `"M0"`, `progress.completed` vacío y `progress.next_step` en confirmar la ruta o el primer módulo. No inventes cifras para que el JSON parezca completo. La versión de la ficha sigue en 4.0.0: el arreglo del 22-10-2026 no cambia el esquema.

Al retomar, resume la ficha en lenguaje natural ("La última vez cerramos la investigación de mercado y la oferta. ¿Seguimos con el plan de 90 días?"). No enseñes el JSON salvo que la persona lo pida.

## Qué no se guarda

La ficha puede acabar en un Proyecto, en una carpeta compartida o reenviada. Por eso no guarda relatos personales, salud, situación emocional ni datos de terceros (nombres de clientes o contactos). De los factores humanos se guarda solo el ajuste al plan ("primeras conversaciones con red cercana", "sprints de una semana") y el nivel de urgencia. Si la persona da cifras de facturación, se guardan como las dio y se le recuerda una vez que la ficha las contiene.

## Formato de la ficha

````markdown
# Ficha Business Launcher — [nombre del negocio o de la persona]
Versión de la ficha: 4.0.0 · Actualizada: AAAA-MM-DD

## Dónde estamos
[5 a 8 líneas: ruta, módulos hechos, siguiente paso y decisiones pendientes]

## Decisiones clave
- AAAA-MM-DD · M2 · Servicio tractor: [servicio] a [precio] €, porque…

## Entregables
- M1 · investigacion-mercado-[nombre].html (v1)

## Estado (lo mantiene Claude; no hace falta editarlo)
```json
{ ...esquema de abajo... }
```
````

## Bloque de reanudación

Para entornos sin archivos, como máximo 12 líneas que la persona puede pegar en una conversación nueva:

```
BUSINESS LAUNCHER · ficha 4.0.0 · AAAA-MM-DD
Persona/negocio: … · Ruta: … · Perfil: …
Hecho: M0, M1 · Siguiente: M7
Oferta: … · Precio tractor: … · ICP: …
Ajustes del plan: … · Urgencia: …
Pendiente: …
```

## Esquema del estado

```json
{
  "version": "4.0.0",
  "updated_at": "AAAA-MM-DD",
  "user_profile": {
    "name": "",
    "location": "",
    "employment": "cuenta ajena | autonomo | sociedad | sin actividad",
    "customer_type": "empresas | particulares | mixto",
    "regulated_activity": "",
    "problem_statement": "",
    "differential": "",
    "existing_clients": false,
    "economic_goal": "",
    "time_available_hours_week": 0,
    "budget_initial": 0,
    "has_team": false,
    "has_brand": false,
    "excluded_sectors": [],
    "existing_assets": {
      "monthly_revenue": null,
      "num_clients": null,
      "avg_ticket": null,
      "existing_contracts": false,
      "existing_website": "",
      "existing_tools": []
    }
  },
  "calibration_level": "arranca_de_cero | freelance_sin_estructura | profesional_con_base | veterano",
  "urgency_level": "baja | media | alta | critica",
  "plan_adjustments": [],
  "route": {
    "assigned": "escalador | activador | redefinidor | definidor | explorador",
    "reassigned_from": null,
    "sequence": ["M0", "M1", "M2", "M5"],
    "optional_chosen": [],
    "skipped": [{ "module": "M3", "motivo": "ya tiene marca" }]
  },
  "progress": {
    "current": "M1",
    "completed": ["M0"],
    "next_step": ""
  },
  "plan_horizon_days": 90,
  "visual_direction": null,
  "decisions": [
    { "date": "AAAA-MM-DD", "module": "M2", "decision": "", "alternatives": [], "motivo": "" }
  ],
  "deliverables": [
    { "module": "M1", "name": "", "format": "HTML", "version": 1 }
  ]
}
```

- Los módulos se identifican siempre como `M0` a `M7` (los archivos se llaman `00-intake.md` a `07-captacion.md`).
- En el brief borrador los campos desconocidos se dejan vacíos. No se entrevista para completar el esquema antes de entregar el brief.
- `visual_direction` lo rellena M6 con la estructura descrita en `modules/06-web-prompt.md`.
- `plan_horizon_days` es 30 en urgencia crítica (ver `layers/factores-humanos.md`).

## Al escribir

- Parte de la ficha que ya tienes en la conversación; añade decisiones y entregables, no los borres. Una entrega regenerada sube su `version`.
- Si la ficha es de una versión anterior (3.x, guardada en el almacenamiento de un artifact o con módulos "03"), conviértela a este formato, quita los datos personales que ya no se guardan y dilo en una línea.
- Si la ficha crece mucho, resume las decisiones antiguas en "Dónde estamos" y conserva las de los módulos en curso.
