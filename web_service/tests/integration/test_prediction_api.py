import sys
import os
from unittest.mock import patch

# Add the parent directory to the system path to find the main module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@patch("requests.post")
def test_surv_or_not(mock_post):
    # Mock the response of the external API
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {"survived": True}
    
    passenger_data = {
        "pclass": 1,
        "sex": 1,
        "age": 25.0,
        "fare": 100.0,
        "traveled_alone": 1,
        "embarked": 0
    }

    response = client.post("/surv_or_not/model1", json=passenger_data)
    assert response.status_code == 200
    assert response.json() == {"survived": True}
    mock_post.assert_called_once_with(
        "http://127.0.0.1:8080/surv/model1", json=passenger_data
    )
