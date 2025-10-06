# Domains (AAA…PPP)

This directory contains the 15 technical domains that organize all engineering work in the ROBBBO-T project.

---

## Domain Structure

Each domain represents a vertical slice of expertise across all products and TFA layers.

| Domain | Focus Areas |
|--------|-------------|
| **AAA** | Architecture, Airworthiness, Analysis |
| **BBB** | Baseline, Build, Balance |
| **CCC** | Certification, Compliance, Configuration |
| **DDD** | Design, Development, Documentation |
| **EEE** | Engineering, Energy, Environment |
| **FFF** | Flight, Fuel, Fabrication |
| **GGG** | Governance, Ground, GSE (Ground Support Equipment) |
| **HHH** | Human Factors, Hydrogen, HUMS (Health & Usage Monitoring) |
| **III** | Integration, Inspection, Information |
| **JJJ** | Joint/Junction, Jettison, Justification |
| **KKK** | Knowledge, KPIs, Kit |
| **LLL** | Lifecycle, Logistics, LH2 (Liquid Hydrogen) |
| **MMM** | Manufacturing, Maintenance, Materials |
| **NNN** | Navigation, NOx, Noise |
| **OOO** | Operations, Optimization, Ops-Excellence |
| **PPP** | Propulsion, Performance, Production |

---

## Usage

Domains are cross-cutting:
- A single component (e.g., H₂ tank) may involve multiple domains:
  - **AAA**: System architecture
  - **EEE**: Energy storage analysis
  - **HHH**: H₂ safety
  - **LLL**: LH2 handling
  - **MMM**: Manufacturing processes

Work is organized in `/products/<product>/<TFA-layer>/` but tagged by domain for cross-product learnings and standards.

---

## Domain Ownership

Each domain should have:
- Lead engineer(s)
- Standards and best practices
- Cross-product synergies documented

---

**Version**: 1.0  
**Last Updated**: 2024-Q4
