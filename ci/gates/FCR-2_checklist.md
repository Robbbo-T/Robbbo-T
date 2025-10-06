# FCR-2 Checklist: Trazabilidad QS/UTCS

## Follow-up Chain Rule 2

Este checklist verifica que la trazabilidad UTCS está completa y que el orden TFA se respeta.

## Objetivos

- Garantizar que todo cambio está trazado en UTCS
- Verificar orden canónico TFA (QS→FWD→UE→FE→CB→QB)
- Asegurar metadata completa
- Validar dependencias entre capas

## Checklist de Validación

### 1. Metadata UTCS

Todo artefacto debe incluir:

- [ ] **Context**: Contexto en el sistema global (producto, capa TFA, dominio)
- [ ] **Content**: Descripción técnica clara
- [ ] **Cache**: Referencias y dependencias documentadas
- [ ] **Structure**: Organización lógica explicada
- [ ] **Style**: Formato consistente
- [ ] **Sheet**: ID de trazabilidad, versión, autor, fecha

### 2. Orden TFA

- [ ] Identificada capa(s) TFA del PR: `QS/`, `FWD/`, `UE/`, `FE/`, `CB/`, `QB/`
- [ ] Capas anteriores están completas (no se puede hacer FE sin FWD)
- [ ] Prefijo correcto en título de PR
- [ ] Documentación de capa actualizada

### 3. Trazabilidad de Cambios

- [ ] Cada cambio técnico tiene justificación
- [ ] Referencias a análisis/simulaciones si aplica
- [ ] Links a issues/tickets relacionados
- [ ] Impacto en otras capas documentado

### 4. Dependencias

- [ ] Dependencias de capas anteriores identificadas
- [ ] Dependencias de otros módulos documentadas
- [ ] No hay dependencias circulares
- [ ] Interfaces entre capas definidas

### 5. QS (Quantum Seal)

Si el PR afecta QS:

- [ ] Requisitos actualizados
- [ ] KPIs definidos o actualizados
- [ ] Modelos de sizing actualizados (si aplica)
- [ ] Trazabilidad a casos de uso/misiones

### 6. FWD (Forward Design)

Si el PR afecta FWD:

- [ ] Diseños referencian requisitos de QS
- [ ] Geometrías/configuraciones documentadas
- [ ] Trade studies justificados
- [ ] Inputs para UE definidos

### 7. UE (User Experience)

Si el PR afecta UE:

- [ ] Factores humanos considerados
- [ ] Ergonomía documentada
- [ ] Interfaces HMI definidas
- [ ] Safety/evacuación considerado

### 8. FE (Final Engineering)

Si el PR afecta FE:

- [ ] Integración con sistemas documentada
- [ ] Interfaces eléctricas/mecánicas definidas
- [ ] Análisis térmico si aplica
- [ ] BMS/control documentado

### 9. CB (Certification Basis)

Si el PR afecta CB:

- [ ] Estándares aplicables identificados (EASA, ESA, NASA)
- [ ] Matrices de compliance actualizadas
- [ ] Safety cases referenciados
- [ ] AMC/GM documentados

### 10. QB (Quality Baseline)

Si el PR afecta QB:

- [ ] Plan de ensayos definido
- [ ] Criterios de aceptación claros
- [ ] Datos de pruebas incluidos o referenciados
- [ ] Verificación independiente considerada

## Validación Automática

El script `fcr_enforcer.py` ejecuta las siguientes validaciones:

```python
def enforce_tfa_order(pr_data):
    """Verifica orden TFA y trazabilidad UTCS"""
    # 1. Extraer capa TFA del prefijo PR
    # 2. Verificar que capas anteriores están completas
    # 3. Validar metadata UTCS en archivos modificados
    # 4. Verificar dependencias
    pass
```

## Criterios de Fallo

El gate FCR-2 **falla** si:

- Falta metadata UTCS en artefactos nuevos/modificados
- Prefijo de PR no coincide con archivos modificados
- Se intenta trabajar en capa sin completar anteriores
- Dependencias no documentadas
- Matrices de compliance no actualizadas (para CB)

## Formato UTCS en Archivos

### En Markdown
```yaml
---
utcs:
  context: "AMPEL360-T-Air / FWD / AAA"
  content: "BWB aerodynamic configuration"
  cache: "refs: QS/sizing-001, CAx/cfd-baseline"
  structure: "Section 1: Overview, Section 2: Analysis"
  style: "Technical Report Template v1.2"
  sheet:
    id: "FWD-AAA-001"
    version: "1.0"
    author: "Engineering Team"
    date: "2024-Q4"
---
```

### En Código
```python
"""
UTCS:
  context: AMPEL360-T-Air / FE / EEE
  content: Battery Management System controller
  cache: deps: numpy, scipy; refs: FWD/power-dist
  structure: Class hierarchy: BMS > CellMonitor > SafetyController
  style: PEP8, type hints
  sheet:
    id: FE-EEE-BMS-001
    version: 2.1
    author: Controls Team
    date: 2024-Q4
"""
```

## Resolución de Fallos

Si FCR-2 falla:

1. Añadir metadata UTCS faltante
2. Corregir prefijo de PR si es incorrecto
3. Completar capas TFA anteriores o justificar excepción
4. Documentar dependencias
5. Actualizar matrices de compliance
6. Re-ejecutar validación localmente

## Comando de Validación Local

```bash
python ci/gates/fcr_enforcer.py --pr-title "FWD/update-bwb-geometry" --files-changed "products/ampel360-t-air/FWD/**"
```

## Excepciones

Solo con aprobación de governance:
- Saltar capas TFA (requiere RFC)
- Work in progress sin UTCS completo (marcar PR como Draft)
- Cross-layer changes (documentar en descripción PR)

---

**Versión**: 1.0  
**Enforcement**: Automático vía CI  
**Override**: Solo con aprobación governance
