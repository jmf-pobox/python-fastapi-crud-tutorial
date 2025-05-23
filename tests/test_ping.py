from fastapi.testclient import TestClient


def test_ping(test_app: TestClient) -> None:
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
