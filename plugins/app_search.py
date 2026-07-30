import subprocess


def search_package(keyword):

    try:
        result = subprocess.run(
            [
                "pm",
                "list",
                "packages"
            ],
            capture_output=True,
            text=True
        )

        packages = result.stdout.splitlines()

        keyword = keyword.lower()


        for line in packages:

            package = line.replace(
                "package:",
                ""
            ).strip()


            if keyword in package.lower():

                return package


        return None


    except Exception:

        return None
