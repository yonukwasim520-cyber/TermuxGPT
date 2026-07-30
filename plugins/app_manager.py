import subprocess
import re


def get_packages():

    result = subprocess.run(
        ["pm", "list", "packages"],
        capture_output=True,
        text=True
    )

    packages = []

    for line in result.stdout.splitlines():

        if line.startswith("package:"):

            packages.append(
                line.replace("package:", "").strip()
            )

    return packages



def get_app_label(package):

    result = subprocess.run(
        [
            "/system/bin/dumpsys",
            "package",
            package
        ],
        capture_output=True,
        text=True
    )

    output = result.stdout


    # البحث عن label
    match = re.search(
        r'label=([^,\n]+)',
        output
    )


    if match:
        return match.group(1).strip()


    return None



def search_app(name):

    name = name.lower()

    apps = []


    for package in get_packages():

        label = get_app_label(package)


        if label:

            apps.append({
                "name": label,
                "package": package
            })


            if name in label.lower():

                return {
                    "name": label,
                    "package": package
                }


    return None