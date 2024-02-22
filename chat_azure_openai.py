import os

import openai
from dotenv import load_dotenv


load_dotenv()

openai.api_type = "azure"
openai.api_key = os.environ["AZURE_OPENAI_API_KEY"]
openai.api_base = os.environ["AZURE_OPENAI_ENDPOINT"]
openai.api_version = "2024-02-15-preview"
# openai.api_version = os.environ["AZURE_OPENAI_API_VERSION"]


# create a chat completion
chat_completion = openai.ChatCompletion.create(
    deployment_id="gpt35-16k",
    model="gpt35-16k",
    messages=[{"role": "user", "content": "Hello world"}],
)

# print the completion
print(chat_completion.choices[0].message.content)
