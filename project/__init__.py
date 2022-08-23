from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

from .routers import router
from project.config import settings
from project.celery_utils import create_celery
from project.socketio_utils import create_socketio

# For offline swagger document generation
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles


def create_app() -> FastAPI:
    # Create the main FastAPI application with offline docs
    app = FastAPI(docs_url=None, redoc_url=None)
    app.mount("/static", StaticFiles(directory="static"), name="static")


    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=app.title + " - Swagger UI",
            oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui.css",
        )


    @app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect():
        return get_swagger_ui_oauth2_redirect_html()


    # Add the celery application
    app.celery_app = create_celery()


    # RESTful endpoints
    @app.get("/")
    async def root():
        return {"message": "hello world"}

    app.include_router(router)

    # Create and add the socketio server application
    socket_app = create_socketio()
    app.mount(settings.SIO_MOUNTPOINT, socket_app)

    return app