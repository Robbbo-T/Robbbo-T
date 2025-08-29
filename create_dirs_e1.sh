#!/bin/bash

cd /workspaces/Robbbo-T/OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/E1-ENVIRONMENTAL_REMEDIATION_CIRCULARITY

# Create CA directories if not exist
mkdir -p CA-E1-001-ECS-CABIN-AIR-SYSTEM
mkdir -p CA-E1-002-PRESSURIZATION-VENTILATION
mkdir -p CA-E1-003-ICE-AND-RAIN-PROTECTION
mkdir -p CA-E1-004-FIRE-DETECTION-SUPPRESSION
mkdir -p CA-E1-005-H2-LEAK-VENTING-PURGE-SAFETY
mkdir -p CA-E1-006-WATER-WASTE-SYSTEMS
mkdir -p CA-E1-007-NOISE-EMISSIONS-CONTRAIL-MGMT
mkdir -p CA-E1-008-THERMAL-MANAGEMENT-NONCRYO
mkdir -p CA-E1-009-REMEDIATION-CIRCULARITY-LIFECYCLE
mkdir -p CA-E1-010-BIOSECURITY-AIR-QUALITY
mkdir -p CA-E1-011-DRAINS-CONDENSATE-ICE-MGMT
mkdir -p CA-E1-012-GROUND-ENV-SAFETY-REMEDIATION

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

# CA-E1-001
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="ECS-HEAT-EXCHANGER-CORES" ;;
    002) name="ECS-MIX-MANIFOLD-DUCTS" ;;
    003) name="ECS-RECIRC-HEPA-ULPA-MODULES" ;;
    004) name="ECS-RECIRC-FANS-MOUNTS" ;;
    005) name="ECS-RAM-AIR-INLET-OUTLET-GEOM" ;;
    006) name="ECS-BYPASS-DOORS-LOUVERS" ;;
  esac
  ci_path="CA-E1-001-ECS-CABIN-AIR-SYSTEM/CI-CA-E1-001-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E1-002
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="OUTFLOW-VALVE-STRUCTURES" ;;
    002) name="SAFETY-RELIEF-VALVES-HOUSINGS" ;;
    003) name="CABIN-PRESSURE-SENSOR-MOUNTS" ;;
    004) name="DIFF-PRESS-DUCTING" ;;
    005) name="CONTROLLED-LEAKAGE-PATHS" ;;
    006) name="VENT-INGESTION-SCREENS" ;;
  esac
  ci_path="CA-E1-002-PRESSURIZATION-VENTILATION/CI-CA-E1-002-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E1-003
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="ELEC-THERMAL-MATS-L/E-ZONING" ;;
    002) name="DEICING-BOOTS-INTERFACES" ;;
    003) name="PICCOLO-MANIFOLDS-DUCTS" ;;
    004) name="ICE-SENSORS-BRACKETS" ;;
    005) name="DRAINAGE-AND-ANTI-ICE-DRIPS" ;;
    006) name="LEADING-EDGE-THERMAL-INSUL" ;;
  esac
  ci_path="CA-E1-003-ICE-AND-RAIN-PROTECTION/CI-CA-E1-003-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E1-004
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="FIRE-BOTTLE-RACKS-BRACKETS" ;;
    002) name="DISCHARGE-LINES-NOZZLES" ;;
    003) name="BURST-DISCS-VENT-PATHS" ;;
    004) name="DETECTOR-LOOPS-ROUTING" ;;
    005) name="CARGO-BAY-SUPPRESSION-GEOM" ;;
    006) name="AVIONICS-BAY-FIRE-ZONING" ;;
  esac
  ci_path="CA-E1-004-FIRE-DETECTION-SUPPRESSION/CI-CA-E1-004-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E1-005
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="H2-SENSOR-GRID-MOUNTS" ;;
    002) name="VENT-MASTS-AEROSHAPE" ;;
    003) name="PURGE-DUCTS-MANIFOLDS" ;;
    004) name="ZONE-CLASSIFICATION-ATEX" ;;
    005) name="SEALING-GASKETS-BARRIERS" ;;
    006) name="GAS-SAMPLING-PORTS" ;;
  esac
  ci_path="CA-E1-005-H2-LEAK-VENTING-PURGE-SAFETY/CI-CA-E1-005-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E1-006
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="POTABLE-TANK-LINERS-BAFFLES" ;;
    002) name="POTABLE-DISTRIBUTION-PIPING" ;;
    003) name="WASTE-TANKS-VACUUM-INTERF" ;;
    004) name="DRAIN-MASTS-HEATERS-INTF" ;;
    005) name="GREY-WATER-RECOVERY-PATHS" ;;
    006) name="ANTIMICROBIAL-LININGS" ;;
  esac
  ci_path="CA-E1-006-WATER-WASTE-SYSTEMS/CI-CA-E1-006-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E1-007
for i in 001 002 003 004 005; do
  case $i in
    001) name="ACOUSTIC-LINERS-MODULES" ;;
    002) name="MICRO-PERF-PANELS" ;;
    003) name="TE-SERRATIONS-CHEVRONS" ;;
    004) name="BOUNDARY-LAYER-INGEST-FAIRINGS" ;;
    005) name="CONTRAIL-SUPPRESSION-GEOM" ;;
  esac
  ci_path="CA-E1-007-NOISE-EMISSIONS-CONTRAIL-MGMT/CI-CA-E1-007-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E1-008
for i in 001 002 003 004 005; do
  case $i in
    001) name="COOLING-LOOP-PLUMBING-BRACKETS" ;;
    002) name="SECONDARY-HEAT-EXCHANGERS" ;;
    003) name="RAM-AIR-DOORS-BYPASS" ;;
    004) name="HOTSPOT-INSULATION-KITS" ;;
    005) name="THERMAL-INTERFACE-MATERIALS" ;;
  esac
  ci_path="CA-E1-008-THERMAL-MANAGEMENT-NONCRYO/CI-CA-E1-008-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E1-009
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="MATERIAL-PASSPORTS-ID-MARKING" ;;
    002) name="DESIGN-FOR-DISASSEMBLY-KITS" ;;
    003) name="FASTENER-STRATEGY-RECYCLABILITY" ;;
    004) name="ADHESIVE-DEBOND-ZONES" ;;
    005) name="EOL-SORTING-SCHEMAS" ;;
    006) name="REFURBISHMENT-REPAIR-KITS" ;;
  esac
  ci_path="CA-E1-009-REMEDIATION-CIRCULARITY-LIFECYCLE/CI-CA-E1-009-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E1-010
for i in 001 002 003 004 005; do
  case $i in
    001) name="HEPA-UV-C-INTEGRATION-MOUNTS" ;;
    002) name="CO-CO2-OZONE-SENSORS-HOUSINGS" ;;
    003) name="AIRFLOW-PATTERNING-BAFFLES" ;;
    004) name="ANTIMICROBIAL-SURFACES" ;;
    005) name="ODOR-ADSORBER-MODULES" ;;
  esac
  ci_path="CA-E1-010-BIOSECURITY-AIR-QUALITY/CI-CA-E1-010-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E1-011
for i in 001 002 003 004 005; do
  case $i in
    001) name="CONDENSATE-DRAIN-NETWORKS" ;;
    002) name="INSULATION-VAPOR-BARRIERS" ;;
    003) name="ICE-PREVENTION-TRACE-INTF" ;;
    004) name="LOW-POINT-DRAINS-ACCESS" ;;
    005) name="WATER-INGRESS-SHIELDS" ;;
  esac
  ci_path="CA-E1-011-DRAINS-CONDENSATE-ICE-MGMT/CI-CA-E1-011-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E1-012
for i in 001 002 003 004 005; do
  case $i in
    001) name="SPILL-CONTAINMENT-PANS" ;;
    002) name="STORMWATER-CONTROL-CHANNELS" ;;
    003) name="DEICING-FLUID-COLLECTION" ;;
    004) name="FOAM-FIRE-SYSTEM-INTERFACES" ;;
    005) name="HAZMAT-STORAGE-BUNDING" ;;
  esac
  ci_path="CA-E1-012-GROUND-ENV-SAFETY-REMEDIATION/CI-CA-E1-012-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

echo "All CI directories created successfully for E1-ENVIRONMENTAL_REMEDIATION_CIRCULARITY."
