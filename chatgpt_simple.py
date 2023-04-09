import openai
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get("OPEN_AI_API_KEY")
openai.api_key = token

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Act as a priest. Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)