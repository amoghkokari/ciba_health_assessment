from fastapi import FastAPI
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.generate_response import router as generate_response_router

# Initialize FastAPI application
fast_app = FastAPI()

# Include routers for different endpoints
fast_app.include_router(health_router)
fast_app.include_router(generate_response_router)
