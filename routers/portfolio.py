"""
routers/portfolio.py — Endpoints del portfolio.

Todos los endpoints devuelven JSON con el contenido
definido en data.py. Separar routers de main.py permite
agregar nuevas secciones sin tocar el entry point.
"""

from fastapi import APIRouter
from data import (
    OWNER, TECHS, AREAS, PROJECTS,
    OTHER_PROJECTS, PROCESS, CONTACT, INTERESTS,
)

router = APIRouter(prefix="/api", tags=["portfolio"])


@router.get("/info")
def get_info():
    """Información general: nombre, título, bio y tecnologías."""
    return {
        "owner": OWNER,
        "techs": TECHS,
        "interests": INTERESTS,
    }


@router.get("/areas")
def get_areas():
    """Áreas de trabajo."""
    return {"areas": AREAS}


@router.get("/projects")
def get_projects():
    """Proyectos destacados y proyectos secundarios."""
    return {
        "featured": PROJECTS,
        "other": OTHER_PROJECTS,
    }


@router.get("/process")
def get_process():
    """Pasos del proceso de trabajo."""
    return {"steps": PROCESS}


@router.get("/contact")
def get_contact():
    """Links de contacto."""
    return {"links": CONTACT}


@router.get("/all")
def get_all():
    """Todo el contenido en una sola llamada (útil para la carga inicial)."""
    return {
        "owner": OWNER,
        "techs": TECHS,
        "interests": INTERESTS,
        "areas": AREAS,
        "projects": {
            "featured": PROJECTS,
            "other": OTHER_PROJECTS,
        },
        "process": PROCESS,
        "contact": CONTACT,
    }
