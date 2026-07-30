import json
import time
import os
import subprocess

from automation.triggers import check_trigger


RULES_FILE = "automation/rules.json"
STATE_FILE = "automation/state.json"



def load_json(file):

    if not os.path.exists(file):

        return {}


    try:

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except Exception:

        return {}



def save_json(file, data):

    os.makedirs(
        "automation",
        exist_ok=True
    )


    with open(
        file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )



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


    except Exception:

        return []



def execute_action(action):

    name = action.get(
        "name"
    )


    print(
        "Executing:",
        action
    )



    if name == "vibrate":

        repeat = action.get(
            "repeat",
            1
        )

        duration = action.get(
            "duration",
            300
        )


        for i in range(repeat):

            subprocess.run(
                [
                    "termux-vibrate",
                    "-f",
                    "-d",
                    str(duration)
                ]
            )


            time.sleep(0.5)



    elif name == "flashlight":

        state = action.get(
            "state",
            "on"
        )


        subprocess.run(
            [
                "termux-torch",
                state
            ]
        )



    elif name == "notification":

        subprocess.run(
            [
                "termux-notification",
                "--title",
                action.get(
                    "title",
                    "TermuxGPT"
                ),
                "--content",
                action.get(
                    "message",
                    "تم التنفيذ"
                )
            ]
        )



def check_rules():

    rules = load_rules()

    state = load_json(
        STATE_FILE
    )


    for index, rule in enumerate(rules):

        trigger = rule.get(
            "trigger",
            {}
        )

        action = rule.get(
            "action",
            {}
        )


        rule_id = str(index)


        try:

            active = check_trigger(
                trigger
            )


            already_done = state.get(
                rule_id,
                False
            )



            if active and not already_done:

                execute_action(
                    action
                )


                state[rule_id] = True


                save_json(
                    STATE_FILE,
                    state
                )



            elif not active:

                # السماح بالتنفيذ مرة أخرى بعد تغير الحالة

                state[rule_id] = False


                save_json(
                    STATE_FILE,
                    state
                )



        except Exception as e:

            print(
                "Rule error:",
                e
            )



def start():

    print(
        "Automation Monitor Started"
    )


    while True:

        check_rules()


        # فحص كل ثانيتين

        time.sleep(
            2
        )



if __name__ == "__main__":

    start()