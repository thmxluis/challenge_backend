from typing import List

from pydantic import BaseModel


class DeliverableBase(BaseModel):
    name: str


class DeliverableCreate(DeliverableBase):
    pass


class Deliverable(DeliverableBase):
    id: int
    
    class Config:
        orm_mode = True


class PackageBase(BaseModel):
    description: str
    price: int
    type_of_service_id: int


class PackageCreate(PackageBase):
    deliverables: List[DeliverableCreate]


class Package(PackageBase):
    id: int
    deliverables: List[Deliverable] = []

    class Config:
        orm_mode = True


class ServiceBase(BaseModel):
    name: str


class ServiceCreate(ServiceBase):
    pass


class Service(ServiceBase):
    id: int
    packages: List[Package] = []

    class Config:
        orm_mode = True
