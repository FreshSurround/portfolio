"""
Endpoints del portfolio.
"""

from fastapi import APIRouter
from data import (
    OWNER, TECHS, AREAS, PROJECTS,
    OTHER_PROJECTS, PROCESS, CONTACT, INTERESTS,
)

router = APIRouter(prefix="/api", tags=["portfolio"])


@router.get("/info")
def get_info():
    return {
        "owner": OWNER,
        "techs": TECHS,
        "interests": INTERESTS,
    }


@router.get("/areas")
def get_areas():
    return {"areas": AREAS}


@router.get("/projects")
def get_projects():
    return {
        "featured": PROJECTS,
        "other": OTHER_PROJECTS,
    }


@router.get("/process")
def get_process():
    return {"steps": PROCESS}


@router.get("/contact")
def get_contact():
    return {"links": CONTACT}


@router.get("/all")
def get_all():
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
