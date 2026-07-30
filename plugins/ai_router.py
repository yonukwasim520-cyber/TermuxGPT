import json
from plugins.tools import run_tool


def handle_ai_response(response):

    try:
        data = json.loads(response)

    except:
        return {
            "success": False,
            "message": "AI response is not JSON"
        }


    if "tool" in data:

        return run_tool(
            data["tool"],
            data.get("input", "")
        )


    return {
        "success": True,
        "message": data.get("message", "")
    }
