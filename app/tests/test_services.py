import pytest
from fastapi import status
from sqlalchemy.orm import Session
from json import dumps

from database import get_db
from schemas import PackageCreate, Package
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
    response = app.post_json("/v1/packages/", content=dumps(package_data))
    assert response.status_code == status.HTTP_200_OK
    created_package = response.json()
    assert created_package["description"] == package_data["description"]
    assert created_package["price"] == package_data["price"]
    assert created_package["type_of_service_id"] == package_data["type_of_service_id"]


def test_read_services(test_db: Session):
    # Obtener la lista de servicios
    response = app.get("/", dependencies={'db': test_db})
    assert response.status_code == status.HTTP_200_OK
    services = response.json()
    assert isinstance(services, list)


def test_read_service(test_db: Session):
    # Obtener un servicio específico
    service_id = 1
    response = app.get(f"/{service_id}", dependencies={'db': test_db})
    assert response.status_code == status.HTTP_200_OK
    service = response.json()
    assert isinstance(service, dict)
    assert "id" in service
    assert "name" in service


def test_read_service_not_found(test_db: Session):
    # Intentar obtener un servicio que no existe
    service_id = 999
    response = app.get(f"/{service_id}", dependencies={'db': test_db})
    assert response.status_code == status.HTTP_404_NOT_FOUND
