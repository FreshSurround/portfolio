from typing import TypedDict


class Area(TypedDict):
    id: str
    title: str
    description: str
    icon: str


class Project(TypedDict):
    id: str
    number: str
    title: str
    description: str
    role: str
    tags: list[str]


class ProcessStep(TypedDict):
    step: str
    label: str
    description: str


class ContactLink(TypedDict):
    label: str
    href: str


OWNER = {
    "name": "Laura Giudici",
    "title": "Desarrollo de software, sistemas y proyectos hardware-software",
    "bio": (
        "Desarrolladora con interés en la construcción de sistemas completos: "
        "desde el software que los controla hasta el hardware con el que interactúan. "
        "Trabajo principalmente en backend, herramientas de software y proyectos donde "
        "se integran programación, electrónica y automatización."
    ),
    "bio_extra": (
        "Me interesa comprender cómo funcionan las cosas a nivel estructural. "
        "Por eso suelo trabajar cerca del funcionamiento interno de los sistemas: "
        "comunicación entre componentes, diseño de APIs, interacción con hardware, "
        "y desarrollo de herramientas propias."
    ),
}

TECHS: list[str] = [
    "Python", "C++", "C#", "FastAPI", ".NET",
    "Arduino", "Git", "Linux", "SQLite",
]

AREAS: list[Area] = [
    {
        "id": "software",
        "title": "Desarrollo de software",
        "description": (
            "Aplicaciones y herramientas orientadas a resolver problemas técnicos concretos. "
            "Trabajo principalmente con Python, C++ y C#."
        ),
        "icon": "◈",
    },
    {
        "id": "backend",
        "title": "Backend y APIs",
        "description": (
            "Diseño de servicios backend y APIs para manejar datos, automatizar procesos "
            "y conectar distintos componentes. FastAPI y bases de datos locales o remotas."
        ),
        "icon": "⬡",
    },
    {
        "id": "embedded",
        "title": "Electrónica y embebidos",
        "description": (
            "Proyectos que integran microcontroladores, sensores y hardware externo con software. "
            "Arduino para construir prototipos funcionales y sistemas experimentales."
        ),
        "icon": "◎",
    },
    {
        "id": "creative",
        "title": "Herramientas creativas",
        "description": (
            "Proyectos que combinan tecnología con audio, video o interfaces experimentales. "
            "Flujos de trabajo técnicos para producción y manipulación de medios digitales."
        ),
        "icon": "◐",
    },
]

PROJECTS: list[Project] = [
    {
        "id": "radio",
        "number": "01",
        "title": "Sistema de radio controlado por software",
        "description": (
            "Proyecto que integra hardware y software para construir un sistema de radio "
            "controlado digitalmente. El sistema utiliza un microcontrolador para interactuar "
            "con un módulo de radio FM y permite controlar la frecuencia, el volumen y otros "
            "parámetros desde una aplicación de escritorio con interfaz analógica interactiva."
        ),
        "role": "Diseño del sistema completo: hardware, firmware del microcontrolador y app de control en PC.",
        "tags": ["C#", "Arduino", "Serial", "Hardware"],
    },
    {
        "id": "backend-api",
        "number": "02",
        "title": "Servidor backend con API para gestión de datos",
        "description": (
            "Desarrollo de un servidor backend utilizando Python y FastAPI para manejar la "
            "interacción con una base de datos local. El sistema estructura datos, expone "
            "endpoints y facilita la construcción de aplicaciones con una capa de backend "
            "simple pero flexible. Separación clara entre lógica, routers y base de datos."
        ),
        "role": "Arquitectura del backend, desarrollo de endpoints, integración con base de datos.",
        "tags": ["Python", "FastAPI", "SQLite"],
    },
    {
        "id": "electronics",
        "number": "03",
        "title": "Prototipos electrónicos y sensores",
        "description": (
            "Desarrollo de circuitos experimentales utilizando sensores, lógica digital y "
            "microcontroladores. Estos proyectos exploran distintas formas de medir variables "
            "físicas y procesarlas mediante lógica digital o software. Combinan componentes "
            "discretos, circuitos integrados y microcontroladores."
        ),
        "role": "Diseño de circuitos, prototipado y programación de control.",
        "tags": ["Arduino", "Lógica digital", "Sensores", "Electrónica"],
    },
]

OTHER_PROJECTS: list[dict] = [
    {
        "title": "Herramientas de automatización en Python",
        "description": "Scripts y utilidades para automatizar tareas de desarrollo, manipulación de datos y pruebas.",
    },
    {
        "title": "Exploración de estructuras de software",
        "description": "Proyectos experimentales para entender cómo funcionan internamente ciertos tipos de software.",
    },
    {
        "title": "Producción audiovisual independiente",
        "description": "Participación en proyectos audiovisuales experimentales donde se combinan narrativa y tecnología.",
    },
]

PROCESS: list[ProcessStep] = [
    {"step": "01", "label": "Análisis", "description": "Comprender el problema antes de elegir herramientas o tecnologías."},
    {"step": "02", "label": "Arquitectura", "description": "Diseño de la estructura general del sistema."},
    {"step": "03", "label": "Desarrollo", "description": "Iteración sobre los componentes del sistema."},
    {"step": "04", "label": "Integración", "description": "Conexión entre hardware y software cuando aplica."},
    {"step": "05", "label": "Refinamiento", "description": "Pruebas, depuración y simplificación del sistema."},
]

CONTACT: list[ContactLink] = [
    {"label": "GitHub", "href": "https://github.com"},
    {"label": "Email", "href": "mailto:laura@example.com"},
    {"label": "LinkedIn", "href": "#"},
]

INTERESTS: list[str] = [
    "diseño de sistemas de software",
    "interacción hardware-software",
    "herramientas de backend y automatización",
    "programación cercana al sistema",
    "tecnología aplicada a proyectos creativos",
]
