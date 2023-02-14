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
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" USER:", " AI:"]
    )
    return response.choices[0].text.replace('BOT:', '').replace('AARON:', '')

