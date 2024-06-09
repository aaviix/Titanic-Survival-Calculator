from fastapi.testclient import TestClient
from main import app  # Import the FastAPI app

client = TestClient(app)

def test_landing_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Survival Calculator" in response.text

def test_predict_endpoint():
    response = client.post("/predict", json={
        "PClass": 3,
        "Sex": "male",
        "Age": 22,
        "Fare": 7.25,
        "TraveledAlone": True,
        "Embarked": "Southampton"
    })
    assert response.status_code == 200
    assert response.json()["prediction"] in ["Survived", "Did not survive"]
