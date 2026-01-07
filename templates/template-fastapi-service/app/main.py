"""FastAPI application entry point."""

from fastapi import FastAPI
from app.routes import router
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    description="A FastAPI service template",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the API", "docs": "/docs"}


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "debug": settings.debug
    }
