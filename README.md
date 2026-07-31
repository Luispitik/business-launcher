# Business Launcher

**Para el profesional o despacho que ya factura y quiere sistematizar una línea de
servicio nueva.** No es un curso de emprendimiento ni una plantilla de plan de negocio: es
una conversación guiada con Claude que termina en oferta definida, precios justificados,
documentos contractuales y un plan de 90 días con fechas.

Si ya tienes clientes y lo que te falta es convertir "eso que haces bien" en un servicio
con nombre, precio y proceso repetible, esto está hecho para ti.

---

## Por qué el encuadre importa

La mayoría de herramientas de este tipo apuntan a quien todavía no ha facturado nunca. El
problema de ese público no es la estructura: es que aún no sabe si alguien pagará. Ninguna
plantilla resuelve eso.

Business Launcher asume lo contrario — que ya tienes demanda, criterio y algún cliente — y
ataca lo que de verdad frena a un profesional en ese punto:

- Cobra por horas y quiere cobrar por resultado, pero no sabe cómo empaquetarlo
- Tiene tres servicios que en realidad son uno mal explicado tres veces
- Sabe que sus precios están bajos y no tiene con qué justificar la subida
- Hace propuestas desde cero cada vez, en Word, a las once de la noche
- Tiene la línea de servicio nueva en la cabeza desde hace meses y sin arrancar

---

## Las 5 rutas adaptativas

El intake detecta tu situación en las primeras cuatro preguntas y reordena el proceso
entero. No todas las rutas ejecutan los mismos módulos ni en el mismo orden.

| Ruta | Situación | Foco del proceso |
|---|---|---|
| **Escalador** | Ya facturas de forma regular | Productizar, subir precios, sistematizar |
| **Activador** | Todo montado, no entran clientes | Sistema de captación (M7 pasa al centro) |
| **Redefinidor** | Negocio existente, quieres pivotar | Rediseño aprovechando activos, sin perder ingresos |
| **Definidor** | Idea clara, sin ejecutar | Estructura paso a paso |
| **Explorador** | Habilidades sí, dirección no | Descubrimiento antes de construir |

Las tres primeras son el caso central. Las dos últimas siguen soportadas y funcionan, pero
si estás ahí, lo que necesitas primero son diez conversaciones con clientes potenciales, no
un plan — y la ruta Explorador te va a llevar exactamente a eso.

**La ruta se puede reasignar a mitad.** Si durante el proceso queda claro que un
"Definidor" en realidad ya tiene un negocio que redefinir, se cambia y se registra el
cambio.

---

## Las 8 fases

| # | Fase | Qué produce |
|---|---|---|
| 0 | **Intake adaptativo** | Ruta detectada, perfil calibrado, brief de negocio |
| 1 | **Investigación de mercado** | Competidores, precios reales, huecos, canales |
| 2 | **Modelo de negocio y oferta** | ICP, propuesta de valor, catálogo con pricing y márgenes |
| 3 | **Identidad de marca** | Naming, logo, paleta, tipografía, manual |
| 4 | **Documentación legal** | Propuesta tipo, NDA, DPA, contrato de servicios |
| 5 | **Plan de 90 días** | 13 semanas con tareas, herramientas y métricas |
| 6 | **Prompt web** | Instrucción lista para que un agente construya tu web |
| 7 | **Captación y ventas** | Sistema de adquisición completo |

Según la ruta, algunas fases se saltan (si ya tienes marca sólida, la 3 no se ejecuta) y
otras cambian de orden (en Activador, la 7 va antes que la 2).

### Tres detalles que marcan la diferencia

**El pricing se calibra al perfil real, no al ideal.** Hay una tabla obligatoria que
clasifica al usuario en cuatro niveles y ancla el precio al cuartil de mercado que le
corresponde. A quien arranca no se le ponen precios de veterano: el síndrome del impostor
ya frena bastante, y un precio que no puedes decir en voz alta sin tartamudear no se cobra.

**Los precios de herramientas se verifican con búsqueda web, siempre.** Nunca de memoria.
Un stack recomendado con precios de hace dos años es un presupuesto roto.

**Hay una capa de factores humanos** que se activa en el intake, en el diseño de la oferta
y en el plan de 90 días. Miedo a vender, urgencia financiera, fracasos previos, resistencia
a delegar. No es decoración: cambia el plan. Con colchón de tres meses, el primer sprint
apunta a ingreso en 30 días; sin él, el plan es otro.

---

## Qué NO hace

Decirlo genera más confianza que ocultarlo:

- **No incluye implementación técnica.** Ni código, ni despliegue, ni configuración de
  herramientas, ni montar la web. La fase 6 genera el *prompt* para construirla; ejecutarlo
  es otro trabajo con otra herramienta.
- **No constituye tu empresa** ni hace trámites: no es una gestoría.
- **Los documentos legales son borradores de trabajo.** Están redactados para legislación
  española y sirven de base sólida, pero no sustituyen la revisión de un abogado. Para un
  sector regulado, el propio módulo lo advierte y no improvisa regulación.
- **No te consigue clientes.** Diseña el sistema de captación; ejecutarlo son tus semanas.
- **No valida tu idea por ti.** Investiga el mercado y te dice lo que encuentra. Si lo que
  encuentra es malo, te lo dirá — pero validar es hablar con clientes, no leer un informe.
- **No inventa datos.** Si falta un número, se estima juntos o se marca `[PENDIENTE]`.

---

## Instalación

### Claude.ai (recomendado)

Ajustes → Capacidades → Skills → crear skill nueva. Pega `SKILL.md` como contenido
principal y sube el resto de ficheros conservando la estructura de carpetas.

### Claude Code

```bash
git clone https://github.com/Luispitik/business-launcher.git ~/.claude/skills/business-launcher
```

### Skills complementarias

| Skill | Para qué | Sin ella |
|---|---|---|
| `docx` | Todos los entregables en Word | Recibes el contenido en chat, no en fichero |
| `pptx` | Presentaciones | Se omiten |
| `canvas-design` | Logo e identidad visual | El módulo de marca entrega criterio, no artes finales |

**Sobre la persistencia entre sesiones:** el estado se guarda de forma invisible mediante
artifacts HTML con almacenamiento de navegador, así que funciona en claude.ai. En otros
entornos puede no estar disponible; en ese caso la skill lo detecta, avisa y continúa —
simplemente el progreso vale solo para esa sesión.

---

## Uso

```
business launcher
```

También arranca con "quiero sistematizar un servicio", "necesito clientes", "quiero
escalar mi negocio" o "ayúdame a lanzar mi empresa".

El intake dura unos 15 minutos y hace las preguntas de una en una. A partir de ahí, cada
fase termina en un checkpoint: nada avanza sin que lo confirmes.

---

## Cómo se comporta

No es un generador de documentos con pasos intermedios. La regla de diseño es que **el
valor está en las preguntas que provoca, no en los ficheros que produce**, y eso se traduce
en comportamientos concretos:

- Propone, y después cuestiona su propia propuesta
- Si detecta que algo contradice lo que dijiste antes, lo corrige **antes** de enseñártelo,
  en vez de esperar a que lo detectes tú
- Antes de cerrar el catálogo, propone servicios complementarios que no habías mencionado
- Te pregunta si el precio óptimo te incomoda decirlo en voz alta, y si la respuesta es sí,
  trabaja la justificación con datos de mercado

Si aceptas todo lo que propone sin discutir nada, algo va mal. El manual lo dice
literalmente.

---

## Entregables

| Entregable | Formato | Fase |
|---|---|---|
| Brief de negocio | DOCX | 0 |
| Investigación de mercado | HTML | 1 |
| Modelo de negocio y oferta | DOCX | 2 |
| Manual de marca + logo | DOCX + PNG/SVG | 3 |
| Propuesta comercial tipo | DOCX | 4 |
| NDA | DOCX | 4 |
| DPA (RGPD) | DOCX | 4 |
| Contrato de prestación de servicios | DOCX | 4 |
| Plan de 90 días | DOCX | 5 |
| Prompt web + mockups | MD + HTML | 6 |
| Estrategia de captación | DOCX | 7 |

Cuáles recibes depende de tu ruta: un Escalador con marca y contratos ya hechos no genera
las fases 3 y 4, las revisa.

---

## Arquitectura

```
SKILL.md                        Orquestador
config/
  route-profiles.md             Las 5 rutas con sus secuencias y ajustes
  state-schema.md               Persistencia invisible entre sesiones
layers/
  factores-humanos.md           Capa transversal (miedos, urgencia, bloqueos)
modules/
  00-intake.md                  Intake adaptativo con árbol de decisión
  01-investigacion.md           Investigación de mercado
  02-negocio-oferta.md          Modelo, oferta y pricing calibrado
  03-marca.md                   Identidad de marca
  04-legal.md                   Pack documental
  05-plan-90-dias.md            Plan accionable
  06-web-prompt.md              Prompt web con dirección visual
  07-captacion.md               Estrategia de captación y ventas
```

Cada módulo se lee cuando toca, no todos de golpe. Es lo que permite que un proceso de ocho
fases quepa en una conversación sin quedarse sin contexto a la mitad.

---

## Licencia

**MIT** — uso, modificación y redistribución libres, incluso comerciales. La única
condición es conservar el aviso de copyright.

Copyright (c) 2026 Luis Salgado. Ver [LICENSE](./LICENSE).

---

Creado por **Luis Salgado** — [salgadoia.com](https://salgadoia.com)
