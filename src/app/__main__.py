import logging

import uvicorn
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.infrastructure.persistence.config import Config
from app.interface.routes import answers, questions
from app.ioc import AppProvider

config = Config()
container = make_async_container(AppProvider(), context={Config: config})


def get_fastapi_app() -> FastAPI:
    app = FastAPI()
    setup_dishka(container, app)
    app.include_router(questions.router)
    app.include_router(answers.router)
    return app


if __name__ == "__main__":
    uvicorn.run(get_fastapi_app(), host="0.0.0.0", port=8000)
