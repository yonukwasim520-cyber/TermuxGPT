import json
import os


RULES_FILE = "automation/rules.json"


pending = None



def load_rules():

    if not os.path.exists(RULES_FILE):
        return []

    try:
        with open(
            RULES_FILE,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)

    except:
        return []



def save_rule(rule):

    rules = load_rules()

    rules.append(rule)

    os.makedirs(
        "automation",
        exist_ok=True
    )

    with open(
        RULES_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            rules,
            f,
            indent=4,
            ensure_ascii=False
        )



def start_notification_setup(trigger):

    global pending

    pending = {

        "step": "title",

        "trigger": trigger,

        "action": {

            "name": "notification"

        }

    }


    return "اكتب عنوان الإشعار"



def continue_setup(text):

    global pending


    if pending is None:

        return None



    if pending["step"] == "title":


        pending["action"]["title"] = (
            text
            if text.strip()
            else "TermuxGPT"
        )


        pending["step"] = "message"


        return "اكتب نص الإشعار (يمكن تركه فارغ)"



    if pending["step"] == "message":


        pending["action"]["message"] = (

            text

            if text.strip()

            else "تم تنفيذ الإجراء"

        )


        save_rule(
            {
                "trigger": pending["trigger"],
                "action": pending["action"]
            }
        )


        pending = None


        return "تم حفظ قاعدة الإشعار"



def is_waiting():

    return pending is not None