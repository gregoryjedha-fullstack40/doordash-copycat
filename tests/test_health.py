import pytest
import httpx

def test_health():
    response = httpx.get("http://localhost:8090/status/")
    assert response.status_code == 200
    assert response.json() == {"status":"Service is up and running"}

