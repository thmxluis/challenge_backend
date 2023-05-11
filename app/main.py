from fastapi import FastAPI

from api.router import api_router
from database import Base, engine


def create_app():
    Base.metadata.create_all(bind=engine)
    app = FastAPI()
    app.include_router(api_router)
    return app


app = create_app()

