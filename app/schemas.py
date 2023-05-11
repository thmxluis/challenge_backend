from typing import List, Optional
from pydantic import BaseModel


class DeliverableBase(BaseModel):
    id: Optional[int]
    name: str


class DeliverableCreate(DeliverableBase):
    pass


class Deliverable(DeliverableBase):
    class Config:
        orm_mode = True


class PackageBase(BaseModel):
    id: Optional[int]
    description: str
    price: int
    type_of_service_id: int


class PackageCreate(PackageBase):

    deliverables: List[DeliverableCreate]

    class Config:
        orm_mode = True
        schema_extra = {

            "default": {
                "description": "Descripcion del package",
                "price": 0,
                "type_of_service_id": 0,
                "deliverables": [
                    {
                        "name": "Nombre del deliverable"
                    }
                ]
            }
        }


class Package(PackageBase):

    deliverables: List[Deliverable] = []

    class Config:
        orm_mode = True


class ServiceBase(BaseModel):
    id: Optional[int]
    name: str


class ServiceCreate(ServiceBase):
    class Config:
        schema_extra = {

            "references": {
                "id": "ID del service",
                "name": "Nombre del service",
                "packages": "Lista de packages asociados al service"
            },
            "required": ["name"],
            "type": "object",
            "title": "Service",
            "description": "Service model Create",
            "default": {
                    "name": "Tipo de servicio"
            }
        }


class Service(ServiceBase):
    packages: List[Package] = []  # Lista de packages asociados al service

    class Config:
        orm_mode = True
