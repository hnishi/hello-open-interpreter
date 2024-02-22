import os

from interpreter import interpreter
from dotenv import load_dotenv


load_dotenv()

interpreter.llm.model = "azure/" + os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
interpreter.chat()

