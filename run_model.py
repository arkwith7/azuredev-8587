# Install the following dependencies: azure.identity and azure-ai-inference
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = os.getenv("AZURE_INFERENCE_SDK_ENDPOINT", "https://hspar-m7k2pfor-swedencentral.services.ai.azure.com/models")
deployment_name = "DeepSeek-R1"
key = os.getenv("AZURE_INFERENCE_SDK_KEY", "YOUR_KEY_HERE")
client = ChatCompletionsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

response = client.complete(
  messages=[
    SystemMessage(content="You are a helpful assistant."),
    UserMessage(content="What are 3 things to visit in Seattle?")
  ],
  max_tokens=2048,
    model = deployment_name,
)

print(response)