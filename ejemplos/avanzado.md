# Ejemplo Avanzado de Uso del Proyecto GAIA AIR Memories

Este documento proporciona un ejemplo avanzado de cómo utilizar el proyecto GAIA AIR Memories. Incluye fragmentos de código y explicaciones detalladas para ayudarte a comprender y aprovechar al máximo las funcionalidades avanzadas del proyecto.

## Crear un Recuerdo con Metadatos

El siguiente ejemplo muestra cómo crear un nuevo recuerdo con metadatos adicionales utilizando la API del proyecto:

```javascript
const nuevoRecuerdo = {
  titulo: "Mi primer vuelo en GAIA AIR",
  descripcion: "Recuerdo detallado de mi primer vuelo en el proyecto GAIA AIR.",
  fecha: "2025-01-01",
  metadatos: {
    ubicacion: "Madrid, España",
    tipo: "Vuelo",
    etiquetas: ["primer vuelo", "GAIA AIR", "experiencia"]
  }
};

api.crearRecuerdo(nuevoRecuerdo)
  .then(response => {
    console.log("Recuerdo creado con metadatos:", response.data);
  })
  .catch(error => {
    console.error("Error al crear el recuerdo con metadatos:", error);
  });
```

## Buscar Recuerdos por Etiquetas

El siguiente ejemplo muestra cómo buscar recuerdos utilizando etiquetas específicas:

```javascript
const etiquetasBusqueda = ["GAIA AIR", "experiencia"];

api.buscarRecuerdosPorEtiquetas(etiquetasBusqueda)
  .then(response => {
    console.log("Recuerdos encontrados:", response.data);
  })
  .catch(error => {
    console.error("Error al buscar recuerdos por etiquetas:", error);
  });
```

## Actualizar Metadatos de un Recuerdo

El siguiente ejemplo muestra cómo actualizar los metadatos de un recuerdo existente:

```javascript
const idRecuerdo = "12345";
const metadatosActualizados = {
  ubicacion: "Barcelona, España",
  tipo: "Vuelo Actualizado",
  etiquetas: ["vuelo actualizado", "GAIA AIR", "nueva experiencia"]
};

api.actualizarMetadatosRecuerdo(idRecuerdo, metadatosActualizados)
  .then(response => {
    console.log("Metadatos del recuerdo actualizados:", response.data);
  })
  .catch(error => {
    console.error("Error al actualizar los metadatos del recuerdo:", error);
  });
```

## Eliminar un Recuerdo por ID

El siguiente ejemplo muestra cómo eliminar un recuerdo utilizando su ID:

```javascript
const idRecuerdo = "12345";

api.eliminarRecuerdoPorID(idRecuerdo)
  .then(response => {
    console.log("Recuerdo eliminado por ID:", response.data);
  })
  .catch(error => {
    console.error("Error al eliminar el recuerdo por ID:", error);
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
