from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import requests
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Passenger(BaseModel):
    pclass: int
    sex: int
    age: float
    fare: float
    traveled_alone: int
    embarked: int

@app.post("/surv_or_not/{model_name}")
async def surv_or_not(model_name: str, passenger: Passenger):
    passenger_dict = passenger.dict()  # Convert to dictionary
    print(type(passenger_dict))
    response = requests.post(f"http://127.0.0.1:8000/surv/{model_name}", json=passenger_dict)
    return response.json()

@app.get("/api")
def read_root():
    return {"message": "Hello World"}

app.mount("/", StaticFiles(directory="dist", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)