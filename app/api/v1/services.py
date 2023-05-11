from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import schemas
from database import get_db
from usecase import Service

router = APIRouter(
    prefix="/services",
    tags=["Services"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=schemas.Service)
def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
    try:
        db_service = Service(db).create_service(service)
        return db_service
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/", response_model=List[schemas.Service])
def read_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        db_services = Service(db).get_services()
        return db_services[skip : skip + limit]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/{service_id}", response_model=schemas.Service)
def read_service(service_id: int, db: Session = Depends(get_db)):
    try:
        db_service = Service(db).get_service(service_id=service_id)
        if db_service is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
        return db_service
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# @router.post("/", status_code=status.HTTP_201_CREATED)
# def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
#     db_service = crud.create_service(db, service)
#     return db_service


# @router.get("/", response_model=List[schemas.Service])
# def read_services(skip: int = 0, limit: int = 100, db: Session = Depends(SessionLocal)):
#     services = crud.get_services(db)
#     return services


# @router.get("/{service_id}", response_model=schemas.Service)
# def read_service(service_id: int, db: Session = Depends(SessionLocal)):
#     db_service = crud.get_service(db, service_id=service_id)
#     if db_service is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
#     return db_service


# @router.post("/{service_id}/packages/", response_model=schemas.Package)
# def create_package_for_service(
#     service_id: int, package: schemas.PackageCreate, db: Session = Depends(SessionLocal)
# ):
#     return crud.create_package(db=db, package=package)


# @router.get("/{service_id}/packages/", response_model=List[schemas.Package])
# def read_packages_for_service(
#     service_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(SessionLocal)
# ):
#     packages = crud.get_packages_by_service(db, service_id=service_id, skip=skip, limit=limit)
#     return packages


# @router.get("/{service_id}/packages/{package_id}", response_model=schemas.Package)
# def read_package_for_service(
#     service_id: int, package_id: int, db: Session = Depends(SessionLocal)
# ):
#     db_package = crud.get_package(db, package_id=package_id)
#     if db_package is None or db_package.type_of_service_id != service_id:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Package not found")
#     return db_package
