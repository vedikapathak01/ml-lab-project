import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
import numpy as np
import os

# 🔥 Only use tracking URI locally, not in CI
if os.getenv("GITHUB_ACTIONS") != "true":
    mlflow.set_tracking_uri("http://127.0.0.1:5003")

mlflow.set_experiment("local-exp")

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])

model = LinearRegression()
model.fit(X, y)

with mlflow.start_run():
    mlflow.log_param("weight", 2)
    mlflow.log_param("bias", 1)
    mlflow.log_metric("accuracy", 0.95)

    mlflow.sklearn.log_model(model, "model")

    print("Training complete")