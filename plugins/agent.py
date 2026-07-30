from plugins.tools import run_tool


def process_command(text):

    text = text.strip()


    if text.startswith("افتح "):

        app_name = text.replace("افتح ", "", 1).strip()

        return run_tool(
            "open_app",
            app_name
        )


    return {
        "success": False,
        "message": "لا أعرف هذا الأمر"
    }
