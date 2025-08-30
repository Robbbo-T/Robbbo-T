# CA-C1-31-10: Cockpit HMI H2 QCB Status

Component Area: CA-C1-31-10-COCKPIT-HMI-H2-QCB-STATUS

## Description
Human Machine Interface systems for monitoring and controlling hydrogen (H₂) and quantum computing board (QCB) status in the cockpit. Provides integrated display systems for cryogenic status, leak detection, quantum processing status, and emergency shutdown controls.

## Impacts
- **E3-31-96** (IO interfaces)
- **O-42-90** (AQUA-OS /cryo/status services)
- **O-45-70** (Digital Evidence Twin)
- **O-46-50** (EFB checklists)

## Artifacts
- Spec HMI + EICAS/ECAM pages
- ICD signals/alerts
- DO-178C (DAL level per FHA)
- V&V Plan HMI
- OM/QRH documentation
- EFB integration

## Testing
- DO-160 EMI/lightning (sections 20/21) for displays/EDS
- Human factors testing per CS-25.1322
- Functional testing of alert systems

## Contents

### Subfolders

- **[CI-CA-C1-31-10-01-H2-STATUS-DISPLAYS](./CI-CA-C1-31-10-01-H2-STATUS-DISPLAYS/)** - Component Implementation: CI-CA-C1-31-10-01-H2-STATUS-DISPLAYS
- **[CI-CA-C1-31-10-02-QCB-STATUS-MONITORING](./CI-CA-C1-31-10-02-QCB-STATUS-MONITORING/)** - Component Implementation: CI-CA-C1-31-10-02-QCB-STATUS-MONITORING
- **[CI-CA-C1-31-10-03-INTEGRATED-ALERT-SYSTEM](./CI-CA-C1-31-10-03-INTEGRATED-ALERT-SYSTEM/)** - Component Implementation: CI-CA-C1-31-10-03-INTEGRATED-ALERT-SYSTEM
- **[CI-CA-C1-31-10-04-EMERGENCY-SHUTDOWN-CONTROLS](./CI-CA-C1-31-10-04-EMERGENCY-SHUTDOWN-CONTROLS/)** - Component Implementation: CI-CA-C1-31-10-04-EMERGENCY-SHUTDOWN-CONTROLS

---

**[← Back to C1-COCKPIT_CABIN_CARGO_SYSTEMS](../)**