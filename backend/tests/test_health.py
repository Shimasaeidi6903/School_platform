from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "school-platform-api",
    }


def test_unknown_api_route_returns_404() -> None:
    response = client.get("/api/v1/unknown")

    assert response.status_code == 404
