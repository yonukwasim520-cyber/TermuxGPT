import json
import os


RULES_FILE = "automation/rules.json"



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



def save_rule(rule):

    rules = load_rules()

    rules.append(
        rule
    )


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
