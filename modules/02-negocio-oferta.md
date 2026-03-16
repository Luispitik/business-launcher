# Módulo 02 — Diseño del negocio y oferta

## Objetivo

Definir el modelo de negocio, la propuesta de valor, el cliente ideal y la
estructura de servicios con tarifas. Incluye checkpoint de factores humanos,
fase de expansión proactiva de catálogo, y visión estratégica de evolución.

## Pre-requisitos

- Cargar estado persistido (user_profile, human_factors, M1 completado).
- Para checkpoint: leer `${CLAUDE_SKILL_DIR}/layers/factores-humanos.md`.

## REGLA CRÍTICA — CALIBRACIÓN DE PERFIL

Antes de diseñar cualquier precio o expectativa, clasificar al usuario:

| Perfil | Indicadores del intake | Calibración de pricing |
|--------|----------------------|----------------------|
| **Arranca de cero** | Empleado, sin clientes, sin portfolio, sin marca | Cuartil bajo-medio del mercado freelance. Precio que pueda decir sin tartamudear. |
| **Freelance sin estructura** | Tiene clientes pero sin proceso, sin precios formales | Cuartil medio. Formalizar lo que ya cobra + subida del 15-20%. |
| **Profesional con base** | Tiene clientes, marca, algo de portfolio | Cuartil medio-alto. Benchmarking directo con M1. |
| **Veterano que escala** | Factura regular, clientes recurrentes, proceso definido | Cuartil alto o por encima de mercado si diferencial lo justifica. |

**Esta tabla es obligatoria.** No asignar precios de "profesional con base" a
alguien que es "arranca de cero". El síndrome del impostor ya le frena bastante
— unos precios inflados le paralizan del todo.

## REGLA CRÍTICA — VERIFICACIÓN DE COHERENCIA

Antes de proponer CADA servicio y CADA precio, verificar contra:
1. **Principios declarados** en el intake y la conversación (si dijo "no quiero
   vender tiempo por dinero", no diseñar servicios por horas).
2. **Situación real** (si dijo "empleado que arranca con 1.000€", no proponer
   stack de herramientas de 200€/mes).
3. **Capacidad técnica** (si no sabe programar, no incluir servicios de desarrollo).

Si Claude detecta una incoherencia con algo que el usuario dijo, **corregirla
antes de presentar**, no esperar a que el usuario la detecte.

## Ejecución

### 2.1 Modelo de negocio

Definir con el usuario:
- ¿Cómo genera dinero? (proyecto, retainer, formación, SaaS, marketplace...)
- ¿Cuál es el servicio tractor? (convierte curiosidad en primer pago)
- ¿Cuál es el servicio de mayor margen?
- ¿Cuál es el servicio de recurrencia?

**Ajuste por ruta:**
- Explorador: empezar con 1 servicio único (el más validable en M1). No diseñar catálogo completo aún.
- Redefinidor: partir de servicios actuales, reconstruir — no diseñar desde cero.
- Escalador: enfocarse en productización de servicios existentes y subida de precios.
- Activador: revisar con lente de conversión — ¿se entiende en 10 segundos?

### 2.2 Cliente ideal (ICP)

```
Sector: [industria]
Tamaño de empresa: [empleados / facturación]
Rol del decisor: [cargo]
Problema principal que resuelves: [frase concreta]
Síntoma que siente el cliente: [cómo lo describe]
Lo que ha intentado antes sin éxito: [alternativas fallidas]
Por qué tú eres la solución: [diferencial concreto]
```

### 2.3 Propuesta de valor

Estructura:
> "Ayudo a [ICP] a [resultado concreto] sin [frustración habitual] en [plazo realista]."

### 2.4 Catálogo de servicios

Para cada servicio:
```
Nombre: [nombre comercial]
Descripción: [1-2 frases para el cliente]
Entregable: [qué recibe exactamente]
Plazo: [días/semanas]
Precio mínimo | óptimo | premium: [€] ← CALIBRADO según tabla de perfil
Costes operativos recurrentes: [APIs, licencias, hosting — desglosados]
Margen real estimado: [% después de costes operativos]
Nivel de esfuerzo: [horas de trabajo]
Cliente ideal para este servicio: [quién lo compra]
Servicio previo recomendado: [embudo]
Variantes: [cloud vs self-hosted, si aplica]
```

### 2.5 FASE DE EXPANSIÓN DE CATÁLOGO (obligatoria)

Tras diseñar el catálogo inicial, Claude **propone proactivamente** servicios
complementarios que el usuario no haya mencionado pero que sean extensiones
naturales de su perfil:

> "Antes de cerrar el catálogo, he identificado [N] servicios complementarios
> que encajan con tu perfil y que podrías considerar. No tienes que añadir
> ninguno — pero quiero que los veas antes de decidir:"
>
> 1. [Servicio X] — [Por qué encaja con su perfil]
> 2. [Servicio Y] — [Por qué encaja]
> 3. [Servicio Z] — [Por qué encaja]
>
> "¿Alguno te interesa incorporar?"

**Criterios para proponer servicios complementarios:**
- Servicios de mantenimiento/retainer si solo ha diseñado proyectos puntuales.
- Versión self-hosted vs cloud si el servicio implica infraestructura técnica.
- Servicio de auditoría/diagnóstico si no tiene servicio tractor de bajo coste.
- Formación/capacitación si su ICP necesita autonomía posterior.
- Diagramas de flujo / documentación visual como entregable estándar en consultoría.
- Vibe Coding / desarrollo visual si tiene capacidades técnicas para ello.

### 2.6 DISEÑO DE MANTENIMIENTO INTEGRAL

Si el catálogo incluye más de 2 servicios que generan necesidad de seguimiento
posterior, **diseñar un retainer integral** en vez de mantenimiento servicio a servicio:

```
RETAINER INTEGRAL — [Nombre]

Concepto: Un solo contrato de mantenimiento que cubre todo lo implementado.
Módulos incluidos: [lista de servicios cubiertos]
Precio mensual: [€] (siempre inferior a la suma de mantenimientos individuales)
Horas incluidas: [N horas/mes]
Qué cubre: [soporte, actualizaciones, optimización, monitorización]
Qué NO cubre: [nuevos desarrollos, ampliaciones de scope]
Escalado: Si el cliente añade nuevos servicios, el retainer sube [€X] por módulo.
```

### 2.7 Estructura de tarifas

Tabla con todos los servicios, rangos de precio y justificación basada en M1.

**Sección obligatoria — Costes operativos por servicio:**
Para cada servicio que implique herramientas de terceros:
- Coste de APIs (estimación mensual por cliente).
- Licencias de software necesarias.
- Hosting / infraestructura.
- **Verificar precios actuales con web_search.** No basarse en conocimiento previo.
- Política de quién paga los costes operativos (incluido en precio vs facturado aparte).

### 2.8 VISIÓN ESTRATÉGICA (obligatoria)

#### Plan de evolución de precios

```
HOJA DE RUTA DE PRICING

Precio de lanzamiento (meses 1-3): [€] ← calibrado al perfil actual
Primer ajuste (mes 4-6): [€] [+X%] [condición: cuando tenga N clientes/testimonios]
Segundo ajuste (mes 7-12): [€] [+X%] [condición: cuando tenga portfolio visible]
Objetivo a 18 meses: [€] [cuartil del mercado al que aspira]
```

Nunca presentar solo el precio actual. Siempre incluir la progresión.

#### Estrategia de primeros clientes

```
PLAN DE INVERSIÓN INICIAL

Opción A — Auditoría/diagnóstico gratuito:
  Ofrecer [servicio tractor] gratis a [N] primeros clientes a cambio de:
  - Testimonial escrito o en vídeo
  - Permiso para usar como caso de estudio
  - 1-2 referidos cualificados

Opción B — Descuento fundador:
  [X]% de descuento para los primeros [N] clientes.
  Con fecha límite: "hasta [fecha] o hasta completar [N] plazas".

Opción C — Piloto reducido:
  Versión reducida del servicio a precio simbólico.
  Objetivo: validar el proceso y generar confianza.

Recomendación: [A / B / C según perfil y urgencia]
```

**Si el usuario arranca de cero, esta sección no es opcional — es el primer
paso del plan de 90 días.**

## CHECKPOINT DE FACTORES HUMANOS (M2)

**Antes de cerrar este módulo**, activar la capa de factores humanos:

1. **Test de pricing emocional:**
   "El precio óptimo de tu servicio principal es €[X]. ¿Te genera incomodidad
   decirlo en voz alta a un potencial cliente?"
   - Si sí → trabajar la justificación con evidencia de mercado del M1.
   - Registrar en `human_factors`.

2. **Verificación de coherencia final:**
   Revisar todo el catálogo contra los principios declarados por el usuario.
   Si algo no cuadra, señalarlo: "Has dicho [principio] pero el servicio [X]
   contradice eso porque [razón]. ¿Ajustamos?"

3. **Revisión de miedos vs oferta:**
   - Si miedo a vender → añadir al entregable un "script de conversación de
     descubrimiento" (no guion de ventas).
   - Si urgencia alta → verificar que el servicio tractor se puede vender en <2 semanas.
   - Si fracaso previo por pricing bajo → mostrar comparativa de mercado.

4. **Actualizar factores humanos en estado:**
   Añadir `"M2"` a `human_factors.updated_at_modules`.

## Entregable M2

**DOCX** — "Modelo de Negocio y Oferta — [Nombre]" con:
- Modelo de negocio
- ICP
- Propuesta de valor
- Catálogo de servicios (tabla completa con costes operativos)
- Retainer integral (si aplica)
- Estructura de tarifas con justificación
- Plan de evolución de precios
- Estrategia de primeros clientes
- Script de conversación de descubrimiento (si aplica)

Si tienes la skill `docx` instalada, lee su SKILL.md antes de generar.

## Persistencia

Actualizar estado con M2 completado, decisiones de pricing en `decisions_log`.

## Checkpoint M2

> "Aquí tienes el modelo completo. Antes de seguir: ¿hay algún servicio que
> quieras añadir, quitar o modificar el precio? ¿Algo que no encaje con cómo
> quieres trabajar?"
