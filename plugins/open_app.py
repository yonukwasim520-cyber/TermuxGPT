from plugins.ai_actions import open_application


ACTION = "open_app"

DESCRIPTION = """
Open an installed Android application by its name.
Use when the user wants to open, launch, start, or run an app.
Input:
{
 "input": "application name"
}
"""


def run(command):

    app_name = command.get("input")

    if not app_name:
        return {
            "success": False,
            "message": "No application name"
        }


    return open_application(app_name)
