# ROBBBO‑T · BOOTSTRAP REPO (TFA V2 / ASI‑T2)

> **SSoT & Guardrails:** Este repo aplica **ASI‑T · Universal Injection Prompt (v1)** como fuente única de verdad para acciones de agentes y humanos. Se aplican **MAL‑EEM** (ética & empatía) y **UTCS** (UiX Threading Context/Content/Cache and Structure/Style/Sheet) para trazabilidad total.

**TFA FLOW (Canon):** `QS → FWD → UE → FE → CB → QB`
**PAx Orientation Markers:** `ONB` (Onboard), `OUT` (Outboard)

---

## 0) MANIFIESTO DEL PORTFOLIO

* **Tesis:** Transporte Aéreo y Espacial con **H₂ híbrido‑eléctrico** y **Quantum‑enhanced**, con verificación física, gobernanza climática y trazabilidad UTCS.
* **Líneas de producto (T = transport, tripulado):**

  * **AMPEL360‑T‑Air**: BWB H₂ hybrid‑electric (Quantum‑enhanced)
  * **AMPEL360‑T‑Space**: Transporte espacial tripulado (suborbital → orbital)

---

## 1) ESTRUCTURA DE REPOSITORIO (MOD‑STACK / MOD‑PACK)

```text
robbbo-t/
├── canon/                         # CANON & GENESIS (SSoT)
│   ├── GENESIS_ASI-T2.md          # Texto canónico (GENESIS) marcado por el usuario
│   ├── CANON_FACTS.md             # Hechos canon (TFA flow, UTCS, Domains AAA…PPP, PAx)
│   └── INJECTION_PROMPT_v1.md     # ASI‑T · Universal Injection Prompt (v1)
├── governance/
│   ├── MAL-EEM/                   # Ética/Seguridad (políticas, checklists)
│   ├── UTCS/                      # Estructuras de trazabilidad, SSoT, plantillas
│   └── COMPLIANCE/                # Rutas de certificación (EASA/ESA/NASA), Means of Compliance
├── ci/
│   ├── gates/
│   │   ├── FCR-1_checklist.md     # Follow‑up Chain Rule 1 (inputs/paths válidos)
│   │   ├── FCR-2_checklist.md     # Follow‑up Chain Rule 2 (trazabilidad QS/UTCS)
│   │   ├── link_path_validator.py # Validador de enlaces/rutas (CI gate)
│   │   └── fcr_enforcer.py        # Enforcers CI (bloqueo de PR si no cumple)
│   └── workflows/                 # YAML de CI/CD (lint, build, sim, docs)
├── docs/
│   ├── ROADMAP.md                 # Roadmap 12–18 meses (Air/Space)
│   ├── PARTNERS.md                # Proveedores/partners
│   ├── FUNDING_EU.md              # Grants UE (Clean Aviation, SESAR, ESA, etc.)
│   └── PLAYBOOKS/                 # Operación, seguridad H₂, GSE, flight test
├── domains/                       # AAA…PPP (15 dominios TFA)
│   ├── AAA/ …                     # (placeholder de todos los dominios canon)
│   └── PPP/
├── products/
│   ├── ampel360-t-air/
│   │   ├── README.md              # One‑pager + KPIs + TRLs
│   │   ├── QS/                    # Gemelos, optimización, mission planning
│   │   ├── FWD/                   # Aero BWB, criogenia, integración energética
│   │   ├── UE/                    # Cabina/sistemas, HMI, safety/evacuación
│   │   ├── FE/                    # Integración propulsión, thermal, BMS, avionics
│   │   ├── CB/                    # Certificación (EASA CS‑25 + SC H₂/eléctrico)
│   │   └── QB/                    # Pruebas HIL/SIL, ensayos criogénicos, e‑fans
│   └── ampel360-t-space/
│       ├── README.md              # One‑pager + Fases A/B/C, human‑rating path
│       ├── QS/
│       ├── FWD/
│       ├── UE/
│       ├── FE/
│       ├── CB/                    # Human‑rating, estándares ESA/NASA
│       └── QB/
├── sim/
│   ├── air/                       # Modelos de sistema (propulsión H₂‑eléctrica), e‑fan
│   └── space/                     # GNC suborbital/orbital, entry‑guidance
├── cax/                           # CAE/CAD/CFD/FEA (enlaces y outputs)
├── qox/                           # Quality Ops eXchange: datos, métricas, ensayos
├── data/                          # Datasets (UTCS‑indexed)
└── tools/
    ├── templates/                 # Plantillas (MoC, PDR/CDR, hazard logs, etc.)
    └── cli/rtx.py                 # CLI para crear estructuras QS→FWD→UE→FE→CB→QB
```

> **Regla:** Todo módulo de producto debe respetar el **orden canónico** `QS→FWD→UE→FE→CB→QB`. Los PR que rompan el orden o no actualicen UTCS serán rechazados por **CI gates**.

---

## 2) CHECKLISTS (por capa TFA)

* **QS:**

  * [ ] Modelos de demanda/energía; sizing H₂; rutas; sensibilidad climática.
  * [ ] Objetivos de ruido, NOx, CO₂ (well‑to‑wake); escenarios de grid H₂.
* **FWD:**

  * [ ] Integración BWB (Air) / estructura y TPS (Space).
  * [ ] Gestión criogénica (aislamiento, ventilación, inertización).
* **UE:**

  * [ ] HMI crew/pax, evac, ergonomía, accesibilidad; aborts (Space).
* **FE:**

  * [ ] Propulsión H₂‑eléctrica, BMS, thermal, e‑fans; LSS/docking (Space).
* **CB:**

  * [ ] Matriz de cumplimiento (EASA SC eléctricos/H₂; ESA/NASA HRP).
* **QB:**

  * [ ] HIL/SIL, bancos de ensayo, pruebas taxi, drop/hover tests.

---

## 3) ONE‑PAGER · AMPEL360‑T‑AIR (BWB H₂ Hybrid‑Electric, Quantum‑Enhanced)

**Propuesta de valor**

* 30–60% ↓ energía pax‑km vs cilíndrico; cero CO₂ en uso; ruido muy bajo taxi/despegue.
* “Quantum‑enhanced”: optimización energética/rota y mantenimiento predictivo.

**Arquitectura (QS→FWD→UE→FE→CB→QB)**

* **QS:** Gemelo cuántico‑híbrido; sizing tanque H₂L; rutas y clima; KPIs.
* **FWD:** BWB con tanques conformales ONB; distribución masas; seguridad H₂.
* **UE:** Cabina, evacuación, ergonomía; HMI energía/flight.
* **FE:** Pila(s) + turbogenerador H₂ (pico/reserva) → e‑fans distribuidos; thermal.
* **CB:** CS‑25 + SC eléctricos/H₂; AMC emergentes; safety cases.
* **QB:** Iron‑bird eléctrico; banco criogénico; demo e‑fan; taxi full‑electric.

**KPIs iniciales**

* E_pax‑km ↓ ≥ 40%; Turnaround ≤ 30 min; MTBUR ↑; ruido SEL ↓ 10–15 dB.

**TRLs & Hitos (12–18 m)**

* TRL3–4: subescala BWB + loop criogénico.
* TRL5–6: HIL/SIL powertrain; taxi.
* TRL6–7: prototipo vuelo + SC H₂/eléctrico.

**Riesgos clave**

* Densidad energética efectiva H₂L + masa aislamiento; gestión térmica; certificación SC.

---

## 4) ONE‑PAGER · AMPEL360‑T‑SPACE (Transporte Tripulado)

**Estrategia evolutiva**

* **Fase A (Suborbital):** 6–10 pax, retorno rápido, ops tipo aeropuerto espacial.
* **Fase B (LEO):** Taxi/logística ligera; docking; life support.
* **Fase C (LEO‑GTO/Gateway):** Reabastecimiento H₂/O₂; federación con partners.

**Arquitectura (QS→FWD→UE→FE→CB→QB)**

* **QS:** Planificación misión/aborts; márgenes térmicos; entry‑guidance asistido.
* **FWD:** Estructura presurizada; TPS reutilizable; GNC alto rendimiento.
* **UE:** Factores humanos; escape/aborto; recuperación rápida.
* **FE:** Integración etapas; ground segment; LSS; docking.
* **CB:** Ruta human‑rating (ESA/NASA); flight safety; verificación independiente.
* **QB:** Drop/hover; captive carry; vuelos libres; post‑flight inspection.

**KPIs iniciales**

* Cadencia ≥ X/mes; turnaround < 2 semanas (Fase A); confiabilidad abort‑safe.

**Riesgos clave**

* TPS reusable a costos razonables; aborts seguros; coordinación regulatoria.

---

## 5) RUTA REGULATORIA Y PARTNERS

* **Air:** Pre‑aplicaciones EASA; definición SC H₂/eléctrico; safety cases.
* **Space:** ESA/NASA HRP, estándares espaciales; autoridades nacionales.
* **Partners clave:** criogenia, pilas H₂, e‑fans, TPS, puertos aeroespaciales.

---

## 6) CI GATES (PR/Commit Conventions)

* **Convenciones PR:** prefijos por capa (`QS/`, `FWD/` …), vínculo UTCS; checklist MAL‑EEM.
* **Validadores:** `link_path_validator.py` y `fcr_enforcer.py` obligatorios; fallo → bloquea merge.
* **Artefactos:** cada PR debe actualizar UTCS (estructura/estilo/hoja) y matrices CB.

---

## 7) Siguientes pasos

1. Crear archivos *README.md* de producto con estas plantillas dentro de `products/…`.
2. Sembrar **GENESIS** y **CANON_FACTS** en `canon/` (ya marcados por el usuario).
3. Inicializar **workflows** de CI (lint + UTCS check + FCR gates).
4. Cargar primeras plantillas de MoC y hazard logs en `tools/templates/`.
5. Abrir *issues* por capa TFA para cada producto (backlog inicial).



