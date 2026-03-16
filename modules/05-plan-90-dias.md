# Módulo 05 — Plan de 90 días accionable

## Objetivo

Plan de acción semanal con tareas concretas, decisiones, herramientas y métricas.
Sin ambigüedades. Adaptado a la ruta y a los factores humanos del usuario.

## Pre-requisitos

- Cargar estado completo (perfil, factores humanos, módulos previos).
- Leer `${CLAUDE_SKILL_DIR}/layers/factores-humanos.md` para checkpoint.

## Estructura base por semana

```
SEMANA [N] — [Título]
Objetivo: [resultado concreto al final de los 7 días]

TAREAS (en orden de ejecución):
[ ] Tarea 1
    Qué hacer: [paso a paso]
    Herramienta: [nombre concreto + link]
    Tiempo estimado: [horas]
    Resultado esperado: [qué tienes cuando completas]
    Decisión necesaria: [si aplica]

MÉTRICA DE ÉXITO:
→ [indicador concreto y medible]
```

## 3 sprints adaptados por ruta

### EXPLORADOR

**Sprint 1 (días 1-30) — Validación**
- Semanas 1-2: 10 conversaciones de descubrimiento con potenciales clientes del nicho elegido en M1.
- Semanas 3-4: Primer servicio piloto (precio reducido o gratis a cambio de caso de estudio). Formalización legal mínima.

**Sprint 2 (días 31-60) — Primeros pasos**
- Primeras propuestas formales basadas en aprendizaje del piloto.
- Web mínima o landing page.
- Primer contenido de autoridad.

**Sprint 3 (días 61-90) — Consolidación**
- 2-3 clientes de pago.
- Proceso definido y replicable.
- Decisión: ¿este nicho funciona o pivoto?

### DEFINIDOR

**Sprint 1 (días 1-30) — Fundación**
- Constitución legal / alta autónomo.
- Herramientas mínimas (email, facturación, CRM básico).
- 10 conversaciones de validación.
- Primera propuesta enviada.
- Web mínima.

**Sprint 2 (días 31-60) — Primeros clientes**
- Refinamiento de propuesta.
- Canal principal de captación (×1).
- Primer cliente o primer "no" documentado.
- Onboarding de cliente definido.

**Sprint 3 (días 61-90) — Optimización**
- Revisión de precios basada en conversaciones reales.
- Segundo cliente o ampliación.
- Sistema de referidos.
- Análisis de resultados vs objetivos.

### REDEFINIDOR

**Sprint 1 (días 1-30) — Transición**
- Mantener ingresos actuales mientras construye lo nuevo.
- Comunicar transición a clientes actuales (si aplica).
- 5 conversaciones en el nuevo mercado.
- Ajustar oferta basada en feedback.

**Sprint 2 (días 31-60) — Puente**
- Primer cliente en el nuevo posicionamiento.
- Reducir gradualmente servicios del modelo anterior.
- Actualizar presencia digital.

**Sprint 3 (días 61-90) — Consolidación**
- Mayoría de ingresos del nuevo modelo.
- Proceso documentado.
- Decisión sobre servicios que mantener del modelo anterior.

### ACTIVADOR

**Sprint 1 (días 1-30) — Activación de pipeline**
- Semana 1: Activar red de contactos (Canal 0 del M7). Enviar mensajes personalizados a 15-20 personas.
- Semana 2: Lanzar canal principal elegido en M7. Primeras 5 acciones de outreach/contenido.
- Semana 3: Primeras conversaciones de descubrimiento (objetivo: 5). Ajustar mensaje si tasa de respuesta <30%.
- Semana 4: Primera propuesta enviada. Configurar pipeline de seguimiento (CRM mínimo).

**Sprint 2 (días 31-60) — Primeras conversiones**
- Primer cliente cerrado o primer "no" con motivo documentado y aprendizaje aplicado.
- Duplicar volumen del canal principal.
- Revisar oferta/pricing si las conversaciones revelan fricción.
- Activar sistema de seguimiento (nunca más de 5 días sin follow-up).
- Publicar primer contenido de autoridad si el canal lo permite.

**Sprint 3 (días 61-90) — Sistema y segundo canal**
- 2-3 clientes activos o en pipeline avanzado.
- Documentar qué mensajes/canales funcionan y cuáles no (playbook propio).
- Evaluar segundo canal de captación (no antes).
- Pedir primer testimonio/caso de estudio a cliente satisfecho.
- Análisis: ratio conversaciones → propuestas → clientes. Identificar cuello de botella.

### ESCALADOR

**Sprint 1 (días 1-30) — Quick wins**
- Subida de precios comunicada a nuevos clientes (los existentes en siguiente renovación).
- Productizar servicio más vendido.
- Medir tiempo por servicio para detectar ineficiencias.

**Sprint 2 (días 31-60) — Sistematización**
- Documentar procesos clave (onboarding, delivery, facturación).
- Evaluar primer hire o subcontratación.
- Automatizar lo automatizable.

**Sprint 3 (días 61-90) — Delegación**
- Primera tarea delegada.
- Sistema de calidad para trabajo delegado.
- Pipeline de leads sistematizado.

## CHECKPOINT DE FACTORES HUMANOS (M5)

**Antes de cerrar este módulo**, activar la capa:

1. **Test de resistencia:**
   "Mirando la primera semana del plan, ¿hay alguna tarea que te genere resistencia real?"
   - Si sí → descomponer en subtareas más pequeñas o sustituir por equivalente menos intimidante.

2. **Ajustes por factores detectados:**
   - Urgencia alta → verificar que Sprint 1 tiene hito de ingreso.
   - Miedo al rechazo → primeras conversaciones con red de confianza.
   - Perfeccionismo → fechas límite fijas + regla "publicar aunque no esté perfecto".
   - Fracaso previo por aislamiento → incluir comunidad/accountability como tarea.

3. **Calibración de ritmo:**
   Comparar horas/semana disponibles (P7) con carga del plan.
   Si no cuadra, reducir scope — nunca inflar disponibilidad.

4. **Actualizar factores humanos en estado:**
   Añadir `"M5"` a `human_factors.updated_at_modules`.

## REGLA CRÍTICA — VERIFICACIÓN DE HERRAMIENTAS

Antes de incluir CUALQUIER herramienta en el plan o en el apéndice:

1. **Consultar stack existente del usuario** (P8b del intake). Si ya tiene
   una herramienta que cubre esa función, usarla — no recomendar otra.

2. **Verificar pricing actual con web_search.** No basarse en conocimiento
   previo para datos de precios. Las herramientas cambian de plan, suben
   precios o eliminan planes gratuitos constantemente.

3. **Incluir siempre alternativa gratuita o freemium** junto a cada
   herramienta de pago. Si no existe alternativa gratuita viable, decirlo
   explícitamente.

4. **Si el usuario tiene presupuesto limitado (<1.000€)**, priorizar
   herramientas gratuitas y solo mencionar las de pago como "cuando puedas
   invertir más".

## Entregable M5

**DOCX** — "Plan de 90 Días — [Nombre]" con:
- Resumen ejecutivo del plan
- Las 13 semanas detalladas
- Apéndice: stack de herramientas recomendado (con links, coste VERIFICADO, alternativas gratuitas)
- Notas de calibración por factores humanos (si aplica)

Si tienes la skill `docx` instalada, lee su SKILL.md antes de generar.

## Persistencia

Actualizar estado. Registrar ajustes por factores humanos en `decisions_log`.

## Checkpoint M5

> "Plan de 90 días generado. ¿Ajustamos alguna semana según tu disponibilidad
> real o alguna tarea que te genere resistencia?"
