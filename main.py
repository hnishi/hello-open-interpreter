import os

import openai
import interpreter
from dotenv import load_dotenv


load_dotenv()

openai.api_type = "azure"
openai.api_key = os.environ["AZURE_OPENAI_API_KEY"]
openai.api_base = os.environ["AZURE_OPENAI_ENDPOINT"]
openai.api_version = os.environ["AZURE_OPENAI_API_VERSION"]

interpreter.model = "azure/" + os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
# interpreter.llm.model = "azure/" + os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
# interpreter.chat()

interpreter.chat(
    "Plot AAPL and META's normalized stock prices"
)  # Executes a single command
# interpreter.chat()

exit()

message = "What operating system are we on?"
for chunk in interpreter.chat(message, display=False, stream=True):
    print(chunk)
