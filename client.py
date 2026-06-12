'''from openai import OpenAI
import os
client = OpenAI(
    api_key="(api_key=os.environ.get(YOUR API KEY")


completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    massages = [
        {"role":"system","content": "You are a visual assistant named AI skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user","content": "what is coding"}
    ]
    )

print(completion.choices[0].massages.content)'''

from openai import OpenAI

client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a visual assistant named AI skilled in general tasks like Alexa and Google Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)
