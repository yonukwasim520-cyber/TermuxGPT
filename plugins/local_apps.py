import os


APP_FILE = "/sdcard/TermuxGPT/apps.txt"


def search_local_apps(query):
    results = []

    if not os.path.exists(APP_FILE):
        return results


    try:
        with open(APP_FILE, "r", encoding="utf-8") as f:

            for line in f:

                line = line.strip()

                if "|" not in line:
                    continue


                name, package = line.split("|", 1)


                if query.lower() in name.lower():

                    results.append({
                        "name": name,
                        "package": package
                    })


    except Exception as e:
        print("Error:", e)


    return results