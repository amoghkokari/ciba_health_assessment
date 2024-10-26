import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_health_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

@pytest.mark.asyncio
async def test_generate_response_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/generate-response",
            json={"clause": "What are the insurance requirements for health coverage?"}
        )
    assert response.status_code == 200
    assert "response" in response.json()
