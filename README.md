# QuickU - Módulo de Administración de Ofertas (Matchmaking) 🚀

🌍 **Acceso a Producción (Live Demo):** [Panel Administrativo QuickU](https://sevenmo-semestre-tarea-8-administraci-n.onrender.com/admin-promos/)

Este repositorio contiene la implementación del panel administrativo para **QuickU**, un ecosistema universitario enfocado en la economía circular y el delivery interno. Este módulo específico está diseñado para que los locales gestionen las "Ofertas Predictivas" que alimentan directamente el motor de emparejamiento (Matchmaking) de la plataforma.

El desarrollo se rige por principios sólidos de Ingeniería de Software, aplicando el patrón arquitectónico **MVC (Modelo-Vista-Controlador)** mediante el framework Django, garantizando la seguridad de los datos a nivel de servidor y optimizando la interfaz mediante técnicas modernas de accesibilidad web.

---
## 🚀 Tecnologías Utilizadas

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)
[![Sass](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)](https://sass-lang.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://developer.mozilla.org/es/docs/Web/JavaScript)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/)

---

## 🏗️ Arquitectura y Patrones de Diseño

### 1. Modelo-Vista-Controlador (MVC)
- **Modelo (`models.py`):** Define la capa de persistencia de datos (`Local`, `Producto`, `Promocion`) y centraliza las restricciones críticas del dominio del problema.
- **Vista (`templates/`):** Interfaces de usuario renderizadas del lado del servidor, separando la presentación de la lógica de negocio.
- **Controlador (`views.py`):** Actúa como orquestador, procesando peticiones HTTP, coordinando las validaciones de datos y determinando las respuestas adecuadas (redirecciones o endpoints JSON).

### 2. Integridad y Validación Back-End (Protección del Core)
Para asegurar que el algoritmo de *Scoring de Match* de QuickU no procese datos anómalos que puedan alterar el modelo de negocio, se implementaron validaciones estrictas a nivel de servidor:
- **Restricciones de Negocio:** El controlador bloquea la persistencia en la base de datos si detecta incongruencias lógicas temporales (ej. *Hora de Inicio* posterior a la *Hora de Fin*) o si los parámetros de descuento exceden los márgenes permitidos.
- **Flujo de Excepciones:** Los errores detectados durante el método `clean()` son capturados y enviados de vuelta a la vista a través del contexto, asegurando que la validación principal no dependa jamás del lado del cliente.

---

## 🎨 UI/UX y Tecnologías Front-End

### Arquitectura Front-End Estrictamente Semántica
La interfaz fue construida aplicando principios de accesibilidad web extrema. **En lugar de recurrir a contenedores genéricos carentes de significado estructural para maquetar el DOM, el diseño se apoya exclusivamente en el uso riguroso de etiquetas HTML5 puramente semánticas** (`<main>`, `<section>`, `<header>`, `<fieldset>`, `<legend>`, `<output>`, etc.). Esto genera un árbol DOM altamente predecible, accesible para lectores de pantalla y optimizado.

### Estilos Modulares (SCSS/BEM)
- **Metodología BEM:** Se adoptó la convención *Block__Element--Modifier* para aislar componentes, evitar la colisión de clases y asegurar la mantenibilidad del código a escala.
- **Preprocesamiento Sass:** El diseño visual moderno (tipo dashboard, con *focus rings* accesibles y comportamiento dinámico de tarjetas) se gestiona mediante un archivo `.scss`, lo que permite el uso de variables de paletas de color, anidamiento y transformaciones compiladas a CSS nativo.

### Peticiones Asíncronas y Dinamismo (AJAX)
La selección de inventario se gestiona mediante un flujo asíncrono implementado con **Vanilla JavaScript (Fetch API)**. Al seleccionar un local universitario, el cliente interroga al servidor en segundo plano; el controlador en Django procesa la solicitud mediante un endpoint dedicado y retorna un payload ligero en formato `JSON`, actualizando el DOM en tiempo real sin necesidad de recargar el contexto completo.

---

## 💻 Stack Tecnológico
- **Back-End:** Python 3.1x, Django 5.x
- **Front-End:** HTML5 Semántico, SCSS, JavaScript Vainilla
- **Base de Datos:** SQLite3 (Desarrollo local y Producción mediante persistencia simulada con Fixtures en Render).
- **Infraestructura:** Despliegue continuo gestionado con Gunicorn y automatización de procesos (`build.sh`).

---

# ⚙️ Guía de Instalación Local

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

---

## 1. Clonar el repositorio

```bash
git clone https://github.com/JuanAntamba/7mo-Semestre_Tarea-8-Administraci-n-MVC.git

cd 7mo-Semestre_Tarea-8-Administraci-n-MVC
```

---

## 2. Crear y activar el entorno virtual

### En Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### En Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Aplicar migraciones y cargar datos iniciales

```bash
python manage.py migrate

python manage.py loaddata initial_data.json
```

El archivo `initial_data.json` carga datos de prueba necesarios para el funcionamiento inicial del sistema AJAX entre locales y productos.

---

## 5. Ejecutar el servidor local

```bash
python manage.py runserver
```

El sistema estará disponible en:

```text
http://127.0.0.1:8000/admin-promos/
```

---

# 🚀 Despliegue en Producción

La aplicación fue desplegada en Render utilizando:
- Gunicorn como servidor WSGI.
- PostgreSQL como base de datos principal.
- Automatización de build mediante `build.sh`.

🌐 Producción:  
https://sevenmo-semestre-tarea-8-administraci-n.onrender.com/admin-promos/

---

# 👨‍💻 Autor

**Juan Carlos Antamba**  
Ingeniería en Software — Universidad de las Américas

Proyecto desarrollado como aplicación práctica de Arquitectura MVC e Ingeniería Web para 7mo Semestre.