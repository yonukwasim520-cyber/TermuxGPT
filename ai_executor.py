import subprocess


def run_ai_action(command):

    action = command.get("action")



    # =====================
    # Flashlight
    # =====================

    if action == "flashlight":

        state = command.get(
            "state",
            "on"
        )

        subprocess.run(
            [
                "termux-torch",
                state
            ]
        )

        return "تم التحكم بالفلاش."



    # =====================
    # Vibration
    # =====================

    if action == "vibrate":

        repeat = command.get(
            "repeat",
            1
        )

        duration = command.get(
            "duration",
            300
        )


        for _ in range(repeat):

            subprocess.run(
                [
                    "termux-vibrate",
                    "-f",
                    "-d",
                    str(duration)
                ]
            )


        return "تم تنفيذ الاهتزاز."



    # =====================
    # Volume
    # =====================

    if action == "volume":

        level = command.get(
            "level",
            50
        )


        subprocess.run(
            [
                "termux-volume",
                "music",
                str(level)
            ]
        )


        return "تم ضبط الصوت."



    # =====================
    # Brightness
    # =====================

    if action == "brightness":

        level = command.get(
            "level",
            50
        )


        subprocess.run(
            [
                "termux-brightness",
                str(level)
            ]
        )


        return "تم ضبط السطوع."



    # =====================
    # Open application
    # =====================

    if action == "open_app":

        package = command.get(
            "package"
        )


        if package:

            subprocess.run(
                [
                    "monkey",
                    "-p",
                    package,
                    "1"
                ]
            )

            return "تم فتح التطبيق."



    return None