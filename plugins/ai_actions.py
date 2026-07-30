# plugins/ai_actions.py

from plugins.local_apps import search_local_apps
from plugins.app_launcher import open_app


def open_application(app_name):

    apps = search_local_apps(app_name)

    if not apps:
        return {
            "success": False,
            "message": "لم يتم العثور على التطبيق"
        }


    app = apps[0]

    package = app["package"]


    result = open_app(
        app["name"],
        [package]
    )


    return {
        "success": True,
        "app": app["name"],
        "package": package,
        "result": result
    }
