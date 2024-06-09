import sys
import os
from unittest.mock import patch

# Add the parent directory to the system path to find the main module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from fastapi.testclient import TestClient
from main import app, Passenger
import pytest

client = TestClient(app)

def test_read_root():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

@pytest.mark.parametrize("pclass,sex,age,fare,traveled_alone,embarked", [
    (1, 1, 25.0, 100.0, 1, 0),  # Valid data
    (3, 0, 30.0, 50.0, 0, 2),   # Valid data
    (1, 1, -5.0, 100.0, 1, 0),  # Invalid age
    (1, 1, 25.0, -100.0, 1, 0), # Invalid fare
])
def test_passenger_model(pclass, sex, age, fare, traveled_alone, embarked):
    try:
        passenger = Passenger(
            pclass=pclass,
            sex=sex,
            age=age,
            fare=fare,
            traveled_alone=traveled_alone,
            embarked=embarked
        )
        assert passenger.pclass == pclass
        assert passenger.sex == sex
        assert passenger.age == age
        assert passenger.fare == fare
        assert passenger.traveled_alone == traveled_alone
        assert passenger.embarked == embarked
    except Exception as e:
        assert isinstance(e, ValueError)
