#!/bin/bash

cd /workspaces/Robbbo-T/OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/D-DEFENCE_CYBERSECURITY_SAFETY

# Create CA directories if not exist
mkdir -p CA-D-001-PLATFORM-SURVIVABILITY
mkdir -p CA-D-002-CYBERSECURITY-ARCHITECTURE
mkdir -p CA-D-003-CRYPTO-PQC-KMS
mkdir -p CA-D-004-SECURE-BOOT-ATTESTATION
mkdir -p CA-D-005-NETWORK-SECURITY-COMMS
mkdir -p CA-D-006-THREAT-MODELING-RISK
mkdir -p CA-D-007-IDS-MONITORING-DETECTION
mkdir -p CA-D-008-SAFETY-ENGINEERING
mkdir -p CA-D-009-FAULT-MANAGEMENT-FDI-SRM
mkdir -p CA-D-010-SECURE-SUPPLY-CHAIN
mkdir -p CA-D-011-INCIDENT-RESPONSE-DRILLS
mkdir -p CA-D-012-GNSS-INTEGRITY-ANTI-JAM
mkdir -p CA-D-013-QUANTUM-SECURITY-INTERFACES
mkdir -p CA-D-014-PHYSICAL-SECURITY-ANTI-TAMPER
mkdir -p CA-D-015-REGULATORY-COMPLIANCE

# Function to create lifecycle folders
create_lifecycle_folders() {
  local base_path=$1
  mkdir -p "$base_path/01-Requirements"
  mkdir -p "$base_path/02-Design"
  mkdir -p "$base_path/03-Building-Prototyping"
  mkdir -p "$base_path/04-Executables-Packages"
  mkdir -p "$base_path/05-Verification-Validation"
  mkdir -p "$base_path/06-Integration-Qualification"
  mkdir -p "$base_path/07-Certification-Security"
  mkdir -p "$base_path/08-Production-Scale"
  mkdir -p "$base_path/09-Ops-Services"
  mkdir -p "$base_path/10-MRO"
  mkdir -p "$base_path/11-Sustainment-Recycle"
}

# CA-D-001
for i in 001 002 003 004 005 006 007; do
  case $i in
    001) name="EMI-EMC-HARDENING-GUIDES" ;;
    002) name="LIGHTNING-LPS-INTERFACES" ;;
    003) name="HIRF-EMP-PROTECTION-ZONES" ;;
    004) name="SHIELDING-TOPLOGIES-BONDING" ;;
    005) name="CABLE-ROUTING-SEGREGATION" ;;
    006) name="THERMAL-SMOKE-PARTITIONING" ;;
    007) name="ENV-QUAL-DO160-MATRICES" ;;
  esac
  ci_path="CA-D-001-PLATFORM-SURVIVABILITY/CI-CA-D-001-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-002
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="ZERO-TRUST-SEGMENTATION" ;;
    002) name="RBAC-ABAC-POLICY-MODELS" ;;
    003) name="SERVICE-MESH-POLICY-ENFORCER" ;;
    004) name="SECURE-GATEWAYS-ARINC-AFDX-TSN" ;;
    005) name="DET-EVIDENCE-ANCHORING" ;;
    006) name="SECURITY-BY-DESIGN-CHECKS" ;;
  esac
  ci_path="CA-D-002-CYBERSECURITY-ARCHITECTURE/CI-CA-D-002-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-003
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="KMS-HSM-ARCHITECTURE" ;;
    002) name="PQC-KYBER-DILITHIUM-PROFILES" ;;
    003) name="KEY-ROTATION-LIFECYCLE" ;;
    004) name="MTLS-IPSEC-TLS13-SUITES" ;;
    005) name="AT-REST-ENCRYPTION-SCHEMAS" ;;
    006) name="SECRET-MANAGEMENT-VAULT-INTF" ;;
  esac
  ci_path="CA-D-003-CRYPTO-PQC-KMS/CI-CA-D-003-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-004
for i in 001 002 003 004 005; do
  case $i in
    001) name="MEASURED-BOOT-CHAIN" ;;
    002) name="FIRMWARE-SIGNING-SBOM-BOMS" ;;
    003) name="FAT-FLIGHT-AUTH-TOKENS" ;;
    004) name="RUNTIME-ATTESTATION-QUOTES" ;;
    005) name="RECOVERY-ROLLBACK-PROCEDURES" ;;
  esac
  ci_path="CA-D-004-SECURE-BOOT-ATTESTATION/CI-CA-D-004-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-005
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="ARINC429-SECURE-BRIDGES" ;;
    002) name="AFDX-TSN-SECURITY-PROFILES" ;;
    003) name="ATM-AOC-LINK-HARDENING" ;;
    004) name="ROS2-DDS-SECURE-POLICIES" ;;
    005) name="OPC-UA-SCADA-SECURE-CHANNELS" ;;
    006) name="VPN-SGRE-WIREGUARD-GATEWAYS" ;;
  esac
  ci_path="CA-D-005-NETWORK-SECURITY-COMMS/CI-CA-D-005-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-006
for i in 001 002 003 004 005; do
  case $i in
    001) name="TARA-ISO21434-TEMPLATES" ;;
    002) name="STRIDE-ATTACK-TREES" ;;
    003) name="MISSION-HAZARD-MAPPING" ;;
    004) name="RISK-METRICS-HEATMAPS" ;;
    005) name="CONTROL-SET-TRACEABILITY" ;;
  esac
  ci_path="CA-D-006-THREAT-MODELING-RISK/CI-CA-D-006-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-007
for i in 001 002 003 004 005; do
  case $i in
    001) name="NIDS-ARINC-AFDX-TSN-SENSORS" ;;
    002) name="HIDS-RTOS-LINUX-AGENTS" ;;
    003) name="ANOMALY-ML-PROFILES" ;;
    004) name="LOG-NORMALIZATION-SCHEMAS" ;;
    005) name="DET-PUBLISHERS-WORM" ;;
  esac
  ci_path="CA-D-007-IDS-MONITORING-DETECTION/CI-CA-D-007-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-008
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="FHA-FUNCTIONAL-HAZARD-ANALYSIS" ;;
    002) name="PSSA-PRELIM-SAFETY-ASSESSMENT" ;;
    003) name="SSA-SYSTEM-SAFETY-ASSESSMENT" ;;
    004) name="FTA-FAULT-TREE-ANALYSIS" ;;
    005) name="FMEA-FMECA-LIBRARY" ;;
    006) name="SAFETY-REQUIREMENTS-RTM" ;;
  esac
  ci_path="CA-D-008-SAFETY-ENGINEERING/CI-CA-D-008-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-009
for i in 001 002 003 004 005; do
  case $i in
    001) name="FAULT-DETECTION-MONITORS" ;;
    002) name="ISOLATION-DIAGNOSTIC-TREES" ;;
    003) name="RECOVERY-SAFE-STATES" ;;
    004) name="SIMPLEX-FALLBACK-MODES" ;;
    005) name="ALERTING-POLICIES-DO178C" ;;
  esac
  ci_path="CA-D-009-FAULT-MANAGEMENT-FDI-SRM/CI-CA-D-009-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-010
for i in 001 002 003 004 005; do
  case $i in
    001) name="SBOM-SLSA-PROVENANCE" ;;
    002) name="3RD-PARTY-COMPONENT-REVIEWS" ;;
    003) name="CVE-VULN-MANAGEMENT" ;;
    004) name="BUILD-HERMETICITY-CI-CD" ;;
    005) name="HW-SERIALIZATION-TRACE" ;;
  esac
  ci_path="CA-D-010-SECURE-SUPPLY-CHAIN/CI-CA-D-010-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-011
for i in 001 002 003 004 005; do
  case $i in
    001) name="PLAYBOOKS-IR-ATM-AOC" ;;
    002) name="TABLETOP-EXERCISES" ;;
    003) name="RED-TEAM-EMULATION" ;;
    004) name="POST-INCIDENT-DET-REPORTS" ;;
    005) name="SERVICE-RESTORE-RUNBOOKS" ;;
  esac
  ci_path="CA-D-011-INCIDENT-RESPONSE-DRILLS/CI-CA-D-011-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-012
for i in 001 002 003 004 005; do
  case $i in
    001) name="RAIM-SBAS-CHECKS" ;;
    002) name="ANTI-SPOOF-DETECTION" ;;
    003) name="ANTENNA-PLACEMENT-AJ-STRATEGY" ;;
    004) name="TIME-SYNC-HOLDOVER-PROFILES" ;;
    005) name="INTEGRITY-ALERTING-THRESHOLDS" ;;
  esac
  ci_path="CA-D-012-GNSS-INTEGRITY-ANTI-JAM/CI-CA-D-012-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-013
for i in 001 002 003 004 005; do
  case $i in
    001) name="QKD-GW-ABSTRACTIONS" ;;
    002) name="QSAFE-POLICY-COMPAT-MATRIX" ;;
    003) name="QPU-CONTAINMENT-BOUNDARIES" ;;
    004) name="QAL-RESULT-VALIDATION-RULES" ;;
    005) name="DET-FORENSICS-QUANTUM" ;;
  esac
  ci_path="CA-D-013-QUANTUM-SECURITY-INTERFACES/CI-CA-D-013-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-014
for i in 001 002 003 004 005; do
  case $i in
    001) name="TAMPER-EVIDENT-SEALS" ;;
    002) name="MESH-TAMPER-SWITCHES" ;;
    003) name="LOCKOUT-TAGOUT-INTERLOCKS" ;;
    004) name="ACCESS-CONTROL-HARDWARE" ;;
    005) name="STORAGE-TRANSPORT-SECURITY" ;;
  esac
  ci_path="CA-D-014-PHYSICAL-SECURITY-ANTI-TAMPER/CI-CA-D-014-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-D-015
for i in 001 002 003 004 005; do
  case $i in
    001) name="DO326A-ED202A-CHECKLISTS" ;;
    002) name="DO356A-AIRWORTHY-SEC-GUIDE" ;;
    003) name="ARP4754A-4761A-MAPPING" ;;
    004) name="ISO21434-IEC62443-CROSSREF" ;;
    005) name="AUDIT-PACKS-DET-INDEX" ;;
  esac
  ci_path="CA-D-015-REGULATORY-COMPLIANCE/CI-CA-D-015-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

echo "All CI directories created successfully for D-DEFENCE_CYBERSECURITY_SAFETY."
