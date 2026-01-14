from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="REST API - Exercício EBAC")

app.include_router(router)
