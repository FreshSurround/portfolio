'''entrypoint de toda la pagina (server que "sirve"
el html o contenido de la pagina)'''

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import portfolio

app = FastAPI(
    title="Portfolio — Lau Giudici",
    description="API del portfolio personal.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(portfolio.router)

'''app.mount() es quien monta y ejectua el html junto con
sus dependencias, y get_portfolio() es quien sube toda la
información y contenido para llenar la página en
api/portfolio, de donde se alimenta index.html'''
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/api/portfolio")
async def get_portfolio():
    return {
        "name": "Neon Informatica",
        "title": "Desarrollo de software, sistemas, proyectos hardware-software y producción audiovisual.",
        "about_1": "Me dedico a la creación de soluciones informáticas para PyMES, particulares y emprendimientos locales, dentro del contexto social-económico de cada una. Específicamente me dedico a actualizar y/o crear nuevos sistemas de gestión admnistrativa. Mis herramientas van desde el software que administra las tareas deseadas de manera eficiente, hasta el hardware que es el puente entre el mundo real y el digital, pasando por la producción audiovisual como fuente principal de comunicación.",
        "about_2": "Me interesa comprender cómo funcionan las cosas a nivel estructural. Por eso suelo trabajar cerca del funcionamiento interno de los sistemas: comunicación entre componentes, diseño de APIs, interacción con hardware, y desarrollo de herramientas propias en lugar de depender exclusivamente de soluciones externas.",
        "skills": {
            "languages": ["Python", "Javascript", "HTML", "C++"],
            "frameworks": ["FastAPI", ".NET / Windows Forms", "React.js"],
            "tools": ["Git", "Linux", "PostgreSQL", "Entornos de producción multimedia y edición"]
        },
        "projects": [
		{
			"title": "Solarformes (En Desarrollo)",
			"description": "Aplicación web que integra, muestra y exporta en distintos formatos (PDF, csv...) información referente a la sustentabilidad, desarrollo y ecología de distintos países del mundo.",
			"technologies": ["Python", "FastAPI", "React.js", "HTML", "Git"],
			"role": ""
		},
		{
                "title": "Sistema de Control Automatizado de Líquidos",
                "description": "Proyecto que utiliza lógica binaria y secuencial para automatizar el control de un tanque de líquidos, incluyendo la activacion/desactivación de la bomba de agua, un display 7-Segmento que indica el nivel del agua, un display de línea que muestra la temperatura del agua y un sistema de alarma para evitar que se sobrellene el tanque.",
                "technologies": ["Lógica binaria", "Lógica secuencial", "Integrados TTL y CMOS", "Sistemas de Control"],
                "role": ""
            },
            {
                "title": "Portfolio",
                "description": "El actual portfolio para mostrar proyectos personales, freelance y diversa información.",
                "technologies": ["Python", "FastAPI", "React.js"],
                "role": ""
            },
            {
                "title": "Prototipos electrónicos y sensores",
                "description": "Desarrollo de circuitos experimentales utilizando sensores, lógica digital y microcontroladores.",
                "technologies": ["Arduino/ESP32", "Lógica digital", "Sensores eléctricos", "Electrónica avanzada"],
                "role": ""
            }
        ]
    }
