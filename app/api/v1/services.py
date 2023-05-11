from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from typing import List

import schemas
from database import get_db
from usecase import Service

router = APIRouter()


@router.post("/", response_model=schemas.Service)
def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo servicio.

    Args:
        service (schemas.ServiceCreate): Datos del servicio a crear.
        db (Session, optional): Objeto de sesión de la base de datos. Defaults to Depends(get_db).

    Returns:
        schemas.Service: El servicio creado.

    Raises:
        HTTPException: Si ocurre un error al crear el servicio (código de estado 500).
    """
    db_service = Service(db).create_service(service)
    return db_service


@router.get("/", response_model=List[schemas.Service])
def read_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene una lista paginada de servicios.

    Args:
        skip (int, optional): Cantidad de servicios a omitir. Defaults to 0.
        limit (int, optional): Cantidad máxima de servicios a retornar. Defaults to 100.
        db (Session, optional): Objeto de sesión de la base de datos. Defaults to Depends(get_db).

    Returns:
        List[schemas.Service]: Lista de servicios.

    Raises:
        HTTPException: Si ocurre un error al obtener los servicios (código de estado 500).
    """
    db_services = Service(db).get_services()
    return db_services[skip: skip + limit]


@router.get("/{service_id}", response_model=schemas.Service)
def read_service(service_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un servicio por su ID.

    Args:
        service_id (int): ID del servicio a obtener.
        db (Session, optional): Objeto de sesión de la base de datos. Defaults to Depends(get_db).

    Returns:
        schemas.Service: El servicio encontrado.

    Raises:
        HTTPException: Si el servicio no existe (código de estado 404).
    """
    db_service = Service(db).get_service(service_id=service_id)
    if db_service is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    return db_service
