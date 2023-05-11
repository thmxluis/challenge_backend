from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    packages = relationship("Package", back_populates="service")


class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    price = Column(Integer)
    type_of_service_id = Column(Integer, ForeignKey("services.id"))

    service = relationship("Service", back_populates="packages")
    deliverables = relationship("Deliverable", back_populates="package")


class Deliverable(Base):
    __tablename__ = "deliverables"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    package_id = Column(Integer, ForeignKey("packages.id"))

    package = relationship("Package", back_populates="deliverables")

