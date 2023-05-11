from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import schemas
from database import get_db
from usecase import Package

router = APIRouter(
    prefix="/packages",
    tags=["Packages"],
    responses={404: {"description": "Not found"}},
)


# Crear un paquete
@router.post("/", response_model=schemas.Package)
def create_package(package: schemas.PackageCreate, db: Session = Depends(get_db)):
    try:
        db_package = Package(db).create_package(package)
        return db_package
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        


# @router.post("/", response_model=schemas.Service)
# def create_service(service: schemas.ServiceCreate, db: Session = Depends(get_db)):
#     try:
#         db_service = Package(db).create_service(service)
#         return db_service
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# @router.get("/", response_model=List[schemas.Service])
# def read_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     try:
#         db_services = Service(db).get_services()
#         return db_services[skip : skip + limit]
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# @router.get("/{service_id}", response_model=schemas.Service)
# def read_service(service_id: int, db: Session = Depends(get_db)):
#     try:
#         db_service = Service(db).get_service(service_id=service_id)
#         if db_service is None:
#             raise HTTPException(
#                 status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
#         return db_service
#     except Exception as e:
#         raise HTTPException(
            # status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
