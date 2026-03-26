# Portfolio — Laura Giudici

Stack: **FastAPI** (backend) + **React 18 via CDN** (frontend, sin build step).

## Estructura

```
portfolio/
├── main.py               # Entry point FastAPI — sirve la API y los archivos estáticos
├── data.py               # Todo el contenido del portfolio (proyectos, áreas, etc.)
├── requirements.txt
├── routers/
│   ├── __init__.py
│   └── portfolio.py      # Endpoints /api/*
└── static/
    ├── index.html        # HTML principal, carga React via CDN
    ├── style.css         # Estilos
    ├── components.js     # Componentes React reutilizables
    └── app.js            # Componente raíz, llama a la API y monta la app
```

## Instalación y uso

If you want to see it without any installation on your local computer, you can visit the [portfolio itself](https://neon-informatica.onrender.com/static/)

```bash
# 1. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate      # Linux/Mac
# venv\Scripts\activate       # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Iniciar el servidor
fastapi dev main.py
```

Abrir en el navegador: **http://localhost:8000**

Documentación automática de la API: **http://localhost:8000/docs**

## Endpoints disponibles

| Método | Ruta             | Descripción                              |
|--------|------------------|------------------------------------------|
| GET    | `/api/all`       | Todo el contenido en una sola llamada    |
| GET    | `/api/info`      | Datos del owner + tecnologías            |
| GET    | `/api/areas`     | Áreas de trabajo                         |
| GET    | `/api/projects`  | Proyectos destacados y secundarios       |
| GET    | `/api/process`   | Pasos del proceso de trabajo             |
| GET    | `/api/contact`   | Links de contacto                        |

## Editar el contenido

Todo el contenido está en `data.py`. Editarlo no requiere tocar HTML ni JS.
