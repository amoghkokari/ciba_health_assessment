from fastapi import FastAPI
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.generate_response import router as generate_response_router

# Initialize FastAPI application
app = FastAPI()

# Include routers for different endpoints
app.include_router(health_router)
app.include_router(generate_response_router)
