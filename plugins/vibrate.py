import subprocess
import time


ACTION = "vibrate"


DESCRIPTION = """
Controls phone vibration.

Examples:
- اهتز الهاتف
- اجعل الهاتف يهتز خمس مرات
- vibrate phone
- repeat vibration

Parameters:
- repeat: number of vibrations
- duration: vibration time in milliseconds
- pattern: normal or alert
"""


MAX_REPEAT = 30
MAX_DURATION = 30000


def run(data):

    repeat = int(data.get("repeat", 1))
    duration = int(data.get("duration", 300))
    pattern = data.get("pattern", "normal")


    repeat = min(repeat, MAX_REPEAT)
    duration = min(duration, MAX_DURATION)


    if pattern == "alert":

        for i in range(repeat):

            subprocess.run([
                "termux-vibrate",
                "-f",
                "-d",
                str(duration)
            ])

            if i < repeat - 1:
                time.sleep(0.3)

    else:

        subprocess.run([
            "termux-vibrate",
            "-f",
            "-d",
            str(duration)
        ])


    return "تم تنفيذ الاهتزاز."