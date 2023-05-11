import pytest
from fastapi import status
from sqlalchemy.orm import Session

from database import get_db
from main import app


@pytest.fixture
def test_db():
    # Configurar y retornar la base de datos de prueba
    db = get_db()
    try:
        yield db
    finally:
        db.close()


def test_create_package(test_db: Session):
    # Crear un paquete de prueba
    package_data = {
        "description": "Paquete de prueba",
        "price": 100,
        "type_of_service_id": 1
    }
    response = app.post("/v1/packages/", json=package_data)
    assert response.status_code == status.HTTP_200_OK
    created_package = response.json()
    assert created_package["description"] == package_data["description"]
    assert created_package["price"] == package_data["price"]
    assert created_package["type_of_service_id"] == package_data["type_of_service_id"]


def test_read_services(test_db: Session):
    # Obtener la lista de paquetes
    response = app.get("/v1/packages/")
    assert response.status_code == status.HTTP_200_OK
    packages = response.json()
    assert isinstance(packages, list)


def test_read_service(test_db: Session):
    # Obtener un paquete específico
    response = app.get("/v1/packages/1")
    assert response.status_code == status.HTTP_200_OK
    package = response.json()
    assert isinstance(package, dict)
    assert "id" in package
    assert "description" in package
    assert "price" in package
    assert "type_of_service_id" in package


def test_read_service_not_found(test_db: Session):
    # Intentar obtener un paquete que no existe
    response = app.get("/v1/packages/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
