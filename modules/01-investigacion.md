# Módulo 01 — Investigación de mercado

## Objetivo

Conocer el mercado al que va a entrar el usuario: tamaño, competidores, precios
de referencia, huecos de posicionamiento. Adaptado a la ruta del usuario.

## Pre-requisitos

- Lee `${CLAUDE_SKILL_DIR}/config/route-profiles.md` para ajustes por ruta.
- Si tienes la skill `lead-research-brief` instalada, lee su SKILL.md antes de ejecutar.
- Cargar `user_profile` del estado persistido.

## Ejecución por ruta

### EXPLORADOR — Investigación exploratoria multi-nicho

El Explorador no tiene un nicho definido. Investigar 2-3 nichos potenciales
derivados de sus habilidades (P3 del intake).

Para cada nicho:
1. Buscar con web_search: competidores (3-5 por nicho), precios, tendencias.
2. Evaluar demanda vs competencia.
3. Identificar hueco de posicionamiento.

Generar **tabla comparativa de nichos**:

| Criterio | Nicho A | Nicho B | Nicho C |
|----------|---------|---------|---------|
| Demanda estimada | | | |
| Nivel de competencia | | | |
| Rango de precios | | | |
| Barrera de entrada | | | |
| Afinidad con su perfil | | | |
| Time-to-first-sale estimado | | | |
| **Puntuación (1-10)** | | | |

Tras la tabla, recomendar un nicho y preguntar: "De estas 3 opciones, ¿cuál
te genera más energía y menos resistencia?" Solo avanzar con la elegida.

### DEFINIDOR — Investigación completa de un nicho

Investigación estándar, un solo nicho:
1. Competidores directos (mínimo 5) con web_search.
2. Precios de mercado por tipo de servicio.
3. Tendencias del sector.
4. Huecos no cubiertos.

### REDEFINIDOR — Investigación comparativa

Doble investigación:
1. Mercado actual (de dónde viene): competidores, posición actual del usuario.
2. Mercado objetivo (adónde va): misma estructura que Definidor.
3. Análisis de transferibilidad: qué activos del mercado actual son útiles en el nuevo.

### ACTIVADOR — Investigación de canales de captación

No investiga el mercado en abstracto — investiga **dónde están los clientes
y cómo llegar a ellos**:
1. ¿Dónde pasa tiempo el ICP? (LinkedIn, comunidades, eventos, foros, grupos...).
2. ¿Qué contenido consume? (newsletters, podcasts, blogs, YouTube...).
3. ¿Quién ya le vende servicios complementarios y cómo capta? (partnerships potenciales).
4. Competidores directos: ¿qué canales de captación usan? ¿Tienen presencia activa en redes, content marketing, cold outreach?
5. Volumen de búsqueda de los problemas que resuelve el usuario (validar demanda).

### ESCALADOR — Benchmarking competitivo

Centrado en pricing y posicionamiento:
1. Top 10 competidores directos con precios visibles.
2. Análisis de pricing: ¿dónde está el usuario vs mercado?
3. Servicios premium que el usuario no ofrece y podría ofrecer.
4. Estrategias de diferenciación de los líderes del mercado.

## Entregable M1

**HTML interactivo** con dos pestañas (o tres para Explorador):

- **Pestaña 1 — Mapa de mercado**: Competidores, posicionamiento, precios de referencia.
- **Pestaña 2 — Oportunidades**: Huecos detectados, diferencial del usuario vs mercado, recomendación de posicionamiento.
- **Pestaña 3 (Explorador)**: Comparativa de nichos con puntuación.
- **Pestaña 3 (Activador)**: Mapa de canales de captación con priorización.

## Persistencia

Tras generar entregable:
```json
{
  "action": "deliverable_generated",
  "module": "M1",
  "details": "investigacion-mercado-[nombre].html v1"
}
```

Actualizar `progress.current_module`, `modules_completed`, `deliverables`.

## Checkpoint M1

> "He terminado el análisis de mercado. ¿Quieres ajustar algo antes de diseñar la oferta?"

Para Explorador, añadir:
> "Has elegido el nicho de [X]. A partir de aquí construimos sobre esta decisión. Si en cualquier momento sientes que no es el camino, podemos recalibrar."
