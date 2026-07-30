import urllib.request
import urllib.parse
import re


def search_apkmirror(name):

    results = []

    query = urllib.parse.quote(name)

    url = f"https://www.apkmirror.com/?post_type=app_release&searchtype=apk&s={query}"

    try:

        html = urllib.request.urlopen(
            url,
            timeout=10
        ).read().decode(
            "utf-8",
            errors="ignore"
        )


        packages = re.findall(
            r'/apk/([^/]+)/',
            html
        )


        for package in packages:

            results.append(
                {
                    "name": name,
                    "package": package
                }
            )


    except Exception as e:

        print("APKMirror error:", e)


    return results