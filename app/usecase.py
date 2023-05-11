from sqlalchemy.orm import Session

import models
import schemas


# Craamos el usecase de service
class Service:
    def __init__(self, db: Session):
        self.db = db

    def get_service(self, service_id: int):
        return self.db.query(models.Service).filter(models.Service.id == service_id).first()

    def get_services(self):
        return self.db.query(models.Service).all()

    def create_service(self, service: schemas.ServiceCreate):
        db_service = models.Service(name=service.name)
        self.db.add(db_service)
        self.db.commit()
        self.db.refresh(db_service)
        return db_service


# Craamos el usecase de package
class Package:
    def __init__(self, db: Session):
        self.db = db

    def create_package(self, package: schemas.PackageCreate):
        db_deliverables = [
            models.Deliverable(name=deliverable.name)
            for deliverable in package.deliverables
        ]
        db_package = models.Package(
            description=package.description,
            price=package.price,
            type_of_service_id=package.type_of_service_id,
            deliverables=db_deliverables,
        )
        self.db.add(db_package)
        self.db.commit()
        self.db.refresh(db_package)
        return db_package

    def get_package(self, package_id: int):
        return self.db.query(models.Package).filter(models.Package.id == package_id).first()

    def get_packages(self):
        return self.db.query(models.Package).all()


# Creamos el usecase de Deliverable
class Deliverable:
    def __init__(self, db: Session):
        self.db = db

    def create_deliverable(self, deliverable: schemas.DeliverableCreate):
        db_deliverable = models.Deliverable(name=deliverable.name)
        self.db.add(db_deliverable)
        self.db.commit()
        self.db.refresh(db_deliverable)
        return db_deliverable

    def get_deliverable(self, deliverable_id: int):
        return self.db.query(models.Deliverable).filter(models.Deliverable.id == deliverable_id).first()

    def get_deliverables(self):
        return self.db.query(models.Deliverable).all()
