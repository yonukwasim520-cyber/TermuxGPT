import requests

from config import API_KEY



def ask_ai(message):

    url = "https://openrouter.ai/api/v1/chat/completions"


    headers = {

        "Authorization": f"Bearer {API_KEY}",

        "Content-Type": "application/json"

    }


    data = {

        "model": "openai/gpt-4o-mini",

        "messages": [

            {

                "role": "system",

                "content": """
You are TermuxGPT.

Rules:
- Understand Arabic and English.
- Reply in the same language as the user.
- Do not execute commands yourself.
- If the user asks for a phone action, describe it clearly.
"""

            },

            {

                "role": "user",

                "content": message

            }

        ]

    }


    response = requests.post(

        url,

        headers=headers,

        json=data,

        timeout=60

    )


    if response.status_code != 200:

        return (
            "AI Error: "
            + str(response.status_code)
        )


    result = response.json()


    return result["choices"][0]["message"]["content"]