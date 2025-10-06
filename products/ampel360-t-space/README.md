# AMPEL360-T-Space · Transporte Espacial Tripulado

---

## One-Pager Overview

**AMPEL360-T-Space** es un sistema de transporte espacial tripulado con estrategia evolutiva: **Fase A (Suborbital)** → **Fase B (LEO)** → **Fase C (LEO-GTO/Gateway)**. Diseñado para turismo espacial inicial, taxi orbital y logística tripulada ligera con foco en reusabilidad, seguridad y turnaround rápido.

---

## Propuesta de Valor

### Estrategia Evolutiva

#### Fase A: Suborbital (TRL 5-6)
- **Payload**: 6-10 pasajeros
- **Perfil**: Ascenso rápido, apogeo ~100-150 km, experiencia microgravedad ~5 min, retorno
- **Operaciones**: Tipo aeropuerto espacial (horizontal takeoff/landing preferido)
- **Turnaround**: <2 semanas (target)
- **Market**: Turismo espacial, research payloads

#### Fase B: LEO Taxi/Logística (TRL 6-7+)
- **Orbit**: LEO (200-400 km)
- **Payload**: 4-6 crew + cargo ligero
- **Docking**: ISS successor, commercial stations
- **Life Support**: Duración ~1-7 días
- **Market**: Crew rotation, cargo urgente, rescue

#### Fase C: LEO-GTO / Gateway (TRL 7+)
- **Orbit**: LEO → GTO, Lunar Gateway
- **Payload**: 2-4 crew + supplies
- **Refueling**: In-orbit H₂/O₂ replenishment
- **Partnerships**: NASA, ESA, international
- **Market**: Lunar missions, deep space gateway logistics

### Diferenciadores

- **Reusabilidad**: Target >50 vuelos sin overhaul mayor
- **Turnaround rápido**: Fase A <2 semanas, Fase B <1 mes
- **Human-rated**: Desde diseño, path ESA/NASA certification
- **Abort-safe**: Abort modes en todas las fases (pad, ascent, orbit, entry)

---

## Arquitectura Técnica (TFA Flow)

### QS (Quantum Seal) - Planificación Misión

**Objetivo**: Definir misiones, perfiles, sizing, KPIs

**Key Deliverables**:
- Perfiles de misión (suborbital, orbital)
- Análisis de aborts (pad, ascent, entry)
- Sizing preliminar (masa, propulsión, delta-V)
- Trade studies (VTVL vs winged, propellants)
- Entry-guidance asistido (quantum-enhanced trajectory optimization)

**TRL Target**: 2-3

**Location**: `/products/ampel360-t-space/QS/`

---

### FWD (Forward) - Estructura & TPS

**Objetivo**: Diseño estructural, TPS, GNC

**Key Components**:
- **Estructura presurizada**: Crew cabin, pressure vessel, structural loads
- **TPS (Thermal Protection System)**: Reusable, inspectable, low-maintenance
- **GNC**: Guidance, Navigation, Control (ascent, orbit, entry)
- **Propulsión**: Etapas, engines, propellant management
- **Aerodynamics**: Ascent/entry shapes (if winged or lifting body)

**Key Deliverables**:
- Structural concept (CAD, FEA)
- TPS materials selection & trade study
- GNC architecture (sensors, algorithms, redundancy)
- Propulsion system design

**TRL Target**: 3-4

**Location**: `/products/ampel360-t-space/FWD/`

---

### UE (User Experience) - Factores Humanos

**Objetivo**: Diseño centrado en crew/pasajeros

**Key Components**:
- **Cabina tripulada**: 6-10 pax (Fase A), 4-6 crew (Fase B)
- **Factores humanos**: G-loads (ascent/entry), vibración, acústica, vistas
- **Escape/Abort**: Sistemas de abort (launch abort, entry abort)
- **Confort**: Asientos, restraints, iluminación, comunicación
- **Recuperación**: Post-landing egress, medical support

**Key Deliverables**:
- Cabin layout (CAD, renders, mockups)
- Human factors analysis (G-loads, comfort)
- Abort system design (rocket, capsule separation, parachutes)
- Emergency procedures manual

**TRL Target**: 3-4

**Location**: `/products/ampel360-t-space/UE/`

---

### FE (Final Engineering) - LSS & Integración

**Objetivo**: Integración sistemas críticos

**Key Components**:
- **LSS (Life Support System)**: O₂, CO₂ scrubbing, thermal, humedad
- **Docking**: Mecanismos, sensores, approach/contact
- **Ground Segment**: Mission control, telemetry, tracking
- **Avionics**: Flight computer, comms, data handling
- **Thermal**: Radiators, insulation, active cooling

**Key Deliverables**:
- LSS design (O₂ generation/storage, CO₂ removal, ECLSS loops)
- Docking mechanism design (if orbital phases)
- Ground segment architecture
- Avionics block diagram
- Thermal control architecture

**TRL Target**: 4-5

**Location**: `/products/ampel360-t-space/FE/`

---

### CB (Certification Basis) - Human-Rating

**Objetivo**: Ruta human-rating, compliance espacial

**Key Components**:
- **Estándares**: ESA, NASA Human Rating Plan (HRP), national authorities
- **Safety**: FMEA, FTA, hazard analysis (probabilistic risk assessment)
- **Flight Safety**: Independent verification, abort modes demonstration
- **Crew Safety**: Radiation, micrometeorites, EVA (if applicable)
- **Matrices de compliance**: Trazabilidad estándares → evidencia

**Key Deliverables**:
- Human-rating plan (ESA/NASA coordination)
- Safety assessment reports (FMEA, FTA, PRA)
- Flight safety documentation
- Compliance matrices (ESA, NASA, national)
- Certification milestones & authority engagement

**TRL Target**: 4-6

**Location**: `/products/ampel360-t-space/CB/`

---

### QB (Quality Baseline) - Ensayos & Flight Test

**Objetivo**: Verificación, flight test, human-rating demos

**Key Components**:
- **Drop tests**: Parachute deployment, landing dynamics (if applicable)
- **Hover tests**: VTVL (if applicable), stability & control
- **Captive carry**: Aerodynamic loads, separation dynamics (if air-launched)
- **Propulsion tests**: Full thrust, throttle, shutdown/restart
- **LSS tests**: Closed-loop validation, crew environment
- **Free flights**: Suborbital uncrewed, then crewed
- **Post-flight inspection**: TPS integrity, structural health

**Key Deliverables**:
- Drop test results (landing, abort system)
- Hover test data (VTVL control, if applicable)
- Captive carry report (if air-launched)
- Propulsion ground test data
- LSS functional test results
- Free flight test reports (suborbital, orbital)
- Post-flight inspection procedures & data

**TRL Target**: 5-7

**Location**: `/products/ampel360-t-space/QB/`

---

## KPIs Iniciales (Target)

### Fase A (Suborbital)

| KPI | Target |
|-----|--------|
| **Payload** | 6-10 pax |
| **Apogeo** | 100-150 km |
| **Microgravedad** | ~5 min |
| **Turnaround** | <2 semanas |
| **Cadencia** | ≥2 vuelos/mes |
| **Reusabilidad** | >50 vuelos |
| **Abort safety** | Abort modes todas fases |

### Fase B (LEO)

| KPI | Target |
|-----|--------|
| **Payload** | 4-6 crew + 500 kg cargo |
| **Orbit** | LEO 200-400 km |
| **Docking** | ISS/commercial stations |
| **Mission duration** | 1-7 días |
| **Turnaround** | <1 mes |

---

## TRLs & Hitos (12-18 meses)

### TRL 2-3 (Q1-Q2 2024)
- Perfiles de misión suborbital
- Trade studies: config, propulsión, TPS
- Análisis de aborts
- Sizing preliminar

### TRL 3-4 (Q2-Q3 2024)
- Diseño conceptual estructura & TPS
- GNC architecture
- Cabin layout (factores humanos)
- Drop tests (no propulsion)

### TRL 4-5 (Q3-Q4 2024)
- LSS conceptual design
- Abort system design
- Safety analysis (FMEA, FTA)
- Standards matrix (ESA/NASA)
- Propulsion ground tests

### TRL 5 (Q1 2025)
- Hover tests (VTVL, if applicable)
- Captive carry (if air-launched)
- LSS functional tests
- Abort system demo

### TRL 6 (Q2 2025)
- Free flights suborbital (uncrewed)
- TPS validation (entry heating)
- Abort modes demonstration
- Pre-certification discussions (ESA, national)

---

## Riesgos Clave

### Técnicos
- **TPS reusable**: Costos razonables, inspección rápida, durabilidad >50 vuelos
- **Aborts seguros**: Demostración de abort modes (pad, ascent, entry)
- **LSS confiabilidad**: Closed-loop estable, redundancia O₂/CO₂

### Operacionales
- **Turnaround**: Lograr <2 semanas (Fase A) con inspecciones post-vuelo
- **Spaceport**: Selección, licensing, infraestructura
- **Recovery**: Logística recuperación (landing site, weather, crew egress)

### Regulatorios
- **Human-rating**: Coordinación ESA/NASA, demostración probabilistic risk <1:270 LOC/LOM
- **National authorities**: Licensing vuelos tripulados (España, Francia, otros)
- **Liability & insurance**: Cobertura pasajeros, third-party

### Financieros
- **CapEx alto**: Desarrollo Fase A (~€50-150M), Fase B (~€200-500M)
- **Dependencia funding**: ESA (FLPP, HRE), national, private investors

---

## Dependencias & Enlaces

### Upstream (Canon)
- `/canon/GENESIS_ASI-T2.md`: Principios fundacionales
- `/canon/CANON_FACTS.md`: TFA flow, UTCS, domains

### Governance
- `/governance/MAL-EEM/`: Checklist ético (human-rating crítico)
- `/governance/UTCS/`: Trazabilidad
- `/governance/COMPLIANCE/`: Certificación espacial

### Simulación
- `/sim/space/`: GNC suborbital/orbital, entry-guidance

### CAx/QOx
- `/cax/`: CAD, FEA, CFD (entry aerodynamics)
- `/qox/`: Datos ensayos, flight test data

### Partners
- `/docs/PARTNERS.md`: TPS, propulsion, LSS, spaceports
- `/docs/FUNDING_EU.md`: ESA (FLPP, HRE), EIC Accelerator

---

## Status & Next Steps

**Current Status**: Planning / QS phase  
**TRL**: 2  
**Next Milestone**: Complete QS (mission profiles, trade studies) - Q1 2024

**Immediate Actions**:
1. Define suborbital mission profile (altitude, duration, G-loads)
2. Trade study: VTVL vs winged, propellants (H₂/O₂, RP-1/LOX, hybrid)
3. Preliminary abort analysis (modes, safety)
4. Initiate ESA engagement (FLPP, HRE programs)

---

**Versión**: 1.0  
**UTCS**:
```yaml
context: AMPEL360-T-Space / Product Overview
content: Crewed space transport (suborbital → orbital)
cache: refs: /canon/, /governance/, /docs/
structure: TFA flow (QS→FWD→UE→FE→CB→QB)
style: One-pager + phased approach
sheet:
  id: PRODUCT-SPACE-001
  version: 1.0
  date: 2024-Q4
```
