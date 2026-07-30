import json
import requests
import os
import importlib

from config import API_KEY


PLUGIN_FOLDER = "plugins"



def load_plugins_info():

    info = ""

    if not os.path.exists(PLUGIN_FOLDER):

        return info


    for file in os.listdir(PLUGIN_FOLDER):

        if file.endswith(".py") and file != "__init__.py":

            name = file[:-3]

            try:

                plugin = importlib.import_module(
                    f"{PLUGIN_FOLDER}.{name}"
                )


                if (
                    hasattr(plugin, "ACTION")
                    and hasattr(plugin, "DESCRIPTION")
                ):

                    info += f"""
Action:
{plugin.ACTION}

Description:
{plugin.DESCRIPTION}

----------------
"""


            except Exception as e:

                print(
                    "Plugin loading error:",
                    name,
                    e
                )


    return info




def understand(text):


    plugins = load_plugins_info()


    system_prompt = f"""

You are CommandAI.

Your ONLY job is converting user messages into JSON commands.

Return ONLY valid JSON.

Never explain.
Never give tutorials.
Never mention Tasker or other apps.



If it is not a command:

{{
"is_command": false
}}



Available plugins:

{plugins}



=====================
DIRECT COMMANDS
=====================


Flashlight ON:

User:
شغل الفلاش

Return:

{{
"is_command":true,
"action":"flashlight",
"state":"on"
}}



Flashlight OFF:

User:
اطفئ الفلاش

Return:

{{
"is_command":true,
"action":"flashlight",
"state":"off"
}}



Vibration:

User:
اهتز الهاتف 5 مرات

Return:

{{
"is_command":true,
"action":"vibrate",
"repeat":5,
"duration":300
}}



=====================
SETUP COMMANDS
=====================


Notification:

User:
ارسل إشعار

Return:

{{
"is_command":true,
"action":"notification_setup"
}}



Vibration without number:

User:
اهتز

Return:

{{
"is_command":true,
"action":"vibrate_setup"
}}



Volume without number:

User:
غير الصوت

Return:

{{
"is_command":true,
"action":"volume_setup"
}}



Brightness without number:

User:
غير السطوع

Return:

{{
"is_command":true,
"action":"brightness_setup"
}}



=====================
AUTOMATION
=====================


Words:

- لما
- عندما
- عند
- إذا
- اذا
- when
- if


mean automation.

Never execute directly.



Charging example:

User:

لما أشحن هاتفي شغل الفلاش


Return:


{{
"is_command":true,
"action":"automation",
"rule":{{
"trigger":{{
"type":"charging",
"state":"connected"
}},
"action":{{
"name":"flashlight",
"state":"on"
}}
}}
}}



Charging notification:

User:

لما أشحن هاتفي أرسل إشعار


Return:


{{
"is_command":true,
"action":"automation",
"rule":{{
"trigger":{{
"type":"charging",
"state":"connected"
}},
"action":{{
"name":"notification"
}}
}}
}}



Battery:

User:

إذا وصلت البطارية 10 اهتز


Return:


{{
"is_command":true,
"action":"automation",
"rule":{{
"trigger":{{
"type":"battery",
"condition":"<=",
"value":10
}},
"action":{{
"name":"vibrate",
"repeat":1,
"duration":300
}}
}}
}}



Rules:

- Always JSON only.
- Automation words create rules.
- Do not explain.
- Maximum repeat 30.
- Maximum duration 30000.



User message:

{text}

"""


    try:


        response = requests.post(

            "https://openrouter.ai/api/v1/chat/completions",

            headers={

                "Authorization":
                f"Bearer {API_KEY}",

                "Content-Type":
                "application/json"

            },


            json={

                "model":
                "openai/gpt-4o-mini",


                "messages":[

                    {
                        "role":"system",
                        "content":system_prompt
                    },

                    {
                        "role":"user",
                        "content":text
                    }

                ],


                "temperature":0

            },


            timeout=60

        )


        data = response.json()


        result = data["choices"][0]["message"]["content"]


        return json.loads(result)



    except Exception as e:


        print(
            "Command AI Error:",
            e
        )


        return {
            "is_command":False
        }