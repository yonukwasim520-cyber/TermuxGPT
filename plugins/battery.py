import subprocess
import json


ACTION = "battery"


DESCRIPTION = """
Reads phone battery information.

Examples:
- كم نسبة البطارية
- ما حالة البطارية
- battery level
- show battery

Returns:
- percentage
- charging status
- temperature
"""


def run(data):

    result = subprocess.run(
        [
            "termux-battery-status"
        ],
        capture_output=True,
        text=True
    )


    info = json.loads(result.stdout)


    return (
        f"البطارية: {info['percentage']}%\n"
        f"الحالة: {info['status']}\n"
        f"الحرارة: {info['temperature']}°C"
    )