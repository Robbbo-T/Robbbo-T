# Data

This directory indexes datasets used across the ROBBBO-T project.

---

## Purpose

Central index for all data resources:
- Reference data (atmospheric models, material properties)
- Historical data (existing aircraft/spacecraft performance)
- Market data (demand, routes, passenger profiles)
- Environmental data (weather, emissions factors)

Large datasets stored externally, indexed here with UTCS metadata.

---

## Categories

### Reference Data
- Atmospheric models (ISA, US Standard Atmosphere)
- Material properties (composites, metals, cryogenic materials)
- Component performance maps (fuel cells, batteries, motors)
- Standards databases (EASA, ESA, NASA requirements)

### Market Data
- Air routes and demand (passenger volumes, frequencies)
- Airport infrastructure (runway lengths, H₂ availability)
- Spaceport locations and capabilities
- Competitive benchmarks (existing aircraft/spacecraft)

### Environmental Data
- Weather patterns (temperature, wind, precipitation)
- H₂ production pathways (well-to-wake emissions)
- Grid carbon intensity (regional electricity mix)
- Noise regulations (airport-specific limits)

### Operational Data
- Flight profiles (typical missions, climb/cruise/descent)
- Turnaround operations (refueling, cleaning, boarding)
- Maintenance schedules (inspection intervals, MTBUR)
- Safety statistics (incident rates, hazard probabilities)

---

## File Naming Convention

```
<category>-<subcategory>-<source>-<version>.<ext>

Examples:
  reference-atmosphere-isa-1976.csv
  market-air-routes-eu-2024.xlsx
  environment-h2-production-pathways-2024.json
  operational-flight-profiles-regional-baseline.mat
```

---

## Dataset Entry Template

```markdown
### Dataset: European Air Routes and Demand (2024)
- **Category**: Market data
- **Subcategory**: Air routes
- **Source**: Eurostat, OAG
- **Version**: 2024-Q3
- **Date**: 2024-09-30
- **Format**: Excel (.xlsx)
- **Size**: 25 MB
- **Description**: 
  Passenger volumes and frequencies for European air routes (<3000 km).
  Includes city pairs, annual passengers, flight frequency, typical aircraft.
- **Columns**: 
  - origin_city, destination_city, distance_km, passengers_annual, flights_annual, 
    aircraft_type, load_factor
- **Location**: `s3://robbbo-t-data/market/air-routes-eu-2024.xlsx`
- **Usage**: 
  - QS: Market sizing for AMPEL360-T-Air
  - Route selection and demand modeling
- **UTCS**:
  ```yaml
  utcs:
    context: "Data / Market / Air Routes"
    content: "European air route demand 2024"
    cache: "refs: /products/ampel360-t-air/QS/"
    structure: "Tabular (Excel)"
    style: "Dataset"
    sheet:
      id: "DATA-MARKET-AIR-001"
      version: "2024-Q3"
      date: "2024-09-30"
  ```
```

---

## UTCS Indexing

All datasets must include UTCS metadata for traceability:
- **Context**: Where in the system is this used?
- **Content**: What data does it contain?
- **Cache**: What depends on this data?
- **Structure**: Format and organization
- **Style**: Data schema and units
- **Sheet**: Version, provenance, date

---

## Data Sources

### Open Data
- Eurostat (EU statistics)
- NASA (atmospheric models, space data)
- NOAA (weather, climate)
- ICAO (aviation standards)

### Commercial
- OAG (flight schedules)
- Cirium (fleet data)
- IHS Markit (market analysis)

### Proprietary
- Internal testing (QOx)
- Simulations (sim/)
- CAx analyses (cax/)

---

## Data Quality

All datasets should be:
- ✅ **Verified**: Source credibility checked
- ✅ **Validated**: Values checked for reasonableness
- ✅ **Versioned**: Changes tracked over time
- ✅ **Documented**: Metadata complete (UTCS)
- ✅ **Accessible**: Location and access documented

---

## Storage

### Small files (< 10 MB)
- Can be committed directly to repo (if not sensitive)
- Use Git LFS for binary formats

### Large files (> 10 MB)
- Store externally (S3, institutional storage)
- Index here with metadata and access instructions

### Sensitive data
- Never commit credentials or PII
- Document access control in `/governance/COMPLIANCE/`

---

**Version**: 1.0  
**Last Updated**: 2024-Q4
