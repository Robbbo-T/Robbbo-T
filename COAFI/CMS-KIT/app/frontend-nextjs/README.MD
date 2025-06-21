# COAFI Frontend (Next.js)

**Estado:** 🧪 En desarrollo  
**Stack:** Next.js · TypeScript · TailwindCSS · shadcn/ui · Zustand · REST/Federated APIs  

---

## 🌐 Descripción

Este módulo proporciona la interfaz de usuario para **COAFI CMS-KIT**, orientada a la gestión de contenidos, nodos federados y agentes AI en entornos aeroespaciales.

Diseñado como una interfaz adaptativa, ofrece una experiencia UI/UX centrada en:

- **Gestión de usuarios y permisos**
- **Monitorización de nodos y agentes federados**
- **Configuración de "Widget Moods" y contextos de orquestación**
- **Interacción con tokens descentralizados (GaiaToken)**
- **Visualización de telemetría y auditoría ética**

---

## 📁 Estructura (prevista)

```
frontend-nextjs/
├── app/                # Rutas Next.js (pages router)
│   ├── dashboard/      # Vista principal (admin panel, overview de nodos)
│   ├── auth/           # Login, registro, recuperación
│   └── settings/       # Configuración de usuario y orquestación
│
├── components/         # Componentes reutilizables (cards, forms, mood-panels)
├── lib/                # Hooks, stores y utilidades globales
├── services/           # Llamadas a API (FastAPI backend + endpoints federados)
├── styles/             # Tailwind y estilos globales
└── public/             # Imágenes, iconos, etc.
```

---

## 🧠 Funciones destacadas (roadmap)

- [ ] Autenticación federada con JWT/OAuth2
- [ ] Switch dinámico entre "Widget Moods" (configuración UI basada en estado AI)
- [ ] Dashboard para administración de nodos y usuarios
- [ ] Integración visual con agentes AI
- [ ] Monitor de auditoría y telemetría
- [ ] WebSockets para eventos en tiempo real
- [ ] Multilenguaje + modo accesibilidad

---

## 🚀 Scripts

```bash
pnpm install        # Instala dependencias
pnpm dev            # Corre el entorno de desarrollo (http://localhost:3000)
pnpm build          # Compila para producción
```

---

## 📦 Dependencias clave

- `next` – Framework React fullstack
- `tailwindcss` – Utilidades de estilo
- `shadcn/ui` – Componentes de interfaz personalizables
- `axios` – Cliente HTTP
- `zustand` – Estado global reactivo
- `clsx` – Composición condicional de clases

---

## 🔐 Seguridad

El frontend no almacena datos sensibles localmente. Todo el flujo de autenticación utiliza tokens de acceso firmados (JWT), y está previsto soporte para **tokens descentralizados (DID + ZK Proofs)** a través de GaiaToken.

---

## 🛰️ Modo federado

El panel está diseñado para interactuar con nodos descentralizados. Cada nodo puede tener su propio endpoint backend, y la UI se adaptará dinámicamente mediante auto-descubrimiento y handshake federado.

---

## 🧬 Enlace con GAIA-AIR

En futuras versiones, este frontend funcionará como **panel de control ético y operativo** del sistema GAIA-AIR, permitiendo:

- Asignación y control de agentes AI por misión
- Visualización de decisiones autónomas con trazabilidad ética
- Intervención humana directa sobre el flujo de contexto/memoria

---

## 📄 Licencia

MIT © Robbbo-T · COAFI Project
```

---
