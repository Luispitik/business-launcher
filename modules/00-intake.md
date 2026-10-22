# M0 — Intake

## Objetivo

Dejar la ruta asignada y un brief utilizable en la primera respuesta. Lo que falte se completa después, sobre ese brief. Si la persona ya ha dado un dato (en su primer mensaje o en una ficha), entra en el brief y no se vuelve a preguntar. Salta lo que su ruta no necesita.

Una pregunta suelta, sin pedir este proceso, no llega aquí: se responde directo, como dice `SKILL.md`.

## Arranque — la primera respuesta

Orden fijo. No lo inviertas y no lo dejes para cuando tengas más datos. El brief sale en este mensaje, en borrador, aunque casi todo esté por cerrar.

1. Preséntate en dos frases, solo si la sesión es nueva. Por ejemplo: "Voy a acompañarte a construir (o reconstruir) tu negocio. En este mensaje te dejo un brief en borrador con lo que ya sé; lo que falte queda marcado y lo cerramos sobre ese brief."

2. Escribe el brief en el propio mensaje, con este encabezado literal y en su propia línea. Si además puedes crear archivos, adjunta el DOCX; el archivo no sustituye al texto.

```
BRIEF INICIAL (borrador)
```

Dentro del brief no uses signos de interrogación: las preguntas van debajo. Rellena solo lo que ya conste. Cada hueco lleva la marca `[PENDIENTE]`. No inventes cifras, nombres ni una ruta por si acaso, y no escribas que el brief llegará más adelante: este es el brief.

```
BRIEF INICIAL (borrador)
Persona: [nombre, u omite la línea si no lo ha dicho] · [oficio] · [ciudad] · [situación laboral]
Situación: [lo que ha dicho, en una línea]
Ruta: [ruta y por qué, o PENDIENTE si no hay señal]
Calibración: [una de las cuatro de abajo, o PENDIENTE]
Objetivo y medios: [objetivo a 12 meses, horas por semana, presupuesto]
Ya tiene: [clientes, marca, web, herramientas]
Diferencial: [experiencia o conocimiento que le distingue, o PENDIENTE]
Secuencia: [módulos de la ruta según config/route-profiles.md, o PENDIENTE]
Siguiente paso: [primer módulo de la ruta, o confirmar la ruta]
```

Calibración, sin abrir otros módulos: arranca de cero (sin clientes ni portfolio); por cuenta propia sin estructura (clientes, sin proceso ni precios formales); profesional con base (clientes, marca y algo de portfolio); veterano que escala (factura de forma regular). La tabla completa está en `modules/02-negocio-oferta.md`, para cuando toque M2.

3. Debajo del brief, como máximo tres preguntas, y solo si cambian la ruta o el primer módulo. Elige entre estas, y solo las que el brief tenga en `[PENDIENTE]`:

- Si no hay ninguna señal de situación: el menú de abajo. Cuenta como una sola pregunta y es la única de ese turno.
- Si hay dos rutas posibles: una sola desambiguación. "¿Tienes clientes que te paguen de forma regular?" (varios: Escalador; pocos y sin sistema: Activador; ninguno: Definidor, Redefinidor o Explorador) o "¿Tienes claro qué ofreces y a quién?" (sí, pero no llegan: Activador; sí, pero quiero cambiar: Redefinidor; no: Explorador).
- Si la ruta está clara y falta el contexto de esa ruta (tabla de la sección siguiente) y ese dato cambia el primer módulo: esa pregunta.
- Si faltan horas, presupuesto u objetivo y no están en el mensaje: una sola, la que más cambie el plan.

Si la situación ya está clara, nómbrala dentro del brief y no enseñes el menú. No preguntes nombre, oficio, ciudad ni situación si ya constan. En este turno no preguntes el diferencial, las herramientas, la marca, la red, los descartes ni los factores humanos: si faltan, quedan en `[PENDIENTE]` dentro del brief.

Menú, solo cuando el primer mensaje no trae situación. Correspondencia: a) Escalador, b) Activador, c) Redefinidor, d) Definidor, e) Explorador.

> ¿Cuál de estas situaciones se parece más a la tuya?
> - a) Ya facturo de forma regular y quiero crecer, productizar o subir precios
> - b) Lo tengo todo montado, pero no me entran clientes
> - c) Tengo negocio o clientes, pero quiero cambiar de dirección
> - d) Tengo una idea clara, pero no he arrancado
> - e) Sé hacer cosas, pero no sé qué negocio montar

4. Crea la ficha de progreso en este mismo turno, con los campos vacíos que hagan falta (`config/state-schema.md`). En "Dónde estamos" di que el brief es un borrador.

## Después del brief

Cuando la persona responda, reescribe el brief con lo nuevo (sigue en borrador hasta el checkpoint) y, en ese mismo mensaje, pregunta juntos los huecos que sigan en `[PENDIENTE]` y que su ruta necesite. No los repartas en varios turnos.

- **Contexto de la ruta**, si no se preguntó ya y sigue vacío:

| Ruta | Pregunta |
|---|---|
| Escalador | "¿Cuánto facturas al mes, cuántos clientes tienes y cuál es tu ticket medio? Valen cifras aproximadas." |
| Activador | "¿Qué tienes montado (oferta, web, marca, contratos) y qué has probado para conseguir clientes? ¿Qué pasó?" |
| Redefinidor | "¿Qué tienes ahora (clientes, facturación, marca, web) y qué quieres cambiar?" |
| Definidor | "En una frase: ¿qué problema quieres resolver y para quién?" |
| Explorador | "¿Qué sabes hacer bien? No pienses en negocio: qué te piden, qué se te da mejor que a la media, qué disfrutas." |

- **Diferencial**, si sigue en `[PENDIENTE]`: qué experiencia, formación o conocimiento le distingue.
- **Contexto operativo**, en el mismo mensaje, con la indicación de que responda lo que sepa: a quién vende o venderá (empresas y profesionales, particulares o ambos) y si la actividad exige título, colegiación o autorización; red (clientes, contactos del sector o conversaciones abiertas); objetivo a 12 meses, si faltaba (Escalador: crecimiento en %, clientes o facturación; el resto: complementar ingresos, menos de 2.000 €/mes; sustituir un sueldo, 2.000-4.000 €; construir empresa, 4.000-10.000 €; crecer con equipo, más de 10.000 €); situación laboral, horas por semana y presupuesto inicial, si faltaban; si trabaja solo o con equipo; marca y web, si no lo ha contado; herramientas y suscripciones que ya usa (hosting, dominio, facturación, CRM, diseño, correo), para no recomendar duplicados.
- **Factores humanos**: como mucho tres preguntas, todas opcionales, siguiendo `layers/factores-humanos.md`. Las más útiles: su mayor bloqueo ahora mismo, si ha intentado algo parecido antes y qué aprendió, y cuántos meses puede sostenerse sin que esto genere ingresos.
- **Descartes**: sectores, clientes o servicios que ya ha descartado.

Si responde a medias, o dice que sigas con lo que hay, no abras otra ronda: estímalo con la persona o deja `[PENDIENTE]` y pasa al diagnóstico.

## Diagnóstico

Cuando el brief ya recoge ese turno de huecos (o la persona prefiere seguir con huecos), presenta el diagnóstico:

```
DIAGNÓSTICO INICIAL
Perfil: [nombre] · Ruta: [ruta] · Calibración: [nivel de la tabla de M2]
Punto de partida: [una línea]
Fortaleza principal: [la más clara]
Riesgo principal: [el más evidente]
Lo que ajusta el plan: [urgencia, bloqueo o experiencia previa que cambia algo]
Herramientas que ya tiene: [resumen]
Secuencia: [módulos de la ruta según config/route-profiles.md, con lo que se salta y por qué]
```

Actualiza el brief con lo cerrado y actualiza la ficha. Lo que siga sin dato permanece `[PENDIENTE]`.

## Entregable

El brief inicial en borrador es el entregable del primer turno: en el mensaje y, si el entorno puede, también en DOCX. Al pasar el checkpoint, entrega el brief de negocio revisado (DOCX, o Markdown si no hay archivos) y la ficha actualizada. El brief cerrado incluye perfil, diagnóstico, ruta y por qué, ajustes al plan por factores humanos (sin detalles personales), herramientas existentes y secuencia de módulos. El borrador es la versión 1; el brief cerrado sube la versión.

## Checkpoint

> Este es tu punto de partida y el camino que te propongo. ¿Te ves reflejado/a? ¿Ajustamos algo antes de empezar con la investigación de mercado?
