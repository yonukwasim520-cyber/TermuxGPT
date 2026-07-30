import subprocess


ACTION = "notification"

DESCRIPTION = "إرسال إشعار للهاتف"



def run(command):

    title = command.get(
        "title",
        "TermuxGPT"
    )

    message = command.get(
        "message",
        ""
    )


    subprocess.run(
        [
            "termux-notification",
            "--title",
            title,
            "--content",
            message
        ]
    )


    return "تم إرسال الإشعار"
