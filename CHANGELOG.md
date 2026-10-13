# Cambios

## 4.0.0 — 2026-10-13

Versión adaptada a los modelos actuales de Claude (Opus 5.5, Fable 5.1, Sonnet 5.5) y a los tres entornos donde se usa la skill.

### Cambia el formato del progreso
- La persistencia en el almacenamiento de artifacts (`window.storage` + `sendPrompt`) se sustituye por una **ficha de progreso** en Markdown (`ficha-business-launcher.md`). El almacenamiento de cada artifact es independiente y no llegaba a la conversación siguiente, y Claude Code y Cowork no tienen artifacts. La ficha se guarda sola en Claude Code y Cowork y se entrega como archivo en claude.ai.
- La ficha ya no guarda el estado emocional ni el relato personal: solo el ajuste al plan y el nivel de urgencia.
- Los módulos se identifican siempre como M0-M7. Las fichas 3.x se convierten al retomarlas.

### Rutas y alcance
- Las cinco rutas vuelven a estar al mismo nivel, como se presentó en Más allá del prompt: Escalador, Activador, Redefinidor, Definidor y Explorador.
- Una única tabla de rutas en `config/route-profiles.md` decide qué módulos toca cada una; se eliminan tres versiones contradictorias sobre cuándo aplica M7.
- M7 básico (red de contactos y guion de descubrimiento) entra en el primer sprint de Definidor y Explorador.
- Explorador valida antes de invertir: marca mínima y checklist de arranque; marca y documentos completos tras validar.
- En Activador, M7 ya no depende de resultados de M2 y M4 que aún no existen.

### Comportamiento
- Instrucciones reescritas para modelos que siguen el texto al pie de la letra: sin mayúsculas de presión ni "REGLA CRÍTICA", cada regla una vez y con su motivo, y paradas solo en los checkpoints.
- La entrevista no vuelve a preguntar lo que la persona ya ha contado, agrupa el contexto operativo en un mensaje y limita los factores humanos a tres preguntas opcionales.
- Sin búsqueda web, los datos se marcan `[VERIFICAR]` en lugar de completarse de memoria. La disponibilidad de dominio y marca se comprueba en el registrador, no con una búsqueda.
- Nueva regla para malestar intenso: reconocerlo, no empujar tareas, sugerir apoyo profesional (024) y ofrecer pausa.
- M2 distingue clientes empresa y particulares, condiciona los servicios técnicos al perfil y, en Escalador, trata cómo comunicar la subida de precios.
- M6 elige herramienta según el perfil (constructor sin código o Claude Code) y evita los estilos visuales por defecto de las webs generadas.

### Contenido legal y comercial
- **Lo legal se investiga en cada uso.** La skill ya no afirma normas, cuotas, plazos ni fechas: indica qué hay que comprobar, y el modelo lo investiga punto por punto en fuente oficial, lo contrasta con una segunda fuente y cita ambas con la fecha. Si no coinciden, hay un cambio anunciado sin publicar o no se puede verificar, se marca `[VERIFICAR con gestoría/abogado]`.
- M4 pasa a "Documentación de arranque": checklist de puntos a verificar (forma de operar, altas, compatibilidades, impuestos y facturación, protección de datos, actividad regulada, uso de IA, nombre y local) y documentos distintos para clientes empresa y particulares, todos con la nota de borrador generado con IA.
- M7 deja de proponer el correo comercial en frío y la automatización de LinkedIn; antes de proponer un canal se verifica la norma vigente y, mientras tanto, se aplica un criterio prudente. Las métricas se presentan como hipótesis.
- M2 añade el precio suelo, exige comparables con fuente para subir precios y fija condiciones para testimonios y precios de fundador. M6 prohíbe la prueba social inventada y construye el bloque legal de la web a partir de requisitos verificados.

### Empaquetado
- Frontmatter conforme a la especificación de Agent Skills (`name`, `description`, `license`, `compatibility`, `metadata`).
- Manifiesto de plugin y marketplace para instalar con `/plugin` en Claude Code.
- Release con `business-launcher.zip` para subir a claude.ai.
- Se retiran las dependencias `pptx` (no se usaba) y `lead-research-brief` (privada).
- Casos de prueba de comportamiento en `evals/`.

## 3.0.0 — 2026-03-16

Primera versión pública: 5 rutas, 8 módulos, capa de factores humanos y persistencia mediante artifacts.
