from plugins.ai_actions import open_application


TOOLS = {
    "open_app": open_application
}


def run_tool(tool_name, argument):

    if tool_name not in TOOLS:
        return {
            "success": False,
            "message": "Tool not found"
        }

    return TOOLS[tool_name](argument)
