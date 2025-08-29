# D-DEFENCE_CYBERSECURITY_SAFETY

## Overview
Comprehensive defense, cybersecurity, and safety domain ensuring platform survivability, cybersecurity architecture, and safety engineering for the AMPEL360 H2 BWB configuration.

## Constituent Assemblies (CAs)

### CA-D-001-PLATFORM-SURVIVABILITY
EMI/EMC hardening, lightning protection interfaces, HIRF/EMP protection zones, shielding topologies, cable routing segregation, and DO-160 environmental qualification.

### CA-D-002-CYBERSECURITY-ARCHITECTURE
Zero-trust segmentation, RBAC/ABAC policy models, service mesh policy enforcement, secure gateways (ARINC/AFDX/TSN), and DET evidence anchoring.

### CA-D-003-CRYPTO-PQC-KMS
Key management systems, post-quantum cryptography (Kyber/Dilithium), key rotation lifecycle, mTLS/IPSec/TLS1.3 suites, and secret management.

### CA-D-004-SECURE-BOOT-ATTESTATION
Measured boot chain, firmware signing, flight authentication tokens, runtime attestation, and recovery procedures.

### CA-D-005-NETWORK-SECURITY-COMMS
ARINC-429 secure bridges, AFDX/TSN security profiles, ATM/AOC link hardening, ROS2/DDS security policies, and VPN gateways.

### CA-D-006-THREAT-MODELING-RISK
TARA ISO 21434 templates, STRIDE attack trees, mission hazard mapping, risk metrics, and control set traceability.

### CA-D-007-IDS-MONITORING-DETECTION
Network/host intrusion detection systems, anomaly ML profiles, log normalization, and DET publishers.

### CA-D-008-SAFETY-ENGINEERING
Functional Hazard Analysis (FHA), Preliminary/System Safety Assessment (PSSA/SSA), Fault Tree Analysis (FTA), FMEA/FMECA library, and safety requirements traceability.

### CA-D-009-FAULT-MANAGEMENT-FDI-SRM
Fault detection monitors, isolation diagnostic trees, recovery safe states, Simplex fallback modes, and DO-178C alerting policies.

### CA-D-010-SECURE-SUPPLY-CHAIN
SBOM/SLSA provenance, third-party component reviews, CVE vulnerability management, build hermeticity, and hardware serialization.

### CA-D-011-INCIDENT-RESPONSE-DRILLS
Incident response playbooks, tabletop exercises, red team emulation, post-incident DET reports, and service restoration.

### CA-D-012-GNSS-INTEGRITY-ANTI-JAM
RAIM/SBAS checks, anti-spoofing detection, antenna placement strategy, time sync holdover, and integrity alerting.

### CA-D-013-QUANTUM-SECURITY-INTERFACES
Quantum Key Distribution (QKD) abstractions, quantum-safe policy compatibility, QPU containment boundaries, and quantum forensics.

### CA-D-014-PHYSICAL-SECURITY-ANTI-TAMPER
Tamper-evident seals, mesh tamper switches, lockout/tagout interlocks, access control hardware, and storage/transport security.

### CA-D-015-REGULATORY-COMPLIANCE
DO-326A/ED-202A checklists, DO-356A airworthiness security guide, ARP4754A/4761A mapping, ISO 21434/IEC 62443 cross-reference, and audit packs.

## Domain Boundaries
- Security policies and cybersecurity architecture (this domain)
- Electronic control units → E3-ELECTRONICS_DIGITAL_INSTRUMENTS
- Operating system security → O-OPERATING_SYSTEMS_NAVIGATION_HPC
- Network protocols → L2-LINKS_AND_COMMUNICATIONS