import urllib.request
import urllib.parse
import re


def search_apkpure(name):

    results = []

    query = urllib.parse.quote(name)

    url = f"https://apkpure.com/search?q={query}"

    try:

        html = urllib.request.urlopen(
            url,
            timeout=10
        ).read().decode(
            "utf-8",
            errors="ignore"
        )


        packages = re.findall(
            r'/([^/]+)/download',
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

        print("APKPure error:", e)


    return results