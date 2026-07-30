import subprocess


ACTION = "brightness"


DESCRIPTION = """
Controls screen brightness.

Examples:
- خلي السطوع 50
- اجعل السطوع 80
- set brightness 50

Parameters:
- level: 0-100
"""


def run(data):

    level = data.get(
        "level",
        50
    )

    try:
        level = int(level)
    except:
        level = 50


    if level < 0:
        level = 0

    if level > 100:
        level = 100


    result = subprocess.run(
        [
            "termux-brightness",
            str(level)
        ],
        capture_output=True,
        text=True
    )


    if result.returncode == 0:

        return f"تم ضبط السطوع إلى {level}%"

    else:

        return (
            "فشل تغيير السطوع: "
            + result.stderr
        )