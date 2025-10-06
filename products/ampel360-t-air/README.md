# AMPEL360-T-Air · BWB H₂ Hybrid-Electric (Quantum-Enhanced)

---

## One-Pager Overview

**AMPEL360-T-Air** es un avión de transporte comercial de configuración **BWB (Blended Wing Body)** con propulsión **H₂ híbrido-eléctrica** y optimización **Quantum-enhanced**. Representa una ruptura tecnológica en eficiencia energética, emisiones y ruido para aviación comercial.

---

## Propuesta de Valor

### Eficiencia Energética
- **30-60% reducción** en energía por pasajero-km vs configuración cilíndrica convencional
- Integración óptima BWB (lift distribution) + H₂ (densidad energética) + eléctrico (eficiencia propulsiva)

### Impacto Ambiental
- **Cero CO₂** en operación (H₂ + electricidad renovable)
- **Well-to-wake**: Dependiente de producción H₂ (target: H₂ verde)
- **Ruido**: 10-15 dB reducción en SEL (Sound Exposure Level) vs turbofans

### Operacional
- **Turnaround**: ≤30 min (target similar a convencional)
- **Range**: 1500-3000 km (mercado regional/medio alcance)
- **Payload**: 150-200 pax (configuración típica)
- **MTBUR** (Mean Time Between Unscheduled Removals): Superior a convencional (menos partes móviles)

### Quantum-Enhanced
- **Optimización energética**: Rutas, climb/descent, energy dispatch en tiempo real
- **Mantenimiento predictivo**: ML/AI con procesamiento cuántico para HUMS
- **Diseño**: Optimización topológica y aeroelástica con algoritmos cuánticos

---

## Arquitectura Técnica (TFA Flow)

### QS (Quantum Seal) - Requisitos & Sizing

**Objetivo**: Definir requisitos, sizing H₂, KPIs, modelos de demanda

**Key Deliverables**:
- Modelos de sizing tanques H₂L (masa, volumen, BOG)
- Análisis de demanda energética por misión
- KPIs: E_pax-km, turnaround, MTBUR, ruido SEL
- Trade studies: configuración, arquitectura propulsiva

**TRL Target**: 2-3

**Location**: `/products/ampel360-t-air/QS/`

---

### FWD (Forward) - Diseño Aerodinámico & Criogenia

**Objetivo**: Diseño forward (aero, estructuras, integración criogénica)

**Key Components**:
- **BWB Configuration**: Geometría, lift distribution, stability & control
- **Tanques H₂**: Integración conformal ONB (onboard), aislamiento, BOG management
- **Distribución de masas**: CG, MOI (momentos de inercia), balance
- **Safety H₂**: Ventilación, inertización, detección fugas

**Key Deliverables**:
- Geometría BWB (CAD, CFD baseline)
- Integración tanques criogénicos
- Trade studies: tamaño tanques, posición, safety

**TRL Target**: 3-4

**Location**: `/products/ampel360-t-air/FWD/`

---

### UE (User Experience) - Cabina & Factores Humanos

**Objetivo**: Diseño centrado en humanos (crew, pax)

**Key Components**:
- **Cabina**: Layout, asientos, iluminación, ventilación
- **HMI Crew**: Displays energía, H₂ status, emergencias
- **Evacuación**: Salidas, slides, tiempo evacuación <90 seg
- **Ergonomía**: Accesibilidad, confort, G-loads
- **Safety**: Procedimientos emergencia H₂

**Key Deliverables**:
- Cabin layout (CAD, renders)
- HMI mockups (cockpit, cabin crew panel)
- Evacuation analysis (sim, timing)
- Safety procedures manual

**TRL Target**: 3-4

**Location**: `/products/ampel360-t-air/UE/`

---

### FE (Final Engineering) - Propulsión & Sistemas

**Objetivo**: Integración de propulsión, sistemas térmicos, aviónica

**Key Components**:
- **Arquitectura propulsiva**: Pila(s) H₂ + turbogenerador H₂ (pico/backup) → e-fans distribuidos
- **BMS** (Battery Management System): Baterías buffer, safety, thermal
- **Thermal Management**: Cooling loops, waste heat recovery, H₂ evaporation cooling
- **Aviónica**: FBW (Fly-By-Wire) para BWB, energy management, FADEC e-fans
- **Distribución eléctrica**: DC bus, redundancia, fault tolerance

**Key Deliverables**:
- Propulsion system architecture (block diagrams, power flow)
- BMS design (cell monitoring, SOC/SOH, safety)
- Thermal management architecture
- Avionics block diagram (FBW, energy, navigation)

**TRL Target**: 4-5

**Location**: `/products/ampel360-t-air/FE/`

---

### CB (Certification Basis) - Regulatorio

**Objetivo**: Ruta de certificación, compliance, safety cases

**Key Components**:
- **Baseline**: EASA CS-25 (Large Aeroplanes)
- **Special Conditions** (SC): H₂ systems, electric propulsion, BWB (novel config)
- **AMC/GM**: Acceptable Means of Compliance, Guidance Material
- **Safety Cases**: Hazard analysis (PHA, FHA, FTA, FMEA), risk mitigation
- **Matrices de compliance**: Trazabilidad requisitos → evidencia

**Key Deliverables**:
- Compliance matrix (CS-25 + SC)
- Special Conditions draft (coordinado con EASA)
- Safety assessment reports (PHA, FHA, FTA, FMEA)
- Certification plan (milestones, authorities engagement)

**TRL Target**: 4-6

**Location**: `/products/ampel360-t-air/CB/`

---

### QB (Quality Baseline) - Ensayos & Verificación

**Objetivo**: Verificación física, ensayos, flight test

**Key Components**:
- **HIL/SIL**: Hardware-In-Loop / Software-In-Loop (powertrain, avionics)
- **Bancos de ensayo**: Criogenia (fill/drain, BOG, thermal), e-fan (thrust, efficiency)
- **Iron-bird**: Integración sistemas (eléctrico, hidráulico, FBW)
- **Ground tests**: Taxi (electric), structural (static, fatigue)
- **Flight test**: Prototipo, envelope expansion, certification flights

**Key Deliverables**:
- HIL/SIL test results (powertrain validation)
- Banco criogénico test report
- E-fan ground test data (thrust, efficiency, noise)
- Iron-bird integration report
- Taxi test results
- Flight test plan & results

**TRL Target**: 5-7

**Location**: `/products/ampel360-t-air/QB/`

---

## KPIs Iniciales (Target)

| KPI | Target | Baseline (Convencional) |
|-----|--------|-------------------------|
| **E_pax-km** | ↓ ≥40% | 100% (reference) |
| **CO₂ operación** | 0 kg/flight | ~5000 kg/flight (kerosene) |
| **Ruido SEL** | ↓ 10-15 dB | ~90 dB (turbofan) |
| **Turnaround** | ≤30 min | ~30 min |
| **Range** | 1500-3000 km | 3000+ km (narrow-body) |
| **Payload** | 150-200 pax | 150-200 pax |
| **MTBUR** | ↑20% | 100% (reference) |

---

## TRLs & Hitos (12-18 meses)

### TRL 2-3 (Q1-Q2 2024)
- Completar sizing H₂ y trade studies
- Diseño conceptual BWB
- Selección arquitectura propulsiva

### TRL 3-4 (Q2-Q3 2024)
- Integración criogénica
- CFD baseline BWB
- Diseño cabina y HMI
- Subescala BWB (wind tunnel o RC flight)

### TRL 4-5 (Q3-Q4 2024)
- Diseño propulsión (pila + turbogen + e-fans)
- BMS y thermal management
- HIL/SIL powertrain
- Banco criogénico

### TRL 5-6 (Q1 2025)
- Demo e-fan (ground test)
- Iron-bird eléctrico
- Taxi test (propulsión eléctrica)
- Special Conditions draft (EASA)

### TRL 6-7 (Q2 2025+)
- Prototipo vuelo
- Flight test campaign
- Certificación EASA

---

## Riesgos Clave

### Técnicos
- **Densidad energética efectiva H₂L**: Incluyendo masa de tanques y aislamiento
- **Gestión térmica**: Integración cooling loops, waste heat, H₂ evaporation
- **Certificación SC**: Proceso largo, coordinación EASA, safety cases robustos

### Operacionales
- **Infraestructura H₂**: Refueling, storage, safety ground
- **Turnaround**: Lograr ≤30 min con refueling H₂
- **Mantenimiento**: Training, tooling, supply chain

### Regulatorios
- **Special Conditions**: Definición y aprobación con EASA
- **Safety cases**: Aceptación de novel technologies (H₂, eléctrico, BWB)

### Financieros
- **CapEx alto**: Desarrollo prototipo TRL 7+ (~€100-300M)
- **Dependencia funding**: Grants EU (Clean Aviation, SESAR), private investment

---

## Dependencias & Enlaces

### Upstream (Canon)
- `/canon/GENESIS_ASI-T2.md`: Principios fundacionales
- `/canon/CANON_FACTS.md`: TFA flow, UTCS, domains

### Governance
- `/governance/MAL-EEM/`: Checklist ético
- `/governance/UTCS/`: Trazabilidad
- `/governance/COMPLIANCE/`: Certificación

### Simulación
- `/sim/air/`: Modelos propulsión, aero, thermal

### CAx/QOx
- `/cax/`: CAD, CFD, FEA outputs
- `/qox/`: Datos ensayos, métricas

### Partners
- `/docs/PARTNERS.md`: Proveedores criogenia, pilas, e-fans
- `/docs/FUNDING_EU.md`: Grants (Clean Aviation, EIC)

---

## Status & Next Steps

**Current Status**: Planning / QS phase  
**TRL**: 2  
**Next Milestone**: Complete QS (sizing, KPIs, trade studies) - Q1 2024

**Immediate Actions**:
1. Finalize H₂ sizing models (tanques, BOG, mass)
2. BWB trade study (config selection)
3. Propulsion architecture selection
4. Initiate EASA pre-engagement

---

**Versión**: 1.0  
**UTCS**:
```yaml
context: AMPEL360-T-Air / Product Overview
content: BWB H₂ Hybrid-Electric commercial aircraft
cache: refs: /canon/, /governance/, /docs/
structure: TFA flow (QS→FWD→UE→FE→CB→QB)
style: One-pager + detailed sections
sheet:
  id: PRODUCT-AIR-001
  version: 1.0
  date: 2024-Q4
```
