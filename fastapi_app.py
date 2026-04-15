from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML API is running"}

@app.get("/predict")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    # dummy logic
    result = "setosa" if petal_length < 2 else "versicolor"
    return {"prediction": result}