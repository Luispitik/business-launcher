# Business Launcher v3 — Claude Skill

> Skill orquestadora para Claude que guía a un profesional desde una idea de negocio hasta una empresa operativa con identidad, oferta, precios, documentos comerciales y plan de acción 100% accionable.

**Fundado por [NorteIA](https://norteia.es) / [SalgadoIA](https://salgadoia.com)**

---

## Qué hace

Business Launcher es una skill para Claude (claude.ai) que actúa como socio estratégico de negocio. Convierte una conversación guiada en un pack completo de lanzamiento:

- **Intake adaptativo** — Detecta tu perfil (Explorador, Definidor, Redefinidor, Activador, Escalador) y adapta todo el proceso
- **Investigación de mercado** — Competidores, precios, huecos, canales de captación
- **Modelo de negocio y oferta** — ICP, propuesta de valor, catálogo de servicios con pricing calibrado
- **Identidad de marca** — Naming, logo, paleta, tipografía, manual de marca
- **Documentación legal** — Propuesta comercial, NDA, DPA, contrato de servicios
- **Plan de 90 días** — 13 semanas con tareas concretas, herramientas y métricas
- **Prompt web** — Instrucción lista para Claude Code que genera tu web profesional
- **Estrategia de captación** — Sistema completo de adquisición de clientes

## 5 rutas adaptativas

| Ruta | Perfil | Foco |
|------|--------|------|
| **Explorador** | No sabe qué negocio montar | Descubrimiento guiado |
| **Definidor** | Idea clara, no ha ejecutado | Estructura paso a paso |
| **Redefinidor** | Negocio existente, quiere pivotar | Rediseño con activos |
| **Activador** | Todo montado, sin clientes | Sistema de captación |
| **Escalador** | Ya factura, quiere crecer | Optimización y escalado |

## Arquitectura

```
SKILL.md                        → Orquestador principal
├── config/
│   ├── route-profiles.md       → 5 rutas adaptativas con secuencias
│   └── state-schema.md         → Persistencia invisible entre sesiones
├── layers/
│   └── factores-humanos.md     → Capa transversal (miedos, urgencia, bloqueos)
└── modules/
    ├── 00-intake.md            → Intake adaptativo con árbol de decisión
    ├── 01-investigacion.md     → Investigación de mercado
    ├── 02-negocio-oferta.md    → Modelo de negocio, oferta y pricing
    ├── 03-marca.md             → Identidad de marca
    ├── 04-legal.md             → Documentación comercial y legal
    ├── 05-plan-90-dias.md      → Plan de 90 días accionable
    ├── 06-web-prompt.md        → Prompt web con dirección visual
    └── 07-captacion.md         → Estrategia de captación y ventas
```

## Instalación

### En Claude.ai (Web)

1. Ve a **Personalizar** → **Skills**
2. Crea una nueva skill
3. Copia el contenido de `SKILL.md` como skill principal
4. Sube el resto de archivos manteniendo la estructura de carpetas

### En Claude Code (CLI)

```bash
# Clona el repositorio en tu directorio de skills
git clone https://github.com/Luispitik/business-launcher.git ~/.claude/skills/business-launcher
```

## Uso

Simplemente di a Claude cualquiera de estas frases:

- "Quiero montar un negocio"
- "No sé qué negocio montar"
- "Necesito clientes"
- "Quiero escalar mi negocio"
- "Ayúdame a lanzar mi empresa"
- "business launcher"

La skill se activa automáticamente y comienza el proceso guiado.

## Skills complementarias recomendadas

Para máximo rendimiento, Business Launcher funciona con estas skills:

| Skill | Para qué |
|-------|----------|
| `docx` | Generar documentos DOCX descargables |
| `pptx` | Generar presentaciones |
| `canvas-design` | Generar logos e identidad visual |
| `lead-research-brief` | Investigación profunda de mercado |

## Entregables que genera

| # | Entregable | Formato |
|---|-----------|---------|
| 1 | Brief de negocio | DOCX |
| 2 | Investigación de mercado | HTML interactivo |
| 3 | Modelo de negocio y oferta | DOCX |
| 4 | Manual de marca + logo | DOCX + PNG/SVG |
| 5 | Propuesta comercial tipo | DOCX |
| 6 | NDA | DOCX |
| 7 | DPA (RGPD) | DOCX |
| 8 | Contrato de servicios | DOCX |
| 9 | Plan de 90 días | DOCX |
| 10 | Prompt web + mockups | MD + HTML |
| 11 | Estrategia de captación | DOCX |

---

## Licencia

**CC BY-NC 4.0** — Puedes usar, modificar y redistribuir esta skill libremente para uso no comercial, siempre que:

1. **Cites al autor original**: NorteIA / SalgadoIA — Luis Salgado
2. **Incluyas un enlace** a este repositorio
3. **No lo uses con fines comerciales** — solo el autor original (NorteIA / SalgadoIA) puede usarlo comercialmente

Ver [LICENSE](./LICENSE) para el texto completo.

---

## Créditos

Creado por **Luis Salgado** — [NorteIA](https://norteia.es) / [SalgadoIA](https://salgadoia.com)

- Web: [salgadoia.com](https://salgadoia.com)
- LinkedIn: [linkedin.com/in/luis-salgado-salgadoia](https://linkedin.com/in/luis-salgado-salgadoia)

---

> **Quieres skills como esta, personalizadas para tu negocio?**
>
> Esta es la versión genérica y open-source de Business Launcher. En [NorteIA](https://norteia.es) diseñamos skills a medida para empresas: onboarding de clientes, generación de propuestas, automatización de procesos comerciales, y mucho más.
>
> **Contacta con nosotros en [norteia.es](https://norteia.es) o [salgadoia.com](https://salgadoia.com)**
