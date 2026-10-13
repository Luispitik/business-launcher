# Business Launcher

**Una skill de Claude que te entrevista, entiende en qué punto está tu negocio y construye contigo el plan completo: del "no sé qué vender" o "no me entra ni un cliente" a una oferta con precio, documentos de arranque y un plan de 90 días.**

En español, pensada para España y de código abierto (MIT). Presentada en el episodio 3 de [Más allá del prompt](https://podcastmadp.com/).

| Si te suena… | Ruta | Qué hace contigo primero |
|---|---|---|
| "Ya facturo y quiero escalar" | **Escalador** | Productizar, subir precios y sistematizar |
| "Lo tengo todo montado y no entra ni un cliente" | **Activador** | Diagnosticar por qué y diseñar tu captación |
| "El negocio existe, pero quiero pivotar" | **Redefinidor** | Rediseñar sin perder los ingresos actuales |
| "Tengo la idea clara, pero no he arrancado" | **Definidor** | Mercado, oferta y precio para empezar con orden |
| "Tengo habilidades, pero ninguna dirección" | **Explorador** | Comparar 2-3 nichos reales y validar con conversaciones antes de construir |

**Empieza así:**

```
business launcher. Soy [profesión] en [ciudad]. Ahora mismo [tu situación en una frase].
Se me da bien [...]. Puedo dedicarle [horas a la semana].
```

No monta tu web, no tramita tu alta ni sustituye a una gestoría o a un abogado: los documentos son borradores de trabajo.

---

## Instalación

### claude.ai y Claude Cowork

1. En **Ajustes → Capacidades**, activa **Ejecución de código y creación de archivos**. Las skills están disponibles en todos los planes, también en el gratuito; en Team y Enterprise las activa la persona administradora.
2. Descarga **`business-launcher.zip`** de la [última Release](https://github.com/Luispitik/business-launcher/releases/latest). No uses el botón "Code → Download ZIP" de GitHub: crea una carpeta `business-launcher-master` y la subida falla porque el nombre de la carpeta no coincide con el de la skill.
3. En **Personalizar → Skills**, pulsa **+ → Crear skill → Subir una skill** y elige el ZIP.

Cowork usa las skills activadas en tu cuenta de claude.ai: no hace falta instalarla aparte. Abre una carpeta de trabajo y tu ficha de progreso se guardará ahí.

### Claude Code

Como plugin, con actualizaciones:

```
/plugin marketplace add Luispitik/business-launcher
/plugin install business-launcher@salgadoia-skills
```

O clonando el repositorio en tus skills personales:

```bash
git clone https://github.com/Luispitik/business-launcher.git ~/.claude/skills/business-launcher
```

Instala una sola copia por entorno. Para los entregables en Word, instala también la skill `docx` (`/plugin install document-skills@anthropic-agent-skills`); sin ella recibirás Markdown o HTML.

---

## Cómo funciona

La entrevista inicial detecta tu ruta y adapta el recorrido. Según la ruta, pasa por estas fases:

| # | Fase | Qué produce |
|---|---|---|
| 0 | Entrevista | Ruta, perfil calibrado y brief de negocio |
| 1 | Investigación de mercado | Competidores, precios reales con su fuente, huecos y canales |
| 2 | Modelo de negocio y oferta | Cliente ideal, propuesta de valor, servicios y precios calibrados |
| 3 | Marca | Nombre, tono, identidad visual (completa o mínima) |
| 4 | Documentación de arranque | Checklist de obligaciones legales y fiscales y documentos comerciales |
| 5 | Plan de 90 días | Semanas con tareas, herramientas verificadas y métricas |
| 6 | Prompt para tu web | Instrucción para que un agente o tu constructor web la monte |
| 7 | Captación y ventas | Diagnóstico y sistema para conseguir clientes (completo o básico) |

En cada fase recibes un entregable y nada avanza sin que lo confirmes. Las rutas cambian el orden y el alcance: en Activador la captación va antes que la oferta; en Explorador se valida con conversaciones antes de invertir en marca y contratos.

**Lo que la diferencia:**

- **Precios calibrados a tu perfil real.** A quien arranca no se le ponen precios de veterano, y cada precio se ancla en comparables del mercado, no en lo que "suena bien". Los modelos de lenguaje tienden a inflar precios y plazos; la skill lo compensa con datos.
- **Datos verificados.** Precios de herramientas y competidores se comprueban con la búsqueda web y llevan fuente y fecha. Si no hay búsqueda web, se marcan `[VERIFICAR]` en lugar de inventarse.
- **Lo legal, investigado cada vez.** La skill no trae respuestas legales escritas: en cada uso investiga cada punto (altas, impuestos, facturación, protección de datos, publicidad…) en la fuente oficial, lo contrasta con una segunda fuente y te da ambas con fecha. Lo que no se puede verificar queda marcado para tu gestoría o tu abogado.
- **Factores humanos.** Urgencia económica, bloqueos y experiencias previas cambian el plan: con un mes de colchón, el plan es de 30 días y busca ingresos ya. Es pragmático, no terapia.
- **Debate, no validación.** Propone, cuestiona su propia propuesta y te señala lo que no encaja con lo que has contado.

### Tu ficha de progreso

El proceso se hace en varias sesiones. Tu progreso vive en un archivo, `ficha-business-launcher.md`, que es tuyo:

- En **Claude Code y Cowork** se guarda solo en tu carpeta de trabajo.
- En **claude.ai**, la skill te entrega la ficha actualizada al cerrar cada fase. Trabaja dentro de un Proyecto (por ejemplo, "Mi negocio") y súbela allí; la próxima vez retomará donde lo dejaste.

La ficha no guarda tu relato personal ni datos de terceros; solo lo necesario para continuar.

---

## Qué no hace

- **No implementa nada técnico.** La fase 6 genera el prompt para construir tu web; ejecutarlo es otro trabajo.
- **No hace trámites** ni sustituye a una gestoría o a un abogado. Los documentos son borradores de trabajo para revisar con un profesional, y en sectores regulados la skill lo advierte y no improvisa normativa.
- **No te consigue clientes.** Diseña el sistema; ejecutarlo son tus semanas.
- **No valida tu idea por ti.** Investiga y te dice lo que encuentra; validar es hablar con clientes.

---

## Estructura

```
SKILL.md                     Orquestador
config/route-profiles.md     Rutas: secuencia de fases y ajustes
config/state-schema.md       Ficha de progreso
layers/factores-humanos.md   Ajustes por urgencia, bloqueos y experiencias previas
modules/00-intake.md … 07-captacion.md   Una fase por archivo, que se lee cuando toca
evals/                       Casos de prueba de comportamiento
.claude-plugin/              Manifiesto de plugin y marketplace para Claude Code
```

Cambios entre versiones: [CHANGELOG.md](CHANGELOG.md).

---

## Licencia

**MIT**: uso, modificación y redistribución libres, también comerciales, conservando el aviso de copyright. Ver [LICENSE](LICENSE).

---

Creado por **Luis Salgado** · [SalgadoIA](https://salgadoia.com) · Sigue tu curiosidad.
