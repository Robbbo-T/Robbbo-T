# Ejemplo Básico de Uso del Proyecto GAIA AIR Memories

Este documento proporciona un ejemplo básico de cómo utilizar el proyecto GAIA AIR Memories. Incluye fragmentos de código y explicaciones para ayudarte a comenzar.

## Crear un Nuevo Recuerdo

El siguiente ejemplo muestra cómo crear un nuevo recuerdo utilizando la API del proyecto:

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

## Obtener Todos los Recuerdos

El siguiente ejemplo muestra cómo obtener todos los recuerdos almacenados:

```javascript
api.obtenerRecuerdos()
  .then(response => {
    console.log("Lista de recuerdos:", response.data);
  })
  .catch(error => {
    console.error("Error al obtener los recuerdos:", error);
  });
```

## Actualizar un Recuerdo Existente

El siguiente ejemplo muestra cómo actualizar un recuerdo existente:

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

## Eliminar un Recuerdo

El siguiente ejemplo muestra cómo eliminar un recuerdo:

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

## Instrucciones para Ejecutar el Ejemplo

1. Clona el repositorio:

```bash
git clone https://github.com/Robbbo-T/gaia-air-memories-project.git
cd gaia-air-memories-project
```

2. Instala las dependencias:

```bash
npm install
```

3. Configura las variables de entorno:

Copia el archivo `.env.example` a `.env` y edítalo con tus valores de configuración.

```bash
cp .env.example .env
nano .env
```

4. Inicia el proyecto:

```bash
npm start
```

5. Ejecuta los ejemplos de código proporcionados en este documento para interactuar con la API del proyecto GAIA AIR Memories.
