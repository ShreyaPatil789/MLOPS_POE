
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Addition API")



class Numbers(BaseModel):
    num1: float
    num2: float



def add_numbers(a, b):
    return a + b



@app.post("/add")
def addition(data: Numbers):
    result = add_numbers(data.num1, data.num2)

    return {
        "num1": data.num1,
        "num2": data.num2,
        "addition": result
    }


@app.get("/")
def home():
    return {"message": "Welcome to Addition API"}
