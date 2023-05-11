from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import schemas
from database import get_db
from usecase import Package

router = APIRouter()


@router.post("/", response_model=schemas.Package)
def create_service(service: schemas.PackageCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo paquete.

    Args:
        service (schemas.PackageCreate): Datos del paquete a crear.
        db (Session, optional): Objeto de sesión de la base de datos. Defaults to Depends(get_db).

    Returns:
        schemas.Package: El paquete creado.

    Raises:
        HTTPException: Si ocurre un error al crear el paquete (código de estado 500).
    """
    db_service = Package(db).create_package(service)
    return db_service


@router.get("/", response_model=List[schemas.Package])
def read_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Obtiene una lista paginada de paquetes.

    Args:
        skip (int, optional): Cantidad de paquetes a omitir. Defaults to 0.
        limit (int, optional): Cantidad máxima de paquetes a retornar. Defaults to 100.
        db (Session, optional): Objeto de sesión de la base de datos. Defaults to Depends(get_db).

    Returns:
        List[schemas.Package]: Lista de paquetes.

    Raises:
        HTTPException: Si ocurre un error al obtener los paquetes (código de estado 500).
    """
    db_services = Package(db).get_packages()
    return db_services[skip: skip + limit]


@router.get("/{package_id}", response_model=schemas.Package)
def read_service(package_id: int, db: Session = Depends(get_db)):
    """
    Obtiene un paquete por su ID.

    Args:
        package_id (int): ID del paquete a obtener.
        db (Session, optional): Objeto de sesión de la base de datos. Defaults to Depends(get_db).

    Returns:
        schemas.Package: El paquete encontrado.

    Raises:
        HTTPException: Si el paquete no existe (código de estado 404).
    """
    db_service = Package(db).get_package(package_id=package_id)
    if db_service is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Package not found")
    return db_service
