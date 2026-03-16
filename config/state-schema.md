# State Schema — Business Launcher v3

## Principio de diseño

La persistencia es **invisible para el usuario**. Nunca se le pide descargar,
subir ni gestionar archivos de estado. Todo ocurre a través de artifacts HTML
mínimos que leen/escriben en `window.storage` por detrás.

El usuario solo interactúa en chat. Los artifacts de estado son instrumentales
(se generan, ejecutan su función y el foco vuelve al chat).

## Clave de almacenamiento

```
Clave: 'bl-state'
Tipo: JSON stringificado
Scope: personal (shared: false)
```

## Operación 1 — Cargar estado (inicio de conversación)

**Cuándo**: SIEMPRE al activarse el skill, antes de cualquier otra cosa.

**Cómo**: Generar un artifact HTML que lea el estado y lo envíe al chat:

```html
<div id="status" style="font-family: var(--font-sans); padding: 1rem 0; color: var(--color-text-secondary); font-size: 14px;">
  Cargando sesión anterior...
</div>
<script>
(async () => {
  const el = document.getElementById('status');
  try {
    const result = await window.storage.get('bl-state');
    if (result && result.value) {
      const state = JSON.parse(result.value);
      const completed = state.progress.modules_completed || [];
      const current = state.progress.current_module || '00';
      const route = state.route.assigned || 'sin asignar';
      const name = state.user_profile.name || 'usuario';
      const pct = state.progress.completion_percentage || 0;
      const deliverables = (state.deliverables || []).length;

      // Mostrar resumen visual
      const modules = ['00','01','02','03','04','05','06'];
      const skipped = state.route.skipped_modules || [];
      const optional = state.route.optional_modules || [];
      const icons = modules.map(m => {
        if (completed.includes(m)) return '✅';
        if (skipped.includes(m)) return '⏭️';
        if (m === current) return '⏳';
        return '⬜';
      });

      el.innerHTML = '<div style="font-size:15px;font-weight:500;color:var(--color-text-primary);margin-bottom:8px">Sesión anterior encontrada</div>'
        + '<div style="margin-bottom:4px"><b>Ruta:</b> ' + route.charAt(0).toUpperCase() + route.slice(1) + ' — ' + name + '</div>'
        + '<div style="margin-bottom:4px"><b>Progreso:</b> Intake ' + icons[0] + ' M1 ' + icons[1] + ' M2 ' + icons[2] + ' M3 ' + icons[3] + ' M4 ' + icons[4] + ' M5 ' + icons[5] + ' M6 ' + icons[6] + '</div>'
        + '<div style="margin-bottom:4px"><b>Entregables:</b> ' + deliverables + ' generados</div>'
        + '<div style="margin-bottom:12px"><b>Completado:</b> ' + pct + '%</div>';

      // Enviar estado completo al chat para que Claude lo tenga en contexto
      sendPrompt('ESTADO RECUPERADO: ' + JSON.stringify(state));
    } else {
      el.textContent = 'Sin sesión anterior. Empezamos de cero.';
      sendPrompt('ESTADO RECUPERADO: null');
    }
  } catch (e) {
    el.textContent = 'Sin sesión anterior. Empezamos de cero.';
    sendPrompt('ESTADO RECUPERADO: null');
  }
})();
</script>
```

**Qué hace Claude al recibir el sendPrompt**:
- Si recibe `null` → Inicia Fase 0 (Intake).
- Si recibe estado → Muestra resumen conversacional y pregunta si retomar o reiniciar.

**IMPORTANTE**: Claude NO muestra el JSON crudo al usuario. Interpreta el estado
y habla en lenguaje natural: "La última vez completamos la investigación de mercado
y el diseño de oferta. ¿Seguimos con la identidad de marca?"

## Operación 2 — Guardar estado (tras cada checkpoint)

**Cuándo**: Después de cada checkpoint confirmado por el usuario.

**Cómo**: Generar un artifact HTML que escriba el estado actualizado:

```html
<div id="save" style="font-family: var(--font-sans); padding: 1rem 0; color: var(--color-text-secondary); font-size: 13px;">
  Guardando progreso...
</div>
<script>
(async () => {
  const state = STATE_JSON_HERE; // Claude reemplaza con el estado completo
  try {
    await window.storage.set('bl-state', JSON.stringify(state));
    document.getElementById('save').innerHTML = '<span style="color:var(--color-text-success)">✓ Progreso guardado</span>';
  } catch (e) {
    document.getElementById('save').innerHTML = '<span style="color:var(--color-text-warning)">⚠ No se pudo guardar. El progreso se mantiene en esta conversación.</span>';
  }
})();
</script>
```

**Claude reemplaza `STATE_JSON_HERE`** con el objeto de estado completo serializado.
El usuario ve brevemente "✓ Progreso guardado" y el flujo continúa.

## Operación 3 — Reinicio

Si el usuario pide reiniciar:

```html
<script>
(async () => {
  try {
    // Backup del estado actual
    const current = await window.storage.get('bl-state');
    if (current && current.value) {
      const ts = new Date().toISOString().slice(0,10);
      await window.storage.set('bl-state-backup-' + ts, current.value);
    }
    // Borrar estado principal
    await window.storage.delete('bl-state');
    sendPrompt('ESTADO REINICIADO');
  } catch (e) {
    sendPrompt('ESTADO REINICIADO');
  }
})();
</script>
```

## Esquema del objeto de estado

```json
{
  "version": "3.0.0",
  "created_at": "ISO 8601",
  "updated_at": "ISO 8601",

  "user_profile": {
    "name": "",
    "location": "",
    "situation": "explorador | definidor | redefinidor | escalador",
    "problem_statement": "",
    "differential": "",
    "existing_clients": false,
    "client_details": "",
    "economic_goal": "",
    "time_available_hours_week": 0,
    "budget_initial": 0,
    "has_team": false,
    "team_details": "",
    "has_brand": false,
    "brand_details": "",
    "main_blocker": "",
    "excluded_sectors": [],
    "existing_assets": {
      "monthly_revenue": null,
      "num_clients": null,
      "avg_ticket": null,
      "conversion_rate": null,
      "existing_contracts": false,
      "existing_website": "",
      "existing_tools": [],
      "existing_subscriptions": []
    }
  },

  "human_factors": {
    "fears": [],
    "past_failures": [],
    "urgency_level": "low | medium | high | critical",
    "urgency_details": "",
    "emotional_state": "",
    "support_network": "",
    "risk_tolerance": "low | medium | high",
    "decision_style": "analytical | intuitive | mixed",
    "updated_at_modules": []
  },

  "route": {
    "assigned": "explorador | definidor | redefinidor | escalador",
    "reassigned_from": null,
    "reassignment_reason": null,
    "module_sequence": ["00", "01", "02", "03", "04", "05", "06"],
    "skipped_modules": [],
    "optional_modules": ["06"]
  },

  "progress": {
    "current_module": "00",
    "current_step": "",
    "modules_completed": [],
    "modules_in_progress": [],
    "last_checkpoint": "",
    "last_checkpoint_at": "ISO 8601",
    "completion_percentage": 0
  },

  "decisions_log": [
    {
      "id": 1,
      "timestamp": "ISO 8601",
      "module": "M2",
      "decision": "Elegido modelo de retainer sobre proyectos puntuales",
      "alternatives_considered": ["Proyecto puntual", "Retainer mensual", "Híbrido"],
      "reasoning": "Mayor previsibilidad de ingresos",
      "human_factors_influence": "Urgencia alta → priorizar recurrencia"
    }
  ],

  "deliverables": [
    {
      "id": 1,
      "module": "M1",
      "name": "investigacion-mercado-acme.html",
      "format": "HTML",
      "generated_at": "ISO 8601",
      "version": 1,
      "status": "final | draft | revised"
    }
  ],

  "change_history": [
    {
      "timestamp": "ISO 8601",
      "action": "module_completed | module_skipped | route_reassigned | deliverable_generated | deliverable_revised | profile_updated | human_factors_updated",
      "module": "",
      "details": "",
      "previous_value": null,
      "new_value": null
    }
  ]
}
```

## Reglas de escritura

1. **Nunca sobrescribir sin leer.** Siempre cargar estado actual → modificar → guardar.
2. **Actualizar `updated_at`** en cada escritura.
3. **`decisions_log` es append-only.** Nunca borrar decisiones anteriores.
4. **`deliverables` permite versiones.** Si se regenera, incrementar `version`.
5. **Si `change_history` supera 50 entradas**, comprimir las antiguas en resumen.
6. **Límite de tamaño.** Si el estado se acerca a 100KB, comprimir `change_history`
   y mantener solo las últimas 20 entradas detalladas.

## Instrucciones para Claude

- **Al inicio**: Genera el artifact lector. Espera el `sendPrompt` con el estado.
- **Tras cada checkpoint**: Construye el objeto de estado actualizado y genera el artifact escritor.
- **Nunca muestres JSON crudo al usuario.** Todo se traduce a lenguaje natural.
- **Si el storage falla**: Continuar normalmente. El estado se mantiene en la conversación
  activa. Avisar al usuario: "No se pudo guardar el progreso. Si cierras esta conversación,
  tendremos que retomar manualmente."
- **Nunca pedir al usuario que descargue, suba o gestione archivos de estado.**
