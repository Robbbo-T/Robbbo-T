#!/bin/bash

cd /home/runner/work/Robbbo-T/Robbbo-T/OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/E2-ENERGY_AND_RENEWABLE

# Create CA directories if not exist
mkdir -p CA-E2-001-POWER-ARCHITECTURE
mkdir -p CA-E2-002-FUEL-CELL-POWERPLANT
mkdir -p CA-E2-003-H2-DISTRIBUTION-NONCRYO
mkdir -p CA-E2-004-POWER-CONVERSION-DISTRIBUTION
mkdir -p CA-E2-005-BATTERY-SYSTEMS
mkdir -p CA-E2-006-ENERGY-MANAGEMENT-EMS
mkdir -p CA-E2-007-THERMAL-ENERGY-RECOVERY
mkdir -p CA-E2-008-RENEWABLE-SOURCES-ONBOARD
mkdir -p CA-E2-009-ELECTRIC-PROPULSION-INTERFACES
mkdir -p CA-E2-010-GROUND-POWER-CHARGING-REFUEL
mkdir -p CA-E2-011-POWER-QUALITY-AND-HARMONICS
mkdir -p CA-E2-012-MEASUREMENT-METERING
mkdir -p CA-E2-013-SAFETY-ISOLATION-PROTECTION
mkdir -p CA-E2-014-ENERGY-SCHEDULING-OPTIMIZATION

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

# CA-E2-001
for i in 001 002 003 004 005; do
  case $i in
    001) name="BUS-TOPOLOGIES-HVDC-MVDC-LVDC" ;;
    002) name="GALLEY-AND-SERVICE-BRANCHES" ;;
    003) name="SEGREGATION-ZONES-ISOLATION" ;;
    004) name="FAULT-LEVELS-PROTECTION-COORD" ;;
    005) name="ENERGY-NOMENCLATURE-SCHEMAS" ;;
  esac
  ci_path="CA-E2-001-POWER-ARCHITECTURE/CI-CA-E2-001-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-002
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="FC-STACK-MODULE-ENVELOPES" ;;
    002) name="ANODE-CATHODE-MANIFOLDS" ;;
    003) name="HUMIDIFIERS-WATER-MGMT" ;;
    004) name="VENTS-PURGE-LINES-ROUTING" ;;
    005) name="STARTUP-SHUTDOWN-LOGIC-IFC" ;;
    006) name="FC-STACK-ISOLATION-INTERLOCKS" ;;
  esac
  ci_path="CA-E2-002-FUEL-CELL-POWERPLANT/CI-CA-E2-002-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-003
for i in 001 002 003 004 005; do
  case $i in
    001) name="REGULATORS-VALVES-ARRAYS" ;;
    002) name="MANIFOLDS-PIPING-SUPPORTS" ;;
    003) name="VENT-AND-RELIEF-PATHS" ;;
    004) name="LEAK-SEGMENTATION-TOPOLOGY" ;;
    005) name="DRIP-PANS-DRAINAGE-INTERFACES" ;;
  esac
  ci_path="CA-E2-003-H2-DISTRIBUTION-NONCRYO/CI-CA-E2-003-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-004
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="DC-DC-ISOLATED-MODULES" ;;
    002) name="DC-AC-INVERTERS-400HZ" ;;
    003) name="PDU-PRIMARY-SECONDARY" ;;
    004) name="FUSE-BREAKER-SELECTIVITY" ;;
    005) name="HVIL-HIGH-VOLT-INTERLOCK-LOOPS" ;;
    006) name="HARNESS-POWER-ROUTING" ;;
  esac
  ci_path="CA-E2-004-POWER-CONVERSION-DISTRIBUTION/CI-CA-E2-004-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-005
for i in 001 002 003 004 005; do
  case $i in
    001) name="CELL-CHEMISTRY-SELECTION" ;;
    002) name="PACK-ARCH-VENTING-PATHS" ;;
    003) name="THERMAL-RUNAWAY-CONTAINMENT" ;;
    004) name="MECHANICAL-ISOLATION-MOUNTS" ;;
    005) name="BMS-INTERFACE-REQUIREMENTS" ;;
  esac
  ci_path="CA-E2-005-BATTERY-SYSTEMS/CI-CA-E2-005-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-006
for i in 001 002 003 004 005; do
  case $i in
    001) name="POWER-BUDGETS-NOMINAL-EMER" ;;
    002) name="LOAD-SHEDDING-POLICIES" ;;
    003) name="STATE-OF-ENERGY-SOE-MODEL" ;;
    004) name="EMS-API-TO-FC-BMS-PDU" ;;
    005) name="ENERGY-AS-POLICY-RULES" ;;
  esac
  ci_path="CA-E2-006-ENERGY-MANAGEMENT-EMS/CI-CA-E2-006-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-007
for i in 001 002 003 004 005; do
  case $i in
    001) name="TEG-THERMOELECTRIC-MODULES" ;;
    002) name="HEAT-EXCHANGERS-WASTE-HEAT" ;;
    003) name="LOOPS-COOLANT-INTERFACES" ;;
    004) name="VALVING-BYPASS-STRATEGIES" ;;
    005) name="COUPLING-TO-ECS-RAM-AIR" ;;
  esac
  ci_path="CA-E2-007-THERMAL-ENERGY-RECOVERY/CI-CA-E2-007-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-008
for i in 001 002 003 004 005; do
  case $i in
    001) name="PV-AEROSKIN-TILES" ;;
    002) name="MPPT-INTERFACE-REQS" ;;
    003) name="PV-ROUTING-PROTECTION" ;;
    004) name="STRUCTURAL-INTEGRATION-GUIDES" ;;
    005) name="ENERGY-HARVESTING-VIBRATION" ;;
  esac
  ci_path="CA-E2-008-RENEWABLE-SOURCES-ONBOARD/CI-CA-E2-008-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-009
for i in 001 002 003 004 005; do
  case $i in
    001) name="MOTOR-INVERTER-POWER-IFC" ;;
    002) name="FEEDERS-AND-RETURN-PATHS" ;;
    003) name="EMI-FILTERING-POWER-SIDE" ;;
    004) name="COOLING-IFC-NONCRYO" ;;
    005) name="FAULT-CONTAINMENT-ZONES" ;;
  esac
  ci_path="CA-E2-009-ELECTRIC-PROPULSION-INTERFACES/CI-CA-E2-009-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-010
for i in 001 002 003 004 005; do
  case $i in
    001) name="GPU-400HZ-28V-INTERFACES" ;;
    002) name="DC-FAST-CHARGE-COUPLERS" ;;
    003) name="H2-REFUEL-COUPLING-NONCRYO" ;;
    004) name="INTERLOCKS-EARTH-BONDING" ;;
    005) name="GROUND-SAFETY-RUNUP-PADS" ;;
  esac
  ci_path="CA-E2-010-GROUND-POWER-CHARGING-REFUEL/CI-CA-E2-010-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-011
for i in 001 002 003 004 005; do
  case $i in
    001) name="THD-LIMITS-SPECTRA" ;;
    002) name="FILTERS-LCL-LC-SELECTION" ;;
    003) name="TRANSIENTS-RIDE-THROUGH" ;;
    004) name="INRUSH-CONTROL-PROFILES" ;;
    005) name="EMISSIONS-IMMUNITY-DO160" ;;
  esac
  ci_path="CA-E2-011-POWER-QUALITY-AND-HARMONICS/CI-CA-E2-011-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-012
for i in 001 002 003 004 005; do
  case $i in
    001) name="METERING-POINTS-PLACEMENT" ;;
    002) name="CURRENT-SHUNTS-CT-HV" ;;
    003) name="VOLTAGE-TAPS-PROTECTION" ;;
    004) name="ENERGY-ACCOUNTING-LEDGER" ;;
    005) name="DATA-QUALITY-VALIDATION" ;;
  esac
  ci_path="CA-E2-012-MEASUREMENT-METERING/CI-CA-E2-012-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-013
for i in 001 002 003 004 005; do
  case $i in
    001) name="INSULATION-RESIST-MONITORING" ;;
    002) name="ARC-FAULT-DETECTION-ZONING" ;;
    003) name="GALVANIC-ISOLATION-PATHS" ;;
    004) name="EARTHING-BONDING-REQUIREMENTS" ;;
    005) name="HAZARD-LABELS-PLACARDS" ;;
  esac
  ci_path="CA-E2-013-SAFETY-ISOLATION-PROTECTION/CI-CA-E2-013-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-E2-014
for i in 001 002 003 004 005; do
  case $i in
    001) name="MISSION-PROFILES-ENERGY-GLIDES" ;;
    002) name="COST-RISK-MODELS-CVAR" ;;
    003) name="FLEET-LEVEL-OPT-QAL-IFC" ;;
    004) name="MRO-ENERGY-IMPACT-METRICS" ;;
    005) name="CO2-POLICIES-EAP-ENFORCERS" ;;
  esac
  ci_path="CA-E2-014-ENERGY-SCHEDULING-OPTIMIZATION/CI-CA-E2-014-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

echo "All CI directories created successfully for E2-ENERGY_AND_RENEWABLE."
