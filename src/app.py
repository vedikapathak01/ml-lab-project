from fastapi import FastAPI
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

app = FastAPI()

# Train simple model
data = load_iris()
X, y = data.data, data.target
model = RandomForestClassifier()
model.fit(X, y)

@app.get("/")
def home():
    return {"message": "ML API is running 🚀"}

@app.get("/predict")
def predict(sepal_length: float, sepal_width: float,
            petal_length: float, petal_width: float):

    pred = model.predict(
        [[sepal_length, sepal_width, petal_length, petal_width]]
    )

    return {"prediction": int(pred[0])}