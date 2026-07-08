import pytest
import httpx

def test_fee_calculation():
    payload = {"distance_km": 5, "weight_kg": 10}
    response = httpx.post("http://localhost:8090/calculate-fee/", json=payload)
    assert response.status_code == 200
    assert "delivery_fee" in response.text
    assert "17.5" in response.text
