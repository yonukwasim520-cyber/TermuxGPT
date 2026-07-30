def guess_packages(name):

    name = name.lower().replace(" ", "")

    guesses = []


    # احتمالات عامة
    guesses.append(name)

    guesses.append(
        "com." + name
    )

    guesses.append(
        "cn." + name
    )


    # أشهر صيغ الشركات
    guesses.append(
        "com." + name + ".app"
    )

    guesses.append(
        "com." + name + ".game"
    )


    return guesses
