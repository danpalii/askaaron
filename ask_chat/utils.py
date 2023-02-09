import openai
from decouple import config

def getCHAT(prompt,temperature):
    model = 'text-davinci-003'
    openai.api_key = config('API_KEY')
    response = openai.Completion.create(
        prompt=prompt,
        max_tokens=4000,
        model=model,
        temperature=int(temperature) / 10,
    )
    return response.choices[0].text.replace('BOT:', '').replace('AARON:', '')

