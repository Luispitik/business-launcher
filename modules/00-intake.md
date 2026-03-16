# Módulo 00 — Intake adaptativo

## Objetivo

Recopilar información, detectar la ruta del usuario y explorar factores
humanos. Máximo 15 minutos. Preguntas de una en una, conversacionalmente.

## Mensaje de arranque

> **Hola. Voy a acompañarte en el proceso de construir (o reconstruir) tu negocio.**
>
> Voy a hacerte unas preguntas para entender tu situación. No hay respuestas
> correctas — solo información de partida. Si no tienes un dato, lo estimamos juntos.
>
> ¿Empezamos?

## Fase 1 — Detección de ruta (P1-P4)

### P1. Identificación
"¿Cómo te llamas y desde dónde trabajas?"

### P2. Situación actual → DETERMINA LA RUTA

"¿Cuál de estas situaciones describe mejor dónde estás ahora?"
- a) Tengo habilidades y experiencia pero no sé qué negocio montar → **EXPLORADOR**
- b) Tengo una idea clara de negocio pero no he arrancado → **DEFINIDOR**
- c) Ya tengo negocio/freelance pero quiero cambiar de dirección → **REDEFINIDOR**
- d) Tengo el negocio montado pero no me entran clientes → **ACTIVADOR**
- e) Ya facturo regularmente y quiero crecer o escalar → **ESCALADOR**

**Desambiguación** (si la respuesta no encaja limpiamente):
- "¿Ya tienes clientes que te paguen de forma regular?"
  → Sí, varios = Escalador | Sí, pocos y sin sistema = Activador | No = Explorador/Definidor/Redefinidor
- "¿Tienes claro qué servicio ofreces y a quién?"
  → Sí pero no llegan clientes = Activador | Sí pero quiero cambiar = Redefinidor | No = Explorador
- Si persiste la duda, preguntar directamente: "¿Te identificas más con [A] o con [B]?"

### P3. Contexto según ruta

| Ruta | P3 |
|------|-----|
| Explorador | "¿Qué sabes hacer bien? No pienses en negocio — piensa en qué te piden, qué se te da mejor que a la media, qué disfrutas." |
| Definidor | "En una frase: ¿qué problema quieres resolver y para quién?" |
| Redefinidor | "¿Qué tienes ahora (clientes, facturación, marca, web) y qué quieres cambiar?" |
| Activador | "Cuéntame qué tienes montado (oferta, web, marca, contratos) y qué has intentado para captar clientes. ¿Qué pasó?" |
| Escalador | "¿Cuánto facturas al mes, cuántos clientes tienes y cuál es tu ticket medio?" |

### P4. Diferencial
"¿Qué experiencia, formación o conocimiento tienes que te diferencia?"

## Fase 2 — Contexto operativo (P5-P9)

### P5. Red existente
"¿Tienes ya clientes, contactos del sector o conversaciones abiertas?"

### P6. Objetivo económico a 12 meses
- a) Complementar ingresos (<€2.000/mes)
- b) Sustituir empleo actual (€2.000–€4.000/mes)
- c) Construir empresa (€4.000–€10.000/mes)
- d) Escalar con equipo (>€10.000/mes)

### P7. Recursos disponibles
"¿Con qué cuentas para arrancar?"
- Tiempo disponible (horas/semana)
- Presupuesto inicial aproximado
- ¿Solo/a o con equipo?

### P8. Estado de marca
"¿Tienes ya nombre de negocio, logo o web?"

### P9. Stack técnico y herramientas existentes
"¿Tienes alguna herramienta, servicio o suscripción ya contratada?
Piensa en todo: hosting, dominio, VPS, herramientas de diseño, CRM,
facturación, email marketing, herramientas de comunicación visual
(Miro, draw.io...), software de cualquier tipo."

**Registrar todo** para no recomendar herramientas duplicadas ni asumir
que parte de cero en stack técnico.

## Fase 3 — Factores humanos (P10-P11)

Leer `${CLAUDE_SKILL_DIR}/layers/factores-humanos.md` antes de ejecutar.

### P10. Bloqueos y miedos
"¿Cuál es tu mayor bloqueo ahora mismo para arrancar o avanzar?"

Si la respuesta es superficial ("falta de tiempo", "no sé por dónde empezar"),
profundizar con UNA:
- "¿Qué es lo peor que podría pasar si arrancas esto y no funciona?"
- "¿Hay alguna conversación que estés evitando tener?"

### P11. Experiencia previa y urgencia
"¿Has intentado algo parecido antes? Y en términos de urgencia:
¿cuántos meses puedes mantenerte sin que esto genere ingresos?"

## Fase 4 — Exclusiones (P12)

### P12. Descartes
"¿Hay alguna industria, tipo de cliente o servicio que hayas descartado ya?"

## Procesamiento post-intake

### 1. Persistir perfil
Guardar en estado: `user_profile` + `human_factors` + `existing_subscriptions`.

### 2. Diagnóstico

```
📊 DIAGNÓSTICO INICIAL

Perfil: [nombre] — [Explorador/Definidor/Redefinidor/Activador/Escalador]
Base: [resumen 1 línea]
Fortaleza principal: [la más clara]
Riesgo principal: [el más evidente]
Factor humano clave: [miedo/bloqueo/urgencia más relevante]
Stack existente: [resumen de herramientas que ya tiene]

Ruta asignada: [NOMBRE]
Secuencia de módulos:
  [secuencia adaptada a la ruta con ✅/⬜/⏭️]
  [Nota si algún módulo se ajusta, salta o reordena]
```

### 3. Brief de negocio (Entregable)

**DOCX** — "Brief de Negocio — [Nombre]" con:
- Datos del perfil completo
- Diagnóstico
- Ruta asignada y justificación
- Factores humanos identificados (pragmático, no clínico)
- Stack existente del usuario
- Secuencia de módulos con ajustes

Si tienes la skill `docx` instalada, lee su SKILL.md antes de generar.

### 4. Checkpoint

> "Este es tu diagnóstico y tu ruta. ¿Te ves reflejado/a?
> ¿Ajustamos algo antes de arrancar M1?"
