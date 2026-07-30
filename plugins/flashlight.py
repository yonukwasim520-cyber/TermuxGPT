import subprocess


ACTION = "flashlight"


DESCRIPTION = """
Controls phone flashlight.

Examples:
- شغل الفلاش
- افتح الكشاف
- اطفئ الفلاش
- turn on flashlight
- turn off flashlight

Parameters:
- state: on or off
"""


def run(data):

    state = data.get("state", "on")


    subprocess.run([
        "termux-torch",
        state
    ])


    if state == "on":
        return "تم تشغيل الفلاش."

    return "تم إيقاف الفلاش."