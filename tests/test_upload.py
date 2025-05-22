# tests/test_upload.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_sem_token():
    response = client.post("/upload/", files={"file": ("test.txt", b"Hello world")})
    assert response.status_code == 401

def test_login_e_upload():
    login = client.post("/token", data={"username": "admin", "password": "admin"})
    assert login.status_code == 200
    token = login.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/upload/", files={"file": ("test.txt", b"Hello world")}, headers=headers)
    assert response.status_code == 200
    assert "filename" in response.json()