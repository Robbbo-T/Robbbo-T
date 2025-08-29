# Mos Tri-Modal Kernel - Gaia Air-Rtos

Generated from AQUA-BRIDGE-OS v22.0 Specification

---


## 4.1 Diseño de Microkernel y Particionamiento (ARINC 653)
Principio: Núcleo mínimo verificable, servicios en espacio de usuario, y particiones temporales y espaciales estrictas para garantizar el aislamiento y la seguridad requeridos por DAL-A.

* **Major Frame:** Un ciclo de tiempo global (configurable, ej. 50 ms) que se divide en minor frames. Cada partición ARINC 653 tiene asignadas ventanas de ejecución precomputadas y fijas dentro de la tabla de tiempo del planificador, asegurando un comportamiento temporal predecible.
* **Aislamiento Espacial:** Se implementa mediante el uso de la MMU (Memory Management Unit) y MPU (Memory Protection Unit) del hardware para crear dominios de memoria completamente aislados.

## 4.2 Planificador HTS (Determinismo Híbrido)
**XAI:** Permitir la coexistencia segura de tareas de control crítico (hard-RT) y análisis/optimización flexible (no-RT) en la ACT. El HTS (Hybrid Task Scheduler) garantiza que las tareas críticas se ejecuten sin jitter ni interrupciones, incluso bajo carga computacional variable.

## 4.6 Voter 2oo3 y Sincronización
Flujo de consenso: dispatch paralelo → barrera de sincronización → comparación bit-a-bit → decisión mayoritaria.
                

---

*This content is part of the AQUA-BRIDGE-OS v22.0 technical specification and is organized according to the aerospace lifecycle methodology.*
