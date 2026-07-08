import pytest
import httpx

def test_root():
    response = httpx.get("http://localhost:8090/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

