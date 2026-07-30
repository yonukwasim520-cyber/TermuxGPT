from plugins.sources.playstore import search_playstore
from plugins.sources.apkpure import search_apkpure
from plugins.sources.apkmirror import search_apkmirror


def search_package(name):

    results = []

    sources = [
        search_playstore,
        search_apkpure,
        search_apkmirror
    ]


    for source in sources:

        try:

            data = source(name)

            if data:
                results.extend(data)

        except Exception:
            pass


    return results