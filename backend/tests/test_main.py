from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_ws_risk():
    with client.websocket_connect("/ws/risk") as websocket:
        data = websocket.receive_text()
        assert data == "risk_stream_connected"
