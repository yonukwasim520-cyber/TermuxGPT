import subprocess
import json


ACTION = "volume"


DESCRIPTION = """
Controls phone volume.

Examples:
- خلي الصوت 50
- اجعل الصوت 80
- set volume 30

Parameters:
- level: percentage from 0 to 100
"""


def get_max_volume():

    try:

        result = subprocess.run(
            [
                "termux-volume"
            ],
            capture_output=True,
            text=True
        )


        data = json.loads(
            result.stdout
        )


        for item in data:

            if item.get("stream") == "music":

                return int(
                    item.get(
                        "max_volume",
                        16
                    )
                )


    except Exception:

        pass


    # قيمة احتياطية إذا فشل الحصول عليها
    return 16



def run(data):

    level = data.get(
        "level",
        50
    )


    try:

        level = int(level)

    except:

        level = 50


    # حماية النسبة
    level = max(
        0,
        min(
            level,
            100
        )
    )


    # معرفة عدد خطوات الجهاز
    max_volume = get_max_volume()


    # تحويل النسبة إلى نقاط الجهاز
    points = round(
        max_volume * level / 100
    )


    subprocess.run(
        [
            "termux-volume",
            "music",
            str(points)
        ]
    )


    return (
        f"تم ضبط الصوت {level}% "
        f"({points}/{max_volume})"
    )
