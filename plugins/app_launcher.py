import subprocess
from plugins.app_memory import remember, get_package


def get_activity(package):

    result = subprocess.run(
        [
            "cmd",
            "package",
            "resolve-activity",
            "--brief",
            "--user",
            "0",
            package
        ],
        capture_output=True,
        text=True
    )

    lines = result.stdout.strip().splitlines()

    for line in reversed(lines):
        if "/" in line:
            return line

    return None



def launch(package):

    activity = get_activity(package)

    if not activity:
        return False

    subprocess.run(
        [
            "am",
            "start",
            "-n",
            activity
        ]
    )

    return True



def open_app(name, possible_packages):

    # 1- البحث في الذاكرة
    saved = get_package(name)

    if saved:

        if launch(saved):
            return {
                "status": "opened",
                "source": "memory",
                "package": saved
            }


    # 2- تجربة الحزم
    for package in possible_packages:

        if launch(package):

            remember(
                name,
                package
            )

            return {
                "status": "opened",
                "source": "search",
                "package": package
            }


    return {
        "status": "not_found"
    }