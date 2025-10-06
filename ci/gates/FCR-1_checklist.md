# FCR-1 Checklist: Validación de Inputs y Paths

## Follow-up Chain Rule 1

Este checklist verifica que todos los inputs y paths son válidos antes de merge.

## Objetivos

- Garantizar que todos los archivos referenciados existen
- Verificar que los paths son correctos y accesibles
- Asegurar que no hay enlaces rotos
- Validar estructura de directorios según canon

## Checklist de Validación

### 1. Paths de Archivos

- [ ] Todos los archivos referenciados en el PR existen
- [ ] Los paths son absolutos o relativos correctos
- [ ] No hay referencias a archivos fuera del repositorio
- [ ] Los nombres de archivo siguen convenciones (lowercase, guiones, no espacios)

### 2. Enlaces en Markdown

- [ ] Todos los enlaces internos apuntan a archivos/directorios existentes
- [ ] Los enlaces relativos están correctamente formados
- [ ] No hay enlaces rotos (#404)
- [ ] Los anchors en enlaces (`#section`) existen en el documento destino

### 3. Estructura de Directorios

- [ ] Los directorios siguen la estructura canon definida en README
- [ ] Las capas TFA están en el orden correcto: `QS/`, `FWD/`, `UE/`, `FE/`, `CB/`, `QB/`
- [ ] Los productos están bajo `products/`
- [ ] Los dominios están bajo `domains/`

### 4. Referencias a Recursos Externos

- [ ] URLs externas son válidas (si es posible verificar)
- [ ] Recursos externos están documentados
- [ ] No hay credenciales hardcoded en paths

### 5. Imports y Dependencias

- [ ] Imports de código referencian módulos existentes
- [ ] Dependencias están declaradas en archivos de configuración
- [ ] No hay dependencias circulares

## Validación Automática

El script `link_path_validator.py` ejecuta las siguientes validaciones:

```python
def validate_paths(pr_files):
    """Valida todos los paths en los archivos del PR"""
    # 1. Verificar existencia de archivos
    # 2. Validar enlaces en markdown
    # 3. Comprobar estructura de directorios
    # 4. Verificar imports en código
    pass
```

## Criterios de Fallo

El gate FCR-1 **falla** si:

- Cualquier archivo referenciado no existe
- Hay enlaces rotos en documentación
- La estructura de directorios viola el canon
- Hay paths con caracteres inválidos o espacios
- Referencias a archivos sensibles (`.env`, credenciales, etc.)

## Resolución de Fallos

Si FCR-1 falla:

1. Revisar el output del validador para identificar problemas
2. Corregir paths rotos o archivos faltantes
3. Actualizar enlaces a sus destinos correctos
4. Verificar estructura de directorios
5. Re-ejecutar validación localmente antes de push

## Comando de Validación Local

```bash
python ci/gates/link_path_validator.py --check-all
```

## Excepciones

Solo con aprobación de governance:
- Paths temporales (documentar en PR)
- Enlaces a recursos aún no creados (crear issue de tracking)
- Estructura experimental (requiere RFC)

---

**Versión**: 1.0  
**Enforcement**: Automático vía CI  
**Override**: Solo con aprobación governance
