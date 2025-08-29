#!/bin/bash

cd /workspaces/Robbbo-T/OPTIME-FRAMEWORK/T-TECHNOLOGICAL/AMEDEO-PELLICCIA/INTEGRATED/AMPEL360-H2-BWB-QNNN/M-MECHANICAL_AND_CONTROL

# Create CA directories if not exist
mkdir -p CA-M-001-FLIGHT-CONTROL-MECHANISMS
mkdir -p CA-M-002-ACTUATION-TECHNOLOGIES
mkdir -p CA-M-003-HYDRAULIC-POWER-DISTRIBUTION
mkdir -p CA-M-004-LANDING-GEAR-SYSTEM
mkdir -p CA-M-005-BRAKE-AND-STEERING-CONTROL
mkdir -p CA-M-006-DOORS-HATCHES-RAMPS-MECHANISMS
mkdir -p CA-M-007-SYSTEMS-MOUNTS-AND-BRACKETS
mkdir -p CA-M-008-PNEUMATIC-MECHANISMS
mkdir -p CA-M-009-SURVIVABILITY-AND-LOAD-PATH-SAFEGUARDS
mkdir -p CA-M-010-MECHANICAL-SERVO-LOOPS-HW
mkdir -p CA-M-011-MAINTENANCE-AND-GSE-INTERFACES
mkdir -p CA-M-012-CROSS-DOMAIN-INTERFACES

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

# CA-M-001
for i in 001 002 003 004 005 006 007 008; do
  case $i in
    001) name="FC-ELEVON-HINGE-LINES" ;;
    002) name="FC-FLAPERON-DRIVE-BOXES" ;;
    003) name="FC-SPOILER-DRIVE-UNITS" ;;
    004) name="FC-TORQUE-TUBES-AND-GEARTRAINS" ;;
    005) name="FC-BALANCE-MASSES" ;;
    006) name="FC-SURFACE-MECHANICAL-LOCKS" ;;
    007) name="FC-OVERCENTER-FAILSAFE-LINKS" ;;
    008) name="FC-LVDT-RVDT-MOUNT-KITS" ;;
  esac
  ci_path="CA-M-001-FLIGHT-CONTROL-MECHANISMS/CI-CA-M-001-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-M-002
for i in 001 002 003 004 005 006 007 008; do
  case $i in
    001) name="ACT-HYDRAULIC-SERVOVALVES" ;;
    002) name="ACT-EHA-MODULES" ;;
    003) name="ACT-EMA-ACTUATORS" ;;
    004) name="ACT-POWER-DRIVE-UNITS-PDU" ;;
    005) name="ACT-REDUNDANCY-MECHANISMS" ;;
    006) name="ACT-JAM-TOLERANCE-DEVICES" ;;
    007) name="ACT-BACKDRIVE-LOCKS" ;;
    008) name="ACT-HEALTH-MONITOR-MOUNTS" ;;
  esac
  ci_path="CA-M-002-ACTUATION-TECHNOLOGIES/CI-CA-M-002-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-M-003
for i in 001 002 003 004 005 006 007 008 009; do
  case $i in
    001) name="HYD-RESERVOIRS" ;;
    002) name="HYD-ENGINE-DRIVEN-PUMPS" ;;
    003) name="HYD-ELECTRIC-PUMPS" ;;
    004) name="HYD-ACCUMULATORS" ;;
    005) name="HYD-MANIFOLDS-BLOCKS" ;;
    006) name="HYD-FILTERS-STRainers" ;;
    007) name="HYD-RETURN-LINES" ;;
    008) name="HYD-OIL-COOLERS" ;;
    009) name="HYD-ISOLATION-VALVE-BRACKETS" ;;
  esac
  ci_path="CA-M-003-HYDRAULIC-POWER-DISTRIBUTION/CI-CA-M-003-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-M-004
for i in 001 002 003 004 005 006 007 008 009 010; do
  case $i in
    001) name="LG-NOSE-GEAR-ASSEMBLY" ;;
    002) name="LG-MAIN-GEAR-ASSEMBLY" ;;
    003) name="LG-RETRACTION-ACTUATORS" ;;
    004) name="LG-UPLOCKS-DOWNLOCKS" ;;
    005) name="LG-DOOR-MECHANISMS" ;;
    006) name="LG-SHOCK-STRUTS" ;;
    007) name="LG-WHEELS-TIRES" ;;
    008) name="LG-NOSE-WHEEL-STEERING-MECH" ;;
    009) name="LG-STRUCTURAL-BAYS" ;;
    010) name="LG-MECHANICAL-INDICATORS" ;;
  esac
  ci_path="CA-M-004-LANDING-GEAR-SYSTEM/CI-CA-M-004-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-M-005
for i in 001 002 003 004 005 006 007 008; do
  case $i in
    001) name="BRK-BRAKE-STACKS" ;;
    002) name="BRK-BRAKE-ACTUATORS" ;;
    003) name="BRK-ANTISKID-VALVE-BLOCKS" ;;
    004) name="BRK-PARKING-BRAKE-UNIT" ;;
    005) name="BRK-ALTERNATE-BRAKE-PATH" ;;
    006) name="NWS-GEARBOX" ;;
    007) name="NWS-TILLER-LINKAGE" ;;
    008) name="BRK-TORQUE-METERS" ;;
  esac
  ci_path="CA-M-005-BRAKE-AND-STEERING-CONTROL/CI-CA-M-005-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-M-006
for i in 001 002 003 004 005 006; do
  case $i in
    001) name="DRS-KINEMATICS-HINGE-ARMS" ;;
    002) name="DRS-UPLOCK-HOOKS" ;;
    003) name="DRS-LATCHES-SEALS" ;;
    004) name="DRS-DRIVE-LINKAGES" ;;
    005) name="DRS-EMERGENCY-JETTISON" ;;
    006) name="DRS-MAINT-ACCESS-PANELS" ;;
  esac
  ci_path="CA-M-006-DOORS-HATCHES-RAMPS-MECHANISMS/CI-CA-M-006-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-M-007
for i in 001 002 003 004 005 006 007; do
  case $i in
    001) name="SYS-AVIONICS-RACKS" ;;
    002) name="SYS-H2-VALVE-SUPPORTS" ;;
    003) name="SYS-PIPE-CLAMPS-P-CLIPS" ;;
    004) name="SYS-CABLE-TRAYS" ;;
    005) name="SYS-SENSOR-BRACKETS" ;;
    006) name="SYS-VIBRATION-ISOLATORS" ;;
    007) name="SYS-RADIATOR-MOUNTS" ;;
  esac
  ci_path="CA-M-007-SYSTEMS-MOUNTS-AND-BRACKETS/CI-CA-M-007-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-M-008
for i in 001 002 003 004 005; do
  case $i in
    001) name="PNM-BLEED-VALVE-MECH" ;;
    002) name="PNM-PRESSURE-REG-PRVs" ;;
    003) name="PNM-DUCT-COUPLINGS" ;;
    004) name="PNM-CHECK-VALVE-HOUSINGS" ;;
    005) name="PNM-ISOLATION-LEVERAGES" ;;
  esac
  ci_path="CA-M-008-PNEUMATIC-MECHANISMS/CI-CA-M-008-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-M-009
for i in 001 002 003 004 005; do
  case $i in
    001) name="SRV-CRASH-LOAD-PATH-DEVICES" ;;
    002) name="SRV-SHEAR-PINS-FUSES" ;;
    003) name="SRV-FUSELAGE-CRUSH-ZONES" ;;
    004) name="SRV-DITCHING-FITTINGS" ;;
    005) name="SRV-FIRE-HARDENED-PASS-THROUGHS" ;;
  esac
  ci_path="CA-M-009-SURVIVABILITY-AND-LOAD-PATH-SAFEGUARDS/CI-CA-M-009-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-M-010
for i in 001 002 003 004 005; do
  case $i in
    001) name="SERVO-FEEDBACK-LVDT-MOUNTS" ;;
    002) name="SERVO-RATE-LIMITERS-MECH" ;;
    003) name="SERVO-MECHANICAL-STOPS" ;;
    004) name="SERVO-BACKUP-MANUAL-REVERSION" ;;
    005) name="SERVO-CABLE-PULLEY-LEGACY-INTF" ;;
  esac
  ci_path="CA-M-010-MECHANICAL-SERVO-LOOPS-HW/CI-CA-M-010-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-M-011
for i in 001 002 003 004 005; do
  case $i in
    001) name="MNT-QUICK-RELEASE-FITTINGS" ;;
    002) name="MNT-SAFEING-PINS-STREAMERS" ;;
    003) name="MNT-JACK-POINTS" ;;
    004) name="MNT-TIE-DOWN-POINTS" ;;
    005) name="MNT-CRADLES-LIFTING-FIXTURES" ;;
  esac
  ci_path="CA-M-011-MAINTENANCE-AND-GSE-INTERFACES/CI-CA-M-011-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

# CA-M-012
for i in 001 002 003 004 005; do
  case $i in
    001) name="XD-TO-E2-H2-VALVES-ACTUATION-MECH" ;;
    002) name="XD-TO-E3-SENSOR-PACKAGING" ;;
    003) name="XD-TO-A-AERODYNAMIC-SURFACE-INTF" ;;
    004) name="XD-TO-C1-CABIN-CARGO-HARDPOINTS" ;;
    005) name="XD-TO-O-OPERATING-SAFE-MODES" ;;
  esac
  ci_path="CA-M-012-CROSS-DOMAIN-INTERFACES/CI-CA-M-012-$i-$name"
  mkdir -p "$ci_path"
  create_lifecycle_folders "$ci_path"
done

echo "All CI directories created successfully for M-MECHANICAL_AND_CONTROL."
