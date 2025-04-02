# COAFI Part I – ATA 26: FIRE PROTECTION  
**Document ID:** GP-AM-EDR-26-001  
**Status:** Draft | **Platform:** Q-01 / AEHCS  
**Author:** A. Pelliccia  
**Date:** [April 01 2025]  

## 26.1 Fire Detection System

### 26.1.1 Fire Detector Locations

- **Engine Bay:**  
  Dual-loop detectors positioned at 45° intervals around the engine core (X: +4.32 m, Y: ±1.05 m, Z: -0.92 m).  
  Proximity to fuel injection manifolds and quantum pulse ignition module (QPS-MOD) considered.  
  Redundancy ensured via loop isolation.

- **Cargo Compartments:**  
  Smoke/thermal detectors installed near structural junctions (frame 52–58),  
  especially in areas adjacent to hydrogen cryo-containers.  
  Sensor placement considers airflow stagnation zones and duct inlets.

- **Cabin Areas:**  
  Ceiling-mounted smoke detectors at 2.5 m intervals, including above galley and lavatories.  
  AEHCS cabins feature additional flame detection sensors near energy-conductive wall panels.  
  Integration with digital cabin display alert (XAI-Panel 26).

- **Electrical Bays (E-Bays 1 & 2):**  
  Localized heat rate-of-rise detectors near quantum converter blocks (Z: -0.45 m to -0.80 m).  
  High-risk areas include MOD-TWIN power supplies and fast-discharge capacitors.  
  Shielded from electromagnetic interference via cryo-fiber jackets.

![Fire Detector Placement Overview – Q-01 AEHCS Configuration](/mnt/data/A_technical_line_diagram_titled_"Fire_Detector_Pla.png")

### 26.1.2 Fire Detector Specifications
- Type: Optical / Infrared / Dual-Sensor
- Detection Time: [Insert value, e.g., <2s]
- Operating Range: [e.g., -50°C to +85°C]
- Certifications: DO-160, MIL-STD-810

### 26.1.3 System Logic & Wiring
- Detection Logic: AND/OR configuration, zone-based
- Fault Monitoring: Loop integrity + auto-test cycle
- **Schematic Ref:** GP-AM-DRW-26-002

---

## 26.2 Fire Suppression System

### 26.2.1 Extinguisher System Description
- Fixed Systems: Engine nacelles, APU bays
- Portable Units: Cabin, cockpit, cargo
- Integration with Q-01 cryo-safety protocols

### 26.2.2 Suppression Agent Specifications
- Agent Types: Halon 1301 (phased-out), Novec 1230, CO₂, Cryo-adapted gel
- Agent Distribution Method: High-speed discharge tubes, zonal manifolds
- Environmental Compliance: ICAO/FAA Fire Safety Guidelines

### 26.2.3 Activation Procedures
- Manual: Cockpit switches, maintenance panels
- Automatic: Triggered via detection threshold
- Post-activation protocols and safety locks
- **Procedure Ref:** GP-AM-PROC-26-001

---

## 26.3 Fire Zones and Protection Features

### 26.3.1 Fire Zone Definition Drawings
- Zone 1: Engine Compartments
- Zone 2: APU & Electrical Bays
- Zone 3: Passenger Cabin
- Zone 4: Avionic Core (AEHCS)
- **Drawing Ref:** GP-AM-DRW-26-003

### 26.3.2 Firewall and Barrier Specifications
- Materials: Titanium alloy / Ceramic composite / Aerogel insulators
- Fire Rating: 30 min minimum at 1100°C
- Penetration Sealing: Q-Grade fireproof bushings

### 26.3.3 Flammability and Smoke Standards
- FAR 25.853 / CS 25.853 compliance
- Materials tested for:
  - Flame spread
  - Smoke density
  - Toxicity index

---

## Special Considerations

### Q-01 Platform
- **Cryogenic Risks:**
  - Liquid hydrogen proximity to avionics/firewalls
  - Sensor integration for leak + ignition risk
- **Fire protection integration with:**
  - Quantum pulse module
  - High-voltage quantum energy routing (MOD-QPS)

### AEHCS Configuration
- **High-voltage power interfaces:** 800V+
- **Thermal runaway containment strategies**
- Multi-agent suppression for electro-thermal zones

---

## Linked Documents

- [GP-AM-EDR-26-002-CAL]: Fire Suppression Volume Calculations  
- [GP-AM-DRW-26-004]: Suppression Agent Routing Schematics  
- [GP-Q-TEST-49-026]: Fire Resistance Test Results for QPS Modules  

---

# COAFI Part I – ATA 32: LANDING GEAR SYSTEM
**Document ID:** REQ-32-LG-1.0
**Review Type:** PDR (Preliminary Design Review)
**Author:** [Author Name]
**Date:** [Date]

## System Overview

The Landing Gear system is a critical component of the aircraft, responsible for supporting the aircraft during ground operations, takeoff, and landing. The system includes the main landing gear, nose gear, and associated hydraulic and electronic control systems. The primary functions of the Landing Gear system are extension and retraction, which are essential for safe aircraft operations.

## Functional Requirements

### 1. Extension Capability
- **REQ-32-LG-EXT-001:** The Landing Gear system shall extend the landing gear within 10 seconds.
- **REQ-32-LG-EXT-002:** The extension mechanism shall be operable under all standard flight conditions.
- **REQ-32-LG-EXT-003:** The system shall provide feedback to the cockpit indicating successful extension.

### 2. Retraction Capability
- **REQ-32-LG-RET-001:** The Landing Gear system shall retract the landing gear within 10 seconds.
- **REQ-32-LG-RET-002:** The retraction mechanism shall be operable under all standard flight conditions.
- **REQ-32-LG-RET-003:** The system shall provide feedback to the cockpit indicating successful retraction.

## Performance Requirements
- **REQ-32-LG-PERF-001:** The Landing Gear system shall operate in temperatures ranging from -40°C to +70°C.
- **REQ-32-LG-PERF-002:** The system shall withstand the impact forces experienced during landing without failure.

## Interface Requirements
- **REQ-32-LG-INT-001:** The Landing Gear system shall interface with the aircraft's hydraulic system.
- **REQ-32-LG-INT-002:** The system shall interface with the cockpit control panel for operation commands and status feedback.

## Safety Requirements
- **REQ-32-LG-SAFE-001:** The Landing Gear system shall include a fail-safe mechanism to ensure gear extension in case of hydraulic failure.
- **REQ-32-LG-SAFE-002:** The system shall undergo regular maintenance checks as per the aircraft maintenance schedule.

## Additional Sections
- Environmental Requirements
- Verification and Validation
- Compliance with Regulatory Standards
