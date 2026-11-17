def test_health_returns_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_health_only_accepts_get(client):
    response = client.post("/health")

    assert response.status_code == 405
