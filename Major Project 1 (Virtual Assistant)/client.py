from openai import OpenAI

#pip install openai

# defaults to getting the keys using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
from openai import OpenAI
def aiProcess(command):
    client = OpenAI(
    api_key="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"
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "system" , "content" :"you are a virtual assistant Jarvis just like Alexa and Gogle Cloud"},
        {"role": "user", "content": "what is coding"}
    ]
    )

    return (completion.choices[0].message)
