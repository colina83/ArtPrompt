import openai
import json

config_file_path = 'C:/Users/Francisco.Colina/Documents/Code/ArtPrompt/ArtLLM/Prompt/config.json'

with open(config_file_path) as f:
    config = json.load(f)

openai.api_key = config['OPENAI_API_KEY']

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