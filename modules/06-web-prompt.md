# Módulo 06 — Prompt multiagente para la web (OPCIONAL)

## Objetivo

Generar un prompt autocontenido que el usuario pueda pegar en Claude Code para
construir su web profesional sin saber programar. Incluye una fase previa de
**dirección visual** donde el usuario elige entre alternativas estéticas o
sube referencias propias antes de que se genere una sola línea de código.

## Pre-requisitos

- Módulos M2 (oferta) y M3 (marca) completados.
- Si M3 fue saltado, usar datos mínimos de marca del intake.

## FASE 0 — Dirección visual (ANTES de generar el prompt)

Esta fase es **interactiva y conversacional**. No se genera el prompt web
hasta que el usuario haya validado una dirección visual concreta.

### Paso 1 — Recoger preferencias base

Preguntar al usuario:

> "Antes de generar el prompt para tu web, necesito entender qué estética
> te representa. Tenemos tres caminos:"
>
> **A)** Te muestro 3 propuestas visuales distintas y eliges la que más encaja.
> **B)** Tú me pasas 1-3 webs de referencia que te gusten y construimos sobre eso.
> **C)** Combinamos: te muestro opciones Y tú aportas referencias.

### Paso 2A — Propuestas visuales generadas (si elige A o C)

Generar **3 alternativas visuales radicalmente distintas** como HTML interactivo.
Cada alternativa incluye:

```
ALTERNATIVA [N] — [Nombre descriptivo]

Filosofía: [1 frase — qué transmite esta dirección]
Estética: [minimalista / editorial / corporativa / bold / tech / artística]
Paleta aplicada: [Cómo se adaptan los colores del M3 a esta estética]
Layout hero: [Descripción de la sección principal]
Tipografía: [Cómo se usa la jerarquía tipográfica del M3]
Espaciado: [Aireado / compacto / asimétrico]
Animaciones: [Ninguna / sutiles / expresivas]
Referencia mental: [Web conocida con estética similar — solo como ancla]
```

**Las 3 deben ser radicalmente distintas**, no variaciones del mismo tema.
Ejemplo para un consultor de IA:

1. **Precision Dark** — Fondo oscuro, monospace en acentos, datos visibles, expertise técnico. Ref: stripe.com
2. **Editorial Cálida** — Fondo crema, serif elegante, espacio en blanco, cercanía experta. Ref: julian.com
3. **Corporate Bold** — Fondo blanco, bloques de color, CTAs grandes, confianza empresarial. Ref: mckinsey.com

Generar cada alternativa como **mockup visual en HTML** (hero + sección servicios)
para que el usuario vea la diferencia, no solo la lea.

### Paso 2B — Referencias del usuario (si elige B o C)

Si el usuario sube o comparte URLs de referencia:

1. Analizar cada referencia (con web_fetch si es URL, o leer imagen si sube captura).
2. Extraer: paleta, layout, tipografía, espaciado, tono, elementos diferenciadores.
3. Presentar síntesis:

```
📋 ANÁLISIS DE TUS REFERENCIAS

Referencia 1: [url]
- Lo que funciona para tu negocio: [elementos aplicables]
- Lo que no encaja con tu ICP/marca: [elementos descartables]
- Elemento clave a incorporar: [el más relevante]

SÍNTESIS — Tu dirección visual combina:
- [Elemento X] de la referencia 1
- [Elemento Y] de la referencia 2
- Adaptado a tu paleta y tipografía del M3
```

### Paso 3 — Validación

> "Esta es tu dirección visual: [resumen en 3 líneas].
> ¿Es exactamente lo que quieres o ajustamos algo?"

Iterar hasta confirmación. No avanzar sin "sí, adelante".

### Persistir dirección visual

```json
{
  "visual_direction": {
    "method": "alternatives | references | combined",
    "chosen_alternative": null,
    "reference_urls": [],
    "aesthetic": "",
    "key_elements": [],
    "confirmed_at": "ISO 8601"
  }
}
```

## Estructura del prompt generado

Solo se genera tras confirmar dirección visual.

```markdown
# INSTRUCCIÓN PARA CLAUDE CODE — Web de [Nombre]

## CONTEXTO DEL PROYECTO
[Datos del negocio, ICP, propuesta de valor — del M2]

## IDENTIDAD VISUAL
[Paleta, tipografía, tono — del M3]

## DIRECCIÓN VISUAL VALIDADA
[Estética elegida, elementos clave, referencia mental]
[Si hay URLs de referencia: elementos concretos a replicar y cuáles no]

Instrucción para Claude Code:
"ANTES de construir ninguna página, genera 1 página de prueba
(hero + sección de servicios + footer) con la dirección visual descrita.
Muéstramela para validación. Solo tras mi OK, construye el resto."

## STACK TÉCNICO
Next.js 14 + TypeScript + Tailwind CSS + App Router
Deploy: Vercel
[Integraciones según el negocio]

## PÁGINAS A CONSTRUIR
[Lista adaptada al modelo de negocio del M2]
Para cada página:
- Propósito y objetivo de conversión
- Secciones con contenido real (nunca lorem ipsum)
- CTA principal
- Elementos visuales según dirección validada

## INTEGRACIONES
[Según necesidad:]
- Formulario de contacto (webhook n8n / Formspree / nativo)
- Chat widget (Anthropic API / Crisp / Tawk)
- Calendario (Calendly / Cal.com embed)
- Analytics (Plausible / GA4)

## BRANDING
[Logo del M3 — integración en header, footer, favicon, OG image]

## SEO
[Structured data: LocalBusiness, Service, Person — datos reales]
[Meta tags por página + Open Graph]

## LEGAL (RGPD)
[Aviso legal, privacidad, cookies — datos reales del usuario]

## BLOG
[Si aplica: estrategia, categorías, primeros 3 títulos]

## DEPLOY
[Vercel CLI → repo → dominio → SSL]

## CHECKLIST FINAL
[ ] Responsive mobile/tablet/desktop
[ ] Lighthouse >90 en todas las métricas
[ ] Páginas legales completas
[ ] Formulario funcional y testeado
[ ] Favicon y OG images
[ ] Analytics instalado
[ ] SSL activo
[ ] Sitemap.xml + robots.txt
```

## Entregables M6

1. **MD** — "Prompt-Web-[Nombre]-ClaudeCode.md" (listo para copiar y pegar)
2. **HTML** — "direccion-visual-[Nombre].html" (mockups de las alternativas presentadas)

## Persistencia

Registrar entregables. Marcar módulo como completado.

## Nota

Módulo opcional en todas las rutas. Si el usuario no lo necesita, saltar sin insistir.
