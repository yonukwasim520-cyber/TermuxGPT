import json
import os


ACTION = "automation"


DESCRIPTION = """
Create automatic rules.

Examples:

- عندما يبدأ الشحن شغل الفلاش
- إذا وصلت البطارية 10 اهتز 5 مرات
- when charging starts turn on flashlight

Creates rules that monitor.py executes later.
"""


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



def save_rules(rules):

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



def run(data):

    rule = data.get(
        "rule"
    )


    if not rule:

        return "لم يتم العثور على قاعدة."



    rules = load_rules()


    rules.append(
        rule
    )


    save_rules(
        rules
    )


    return "تم حفظ القاعدة، سيتم تنفيذها عند تحقق الشرط."