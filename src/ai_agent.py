from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()
def summarize_text(text):
    chat_completion = client.chat.completions.create(
    messages=[
        {
              "role": "user",
             "content": f"Fasse folgenden Text zusammen:\n\n{text}",
        }
        ],
        model="groq/compound-mini",
        max_tokens=150,
    )
    return chat_completion.choices[0].message.content
