import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5003")

mlflow.register_model(
    "runs:/d2d877975416445ba91f4a697193c0c5/model",
    "my-model"
)