# -*- coding: utf-8 -*-

from ai import ask_ai
import arabic_reshaper
from bidi.algorithm import get_display
from prompt_toolkit import prompt


def fix_arabic(text):
    try:
        reshaped = arabic_reshaper.reshape(text)
        return get_display(reshaped)
    except:
        return text


print(" TermuxGPT Started")
print("Press Ctrl+C to exit\n")


while True:
    try:
        user = prompt("You: ")

        if not user.strip():
            continue

        answer = ask_ai(user)

        print("\nGPT:")
        print(fix_arabic(answer))
        print()

    except KeyboardInterrupt:
        print("\n\n TermuxGPT Closed")
        break

    except Exception as error:
        print("\nError:")
        print(error)
        print()