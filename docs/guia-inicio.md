# Guía de Inicio Rápido

Bienvenido a la guía de inicio rápido del proyecto GAIA AIR Memories. Esta guía te ayudará a comenzar a utilizar el proyecto de manera rápida y sencilla.

## Instalación y Configuración

Sigue estos pasos para instalar y configurar el proyecto:

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

## Uso Básico

Aquí tienes algunos ejemplos básicos de cómo utilizar el proyecto:

### Ejemplo 1: Crear un nuevo recuerdo

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

### Ejemplo 2: Obtener todos los recuerdos

```javascript
api.obtenerRecuerdos()
  .then(response => {
    console.log("Lista de recuerdos:", response.data);
  })
  .catch(error => {
    console.error("Error al obtener los recuerdos:", error);
  });
```

### Ejemplo 3: Actualizar un recuerdo existente

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

### Ejemplo 4: Eliminar un recuerdo

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

## Documentación Adicional

Para más detalles sobre cómo utilizar el proyecto, consulta la [documentación completa](./index.md).

¡Esperamos que disfrutes utilizando el proyecto GAIA AIR Memories!
