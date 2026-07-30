from google_play_scraper import search


def search_playstore(name):

    results = []

    try:

        apps = search(
            name,
            lang="en",
            country="us"
        )

        name_lower = name.lower()

        for app in apps:

            title = app.get("title", "")
            package = app.get("appId")

            if package and name_lower in title.lower():

                results.append(
                    {
                        "name": title,
                        "package": package
                    }
                )

    except Exception as e:

        print("Play Store error:", e)

    return results