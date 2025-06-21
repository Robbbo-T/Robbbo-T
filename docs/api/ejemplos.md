# Ejemplos de Uso de la API

Esta sección proporciona ejemplos de cómo utilizar la API del proyecto GAIA AIR Memories. Los ejemplos incluyen fragmentos de código para casos de uso comunes y explicaciones detalladas.

## Ejemplo 1: Crear un nuevo recuerdo

```javascript
const nuevoRecuerdo = {
  titulo: "Mi primer vuelo",
  descripcion: "Recuerdo de mi primer vuelo en el proyecto GAIA AIR.",
  fecha: "2025-01-01"
};

api.crearRecuerdo(nuevoRecuerdo)
  .then(response => {
    console.log("Recuerdo creado:", response.data);
  })
  .catch(error => {
    console.error("Error al crear el recuerdo:", error);
  });
```

## Ejemplo 2: Obtener todos los recuerdos

```javascript
api.obtenerRecuerdos()
  .then(response => {
    console.log("Lista de recuerdos:", response.data);
  })
  .catch(error => {
    console.error("Error al obtener los recuerdos:", error);
  });
```

## Ejemplo 3: Actualizar un recuerdo existente

```javascript
const idRecuerdo = "12345";
const datosActualizados = {
  titulo: "Mi primer vuelo actualizado",
  descripcion: "Actualización del recuerdo de mi primer vuelo.",
  fecha: "2025-01-02"
};

api.actualizarRecuerdo(idRecuerdo, datosActualizados)
  .then(response => {
    console.log("Recuerdo actualizado:", response.data);
  })
  .catch(error => {
    console.error("Error al actualizar el recuerdo:", error);
  });
```

## Ejemplo 4: Eliminar un recuerdo

```javascript
const idRecuerdo = "12345";

api.eliminarRecuerdo(idRecuerdo)
  .then(response => {
    console.log("Recuerdo eliminado:", response.data);
  })
  .catch(error => {
    console.error("Error al eliminar el recuerdo:", error);
  });
```
