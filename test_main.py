
from fastapi.testclient import TestClient
from main import app, add_numbers

client = TestClient(app)


def test_add_numbers():
    assert add_numbers(10, 20) == 30


def test_add_negative_numbers():
    assert add_numbers(-5, -10) == -15


def test_addition_api():
    response = client.post(
        "/add",
        json={"num1": 10, "num2": 20}
    )

    assert response.status_code == 200
    assert response.json()["addition"] == 30


def test_addition_with_decimal():
    response = client.post(
        "/add",
        json={"num1": 5.5, "num2": 2.5}
    )

    assert response.status_code == 200
    assert response.json()["addition"] == 8.0


def test_invalid_input():
    response = client.post(
        "/add",
        json={"num1": "hello", "num2": 20}
    )

    assert response.status_code == 422
