import subprocess
import shutil


def execute_command(action, data):

    if action == "vibrate":

        duration = data.get("duration", 1000)

        command = [
            "termux-vibrate",
            "-f",
            "-d",
            str(duration)
        ]

        if shutil.which("termux-vibrate") is None:
            return "Termux:API غير موجود"

        subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return f"تم اهتزاز الهاتف لمدة {duration}ms"


    return "الأمر غير مدعوم"