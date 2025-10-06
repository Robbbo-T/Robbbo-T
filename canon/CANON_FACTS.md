# CANON FACTS · ASI-T2

## Hechos Canon Inmutables

Este documento contiene los hechos y reglas que definen el sistema ROBBBO-T. Son inmutables salvo proceso formal de governance.

### TFA Flow (Canon)

```
QS → FWD → UE → FE → CB → QB
```

**Definiciones**:

- **QS (Quantum Seal)**: Definición de requisitos, gemelos digitales, sizing, planificación de misión, KPIs
- **FWD (Forward)**: Diseño forward (aero, estructuras, criogenia, TPS, integración física)
- **UE (User Experience)**: Factores humanos, cabina, HMI, evacuación, ergonomía, accesibilidad
- **FE (Final Engineering)**: Integración de propulsión, sistemas térmicos, BMS, aviónica, LSS
- **CB (Certification Basis)**: Rutas regulatorias, compliance matrices, safety cases, AMC/GM
- **QB (Quality Baseline)**: Ensayos, HIL/SIL, bancos de prueba, flight test, verificación

### UTCS (Universal Threading Context/Content/Cache and Structure/Style/Sheet)

Cada artefacto del proyecto debe incluir:

1. **Context**: Dónde encaja en el sistema global
2. **Content**: El contenido técnico específico
3. **Cache**: Referencias y dependencias
4. **Structure**: Organización lógica
5. **Style**: Formato y presentación
6. **Sheet**: Trazabilidad y metadata

### Domains (AAA…PPP)

Los 15 dominios técnicos cubren el ciclo completo:

| Dominio | Focus |
|---------|-------|
| AAA | Architecture, Airworthiness, Analysis |
| BBB | Baseline, Build, Balance |
| CCC | Certification, Compliance, Configuration |
| DDD | Design, Development, Documentation |
| EEE | Engineering, Energy, Environment |
| FFF | Flight, Fuel, Fabrication |
| GGG | Governance, Ground, GSE |
| HHH | Human Factors, Hydrogen, HUMS |
| III | Integration, Inspection, Information |
| JJJ | Joint/Junction, Jettison, Justification |
| KKK | Knowledge, KPIs, Kit |
| LLL | Lifecycle, Logistics, LH2 |
| MMM | Manufacturing, Maintenance, Materials |
| NNN | Navigation, NOx, Noise |
| OOO | Operations, Optimization, Ops-Excellence |
| PPP | Propulsion, Performance, Production |

### PAx Orientation Markers

- **ONB** (Onboard): Dentro del vehículo, embarcado
- **OUT** (Outboard): Fuera del vehículo, ground support

### Producto Portfolio

#### AMPEL360-T-Air
- **Tipo**: Blended Wing Body (BWB)
- **Propulsión**: H₂ híbrido-eléctrico
- **Características**: Quantum-enhanced optimization
- **Target**: Aviación comercial, reducción 30-60% energía pax-km
- **Certificación**: EASA CS-25 + SC emergentes H₂/eléctrico

#### AMPEL360-T-Space
- **Fase A**: Suborbital (6-10 pax)
- **Fase B**: LEO taxi/logística
- **Fase C**: LEO-GTO, Gateway
- **Certificación**: ESA/NASA Human Rating

### Reglas de Orden Canónico

1. Todo módulo de producto **DEBE** seguir la secuencia `QS→FWD→UE→FE→CB→QB`
2. No se puede saltar capas sin justificación documentada
3. Los PR que rompan el orden serán rechazados por CI gates
4. Cada capa debe actualizar UTCS antes de avanzar

### MAL-EEM (Meta-Alignment Layer)

Toda acción técnica debe pasar estos filtros:

1. **Ética**: ¿Es ético este desarrollo?
2. **Empatía**: ¿Consideramos el impacto en personas?
3. **Meaning**: ¿Tiene sentido en el contexto global?

Checklist MAL-EEM obligatorio en:
- Design reviews
- PR submissions
- Safety assessments
- Certification packages

### CI Gates Obligatorios

Los siguientes gates son **obligatorios** y bloquean merge si fallan:

1. **FCR-1**: Follow-up Chain Rule 1 (validación de inputs/paths)
2. **FCR-2**: Follow-up Chain Rule 2 (trazabilidad QS/UTCS)
3. **Link/Path Validator**: Todos los enlaces deben ser válidos
4. **UTCS Check**: Actualización de trazabilidad obligatoria

### Prefijos de PR por Capa TFA

- `QS/`: Cambios en Quantum Seal
- `FWD/`: Cambios en Forward Design
- `UE/`: Cambios en User Experience
- `FE/`: Cambios en Final Engineering
- `CB/`: Cambios en Certification Basis
- `QB/`: Cambios en Quality Baseline
- `GOV/`: Cambios en Governance
- `CI/`: Cambios en CI/CD

### TRL Targets (12-18 meses)

**Air (AMPEL360-T-Air)**:
- TRL 3-4: Subescala BWB + loop criogénico
- TRL 5-6: HIL/SIL powertrain; taxi demo
- TRL 6-7: Prototipo vuelo + SC H₂/eléctrico

**Space (AMPEL360-T-Space)**:
- TRL 4: Drop tests, concepto validado
- TRL 5: Hover tests, captive carry
- TRL 6: Vuelos libres suborbitales

---

**Versión**: 1.0  
**Estado**: CANON - Modificación requiere governance approval  
**Última actualización**: 2024
