import os
import random

from dotenv import load_dotenv

import openai

load_dotenv()


class gpt:

    def response_gpt(self, response, user_content):
        apikeys = os.environ["APIKEY"]
        apik = apikeys.split(",")
        openai.api_key = random.choice(apik)
        openai.api_base = "https://api.openai.iniad.org/api/v1"
        messages = response

        messages.append({"role": "user", "content": user_content})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        agent_res = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": agent_res})
        if (len(messages) > 6):
            messages.pop(0)
        return messages
