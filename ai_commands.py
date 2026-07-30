import json


def parse_ai_response(text):

    try:
        data = json.loads(text)

        action = data.get("action")

        if action:
            return action, data

        return None, None

    except Exception:
        return None, None
