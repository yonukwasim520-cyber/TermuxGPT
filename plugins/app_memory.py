import json
import os


FILE = "data/apps.json"


def load_apps():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save_apps(apps):

    os.makedirs(
        "data",
        exist_ok=True
    )

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            apps,
            f,
            ensure_ascii=False,
            indent=2
        )



def get_package(name):

    apps = load_apps()

    return apps.get(name.lower())



def remember(name, package):

    apps = load_apps()

    apps[name.lower()] = package

    save_apps(apps)
