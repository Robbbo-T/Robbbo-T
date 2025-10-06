# ASI-T · Universal Injection Prompt (v1)

## Propósito

Este documento define el **Universal Injection Prompt** que actúa como SSoT (Single Source of Truth) para todas las acciones de agentes y humanos en el proyecto ROBBBO-T.

## Core Principles

### 1. SSoT (Single Source of Truth)

Toda acción debe referenciar documentos canon:
- `GENESIS_ASI-T2.md` para principios fundamentales
- `CANON_FACTS.md` para hechos inmutables
- Esta guía para procedimientos operacionales

### 2. TFA Flow Compliance

Toda contribución debe identificar su capa TFA:

```
QS → FWD → UE → FE → CB → QB
```

**Antes de iniciar trabajo**:
1. Identificar en qué capa(s) TFA se trabaja
2. Verificar dependencias de capas anteriores
3. Asegurar que UTCS está actualizado para capas previas

### 3. UTCS Threading

Todo artefacto debe incluir metadata UTCS:

```yaml
utcs:
  context: "[Dónde encaja en el sistema]"
  content: "[Descripción técnica]"
  cache: "[Referencias y dependencias]"
  structure: "[Organización]"
  style: "[Formato]"
  sheet: "[Trazabilidad ID, versión, autor, fecha]"
```

### 4. MAL-EEM Checklist

Antes de cualquier submission (PR, documento, diseño):

- [ ] **Ética**: ¿Es ético este desarrollo? ¿Hay consideraciones morales?
- [ ] **Empatía**: ¿Impacta a personas? ¿Consideramos su perspectiva?
- [ ] **Meaning**: ¿Tiene sentido en el contexto del proyecto? ¿Agrega valor real?

## Procedimientos Operacionales

### Para Agentes AI

Al recibir una tarea:

1. **Identificar contexto**:
   - ¿En qué producto(s) impacta? (Air, Space, ambos)
   - ¿En qué capa(s) TFA? (QS, FWD, UE, FE, CB, QB)
   - ¿En qué dominio(s)? (AAA…PPP)

2. **Verificar dependencias**:
   - Revisar capas TFA anteriores
   - Verificar documentación de dominio
   - Consultar UTCS para trazabilidad

3. **Aplicar MAL-EEM**:
   - Completar checklist ético
   - Documentar consideraciones
   - Justificar decisiones

4. **Actualizar trazabilidad**:
   - Incluir metadata UTCS
   - Linkear a documentos canon
   - Actualizar matrices de compliance si aplica

5. **Validation gates**:
   - Correr FCR-1 (paths/inputs válidos)
   - Correr FCR-2 (trazabilidad UTCS)
   - Verificar links con `link_path_validator.py`

### Para Humanos

Al contribuir al proyecto:

1. **Leer documentos canon**:
   - `GENESIS_ASI-T2.md`
   - `CANON_FACTS.md`
   - Esta guía

2. **Seguir convenciones PR**:
   - Usar prefijos por capa: `QS/`, `FWD/`, `UE/`, `FE/`, `CB/`, `QB/`
   - Ejemplo: `QS/update-h2-sizing-model`

3. **Documentar decisiones**:
   - Incluir justificación técnica
   - Referenciar análisis o simulaciones
   - Linkear a issues/tickets

4. **Respetar orden canónico**:
   - No saltar capas TFA sin justificación
   - Asegurar que trabajo anterior está completo
   - Actualizar documentación de dependencias

## Validation Checklist

Antes de submit (PR, design review, documento):

- [ ] Identificada capa(s) TFA afectada(s)
- [ ] Verificadas dependencias de capas anteriores
- [ ] Completado checklist MAL-EEM
- [ ] Incluida metadata UTCS
- [ ] Enlaces verificados (no broken links)
- [ ] Documentación actualizada
- [ ] Tests/validation apropiados
- [ ] Prefijo correcto en PR title
- [ ] Matrices de compliance actualizadas (si aplica CB)

## Enforcement

Los CI gates automáticos verifican:

1. **FCR-1**: Validación de paths e inputs
2. **FCR-2**: Trazabilidad UTCS completa
3. **Link validator**: Todos los links funcionan
4. **Naming conventions**: Prefijos correctos
5. **MAL-EEM**: Checklist presente y completo

**Fallo en cualquier gate = PR bloqueado automáticamente**

## Excepciones

Solo en casos excepcionales y con aprobación de governance:
- Saltar capas TFA (requiere justificación documentada)
- Modificar documentos canon (requiere RFC formal)
- Bypass de CI gates (solo con override manual justificado)

## Contacto y Governance

Para dudas sobre interpretación o excepciones:
- Abrir issue con label `governance`
- Referenciar este documento
- Incluir contexto completo y justificación

---

**Versión**: 1.0  
**Estado**: ACTIVE - Universal Injection Prompt  
**Scope**: Todos los agentes y humanos  
**Última actualización**: 2024
