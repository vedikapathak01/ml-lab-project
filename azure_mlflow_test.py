from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import mlflow
import azureml.mlflow

# Connect to Azure ML Workspace
ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id="eb30c6c9-c272-437c-bcf2-e45b97008f11",
    resource_group_name="ml-rg",
    workspace_name="ml-workspace"
)

# Set MLflow tracking URI
mlflow.set_tracking_uri(ml_client.workspaces.get("ml-workspace").mlflow_tracking_uri)

mlflow.set_experiment("mlflow-azure-exp")

with mlflow.start_run():
    mlflow.log_param("weight", 2)
    mlflow.log_param("bias", 1)
    mlflow.log_metric("accuracy", 0.95)

    print("✅ Logged to Azure MLflow!")