from fastapi import FastAPI
from app.routes.github import router

app = FastAPI(title="GitHub Connector API")

app.include_router(router, prefix="/github")


@app.get("/")
def root():
    return {"message": "GitHub Connector is running"}