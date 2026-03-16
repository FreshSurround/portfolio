'''entrypoint de toda la pagina (server que "sirve"
el html o contenido de la pagina)'''

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import portfolio

app = FastAPI(
    title="Portfolio — Laura Giudici",
    description="API del portfolio personal.",
    version="1.0.0",
)

# CORS — necesario si el browser abre el HTML desde un origen distinto al servidor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Rutas de la API
app.include_router(portfolio.router)

# Archivos estáticos (JS, CSS)
#app.mount("/static", StaticFiles(directory="static"), name="static")

'''serve_frontend() es quien llama y ejectua el html, y
get_portfolio() es quien le da toda la información y contenido
para llenar la página'''
@app.get("/")
def serve_frontend():
    """Sirve el frontend React desde la raíz."""
    return FileResponse("static/index2.html")


@app.get("/api/portfolio")
async def get_portfolio():
    return {
        "name": "Lau Giudici",
        "title": "Desarrollo de software, sistemas, proyectos hardware-software y producción audiovisual.",
        "about_1": "Me dedico a la creación de soluciones informáticas para PyMES, particulares y emprendimientos locales, dentro del contexto social-económico de cada una. Mis herramientas van desde el software que administra las tareas deseadas de manera eficiente, hasta el hardware que es el puente entre el mundo real y el digital, pasando por la producción audiovisual como fuente principal de comunicación.",
        "about_2": "Me interesa comprender cómo funcionan las cosas a nivel estructural. Por eso suelo trabajar cerca del funcionamiento interno de los sistemas: comunicación entre componentes, diseño de APIs, interacción con hardware, y desarrollo de herramientas propias en lugar de depender exclusivamente de soluciones externas.",
        "skills": {
            "languages": ["Python", "C++", "C#"],
            "frameworks": ["FastAPI", ".NET / Windows Forms", "Arduino"],
            "tools": ["Git", "Linux", "SQLite y otras bases de datos ligeras", "Entornos de producción multimedia y edición"]
        },
        "projects": [
            {
                "title": "Sistema de radio controlado por software",
                "description": "Proyecto que integra hardware y software para construir un sistema de radio controlado digitalmente. El sistema utiliza un microcontrolador para interactuar con un módulo de radio FM y permite controlar la frecuencia, el volumen y otros parámetros desde una aplicación de escritorio.",
                "technologies": ["C#", "Arduino", "Comunicación serial", "Electrónica básica"],
                "role": "Diseño del sistema completo: hardware, firmware del microcontrolador y aplicación de control en PC."
            },
		{
			"title": "Proyecto dummy", "description": "Prueba1234",
			"technologies": ["techno"], "role": "no c"
		},
            {
                "title": "Servidor backend con API para gestión de datos",
                "description": "Desarrollo de un servidor backend utilizando Python y FastAPI para manejar la interacción con una base de datos local.",
                "technologies": ["Python", "FastAPI", "PostgreSQL"],
                "role": "Arquitectura del backend, desarrollo de endpoints, integración con base de datos."
            },
            {
                "title": "Prototipos electrónicos y sensores",
                "description": "Desarrollo de circuitos experimentales utilizando sensores, lógica digital y microcontroladores.",
                "technologies": ["Arduino", "Lógica digital", "Sensores eléctricos", "Electrónica básica"],
                "role": "Diseño de circuitos, prototipado y programación de control."
            }
        ]
    }
