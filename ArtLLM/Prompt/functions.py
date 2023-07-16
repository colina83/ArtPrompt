import openai
import json
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

def get_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        temperature = 0.9,
        n=1,
        stop=None,
    )
    
    #print(response) # Just to check the output of openai
    anwser = response.choices[0].text.strip()
    return anwser