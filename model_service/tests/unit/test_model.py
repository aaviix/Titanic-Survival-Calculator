import pytest
import pickle
import os
from model import load_model, predict

# Define a fixture for loading models
@pytest.fixture
def model():
    model_path = 'models/Random Forest.pkl'
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def test_load_model():
    model_path = 'models/Random Forest.pkl'
    model = load_model(model_path)
    assert model is not None

def test_predict(model):
    # Example input based on Titanic dataset features
    example_input = [[3, 1, 22, 7.25, 1, 0]]
    prediction = predict(model, example_input)
    assert prediction in [0, 1]  # The output should be either 0 or 1
