# M6 — Prompt para construir la web (opcional)

## Objetivo

Un prompt autocontenido para que un agente construya la web de la persona sin que tenga que programar, precedido de una dirección visual que la persona valida. Usa la oferta de M2 y la marca de M3 (o los datos mínimos del intake si M3 se saltó). Si no la necesita, se salta sin insistir.

## Elegir con qué se construye

Pregunta qué tiene: si ya usa un constructor sin código (Wix, Squarespace, WordPress, Framer…), el prompt se escribe para ese constructor o para mejorar su web actual. Si no tiene nada y quiere una web propia, el prompt es para Claude Code, y avisa de que necesitará cuentas en GitHub y en un servicio de alojamiento (por ejemplo, Vercel o Netlify), con el coste verificado.

## Dirección visual

La persona elige una de tres vías: le muestras tres propuestas, aporta de una a tres webs de referencia, o ambas.

**Propuestas.** Tres direcciones que difieran en estructura, densidad, tipografía y tono, no solo en color, derivadas de su sector, su cliente ideal y su marca: una asesoría de cumplimiento y un estudio de fisioterapia no deberían recibir las mismas tres. Evita los recursos que hacen que las webs generadas se parezcan entre sí (fondo crema o blanco roto, palabras en cursiva como acento en los titulares, etiquetas de sección numeradas "01/02/03", etiquetas en monoespaciada y botones en forma de píldora); si la marca pide alguno, úsalo a propósito y dilo. Para cada una: idea que transmite, paleta aplicada, sección principal, tipografía, espaciado y animación. Muéstralas como maqueta HTML (cabecera y sección de servicios) para que la persona las vea, no solo las lea.

**Referencias.** Analiza cada web (lectura de la URL o captura): qué encaja con su negocio, qué no y el elemento clave que incorporar, y presenta una síntesis adaptada a su marca.

No generes el prompt hasta que la persona confirme la dirección visual. Guárdala en la ficha como `visual_direction`:

```json
{ "method": "propuestas | referencias | ambas", "chosen": "", "reference_urls": [], "aesthetic": "", "key_elements": [] }
```

## Estructura del prompt

```markdown
# Web de [nombre]

## Contexto
[Negocio, cliente ideal y propuesta de valor de M2]

## Identidad
[Paleta, tipografía y tono de M3]

## Dirección visual validada
[Estética elegida y elementos clave; qué tomar de cada referencia y qué no]
[Recursos a evitar salvo que la dirección validada los pida: fondo crema o blanco roto, cursivas de acento en titulares, etiquetas numeradas "01/02/03", etiquetas en monoespaciada, botones en forma de píldora]

Antes de construir el resto, genera una página de prueba (cabecera, servicios y pie) con esta dirección y enséñamela. Sigue solo tras mi visto bueno.

## Herramienta y alojamiento
[Constructor elegido, o Claude Code con el stack que proponga para una web de servicios; dominio y alojamiento]

## Páginas
[Según el modelo de M2. Para cada una: objetivo, secciones con contenido real (nunca texto de relleno) y llamada a la acción]
No inventes testimonios, reseñas, logos de clientes, cifras de resultados, certificaciones ni premios: si no hay pruebas reales, quita la sección o márcala [PENDIENTE: prueba real].

## Integraciones
[Formulario de contacto, reserva de citas, analítica; solo las que necesite]

## Legal
[Aviso legal con los datos del titular que exige el art. 10 de la LSSI (incluido el colegio y el número si es profesión colegiada) y precios con impuestos.
Privacidad con información básica en cada formulario y una casilla separada y sin marcar para comunicaciones comerciales.
Banner de cookies con "Rechazar" en la primera capa, al mismo nivel que "Aceptar", y sin cargar cookies no técnicas (analítica, píxeles de anuncios) antes del consentimiento.
Si vende a particulares por internet: condiciones de contratación, información previa, derecho de desistimiento y la función de desistimiento si ya es exigible (comprobar su estado en España).
Si hay un asistente o chatbot de IA, que se identifique como IA.
Todos los textos legales, marcados [PENDIENTE: revisión profesional].]

## SEO
[Títulos y descripciones por página, datos estructurados del negocio, ficha local si atiende en un lugar]

## Comprobación final
[ ] Se ve bien en móvil, tableta y escritorio
[ ] Páginas legales completas, con los datos del titular
[ ] Banner de cookies con "Rechazar" en la primera capa y nada no técnico antes del consentimiento
[ ] Formulario probado, con información de privacidad y casilla comercial sin marcar
[ ] Toda prueba social es real y está documentada
[ ] Favicon e imagen para compartir en redes
[ ] Analítica instalada
[ ] HTTPS activo
[ ] Sitemap y robots.txt
```

## Entregables

- MD "prompt-web-[nombre].md", listo para copiar.
- HTML "direccion-visual-[nombre].html" con las maquetas presentadas.

Registra ambos en la ficha.
