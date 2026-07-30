import re



def parse_action(text):

    text = text.lower().strip()



    # =========================
    # Automation
    # =========================

    if (
        "عندما" in text
        or "إذا" in text
        or "اذا" in text
        or "لما" in text
        or "عند" in text
        or "when" in text
        or "if" in text
    ):


        # =====================
        # Charging trigger
        # =====================

        if (
            "شحن" in text
            or "الشحن" in text
            or "اشحن" in text
            or "أشحن" in text
            or "يشحن" in text
            or "الشاحن" in text
            or "اوصل الشاحن" in text
            or "وصل الشاحن" in text
            or "charging" in text
        ):


            if (
                "فلاش" in text
                or "كشاف" in text
                or "flashlight" in text
            ):

                return {

                    "is_command": True,

                    "action": "automation",

                    "rule": {

                        "trigger": {

                            "type": "charging",

                            "state": "connected"

                        },


                        "action": {

                            "name": "flashlight",

                            "state": "on"

                        }

                    }

                }



        # =====================
        # Battery trigger
        # =====================

        if (
            "بطارية" in text
            or "البطارية" in text
            or "battery" in text
        ):


            numbers = re.findall(
                r"\d+",
                text
            )


            if len(numbers) >= 2:


                return {

                    "is_command": True,

                    "action": "automation",

                    "rule": {

                        "trigger": {

                            "type": "battery",

                            "condition": "<=",

                            "value": int(numbers[0])

                        },


                        "action": {

                            "name": "vibrate",

                            "repeat": int(numbers[1]),

                            "duration": 300

                        }

                    }

                }



    # =========================
    # Volume
    # =========================

    if (
        "صوت" in text
        or "volume" in text
    ):


        numbers = re.findall(
            r"\d+",
            text
        )


        if numbers:

            return {

                "is_command": True,

                "action": "volume",

                "level": int(numbers[0])

            }



    # =========================
    # Brightness
    # =========================

    if (
        "سطوع" in text
        or "brightness" in text
    ):


        numbers = re.findall(
            r"\d+",
            text
        )


        if numbers:

            return {

                "is_command": True,

                "action": "brightness",

                "level": int(numbers[0])

            }



    # =========================
    # Flashlight direct
    # =========================

    if (
        "فلاش" in text
        or "كشاف" in text
        or "flashlight" in text
    ):


        state = "on"


        if (
            "اطف" in text
            or "إطف" in text
            or "إيقاف" in text
            or "ايقاف" in text
            or "اغلق" in text
            or "off" in text
        ):

            state = "off"



        return {

            "is_command": True,

            "action": "flashlight",

            "state": state

        }



    # =========================
    # Vibration direct
    # =========================

    if (
        "اهتز" in text
        or "اهتزاز" in text
        or "vibrate" in text
    ):


        numbers = re.findall(
            r"\d+",
            text
        )


        return {

            "is_command": True,

            "action": "vibrate",

            "repeat": int(numbers[0]) if numbers else 1,

            "duration": 300

        }



    return None