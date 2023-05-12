import pytest
from fastapi import status
from sqlalchemy.orm import Session
from starlette.testclient import TestClient

from database import get_db, engine
from main import app
from schemas import ServiceCreate

client = TestClient(app)


@pytest.fixture(scope="function")
def db_session():
    # Crear la sesión de la base de datos
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()


def test_create_service(db_session: Session):
    # Crear un servicio de prueba
    service_data = ServiceCreate(name="Test Service")
    response = client.post("/v1/services/", json=service_data.dict())

    # Verificar el código de respuesta y los datos del servicio creado
    assert response.status_code == 200
    created_service = response.json()
    assert created_service["name"] == service_data.name


def test_read_services(db_session: Session):
    # Obtener la lista de servicios
    response = client.get("/v1/services/")
    assert response.status_code == status.HTTP_200_OK
    services = response.json()
    assert isinstance(services, list)


def test_read_service(db_session: Session):
    # Obtener un servicio específico
    response = client.get("/v1/services/1")
    assert response.status_code == status.HTTP_200_OK
    service = response.json()
    assert isinstance(service, dict)
    assert "id" in service
    assert "name" in service


def test_read_service_not_found(db_session: Session):
    # Intentar obtener un servicio que no existe
    response = client.get("/v1/services/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND


# Configuración para usar el db_session en todos los tests
@pytest.fixture(autouse=True)
def override_get_db(db_session):
    def override():
        return db_session
    app.dependency_overrides[get_db] = override
