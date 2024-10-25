from fastapi import APIRouter

# Create a router for health checks
router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Health check endpoint that returns the status of the application.
    Returns:
        dict: A JSON response indicating the health status.
    """
    return {"status": "healthy"}