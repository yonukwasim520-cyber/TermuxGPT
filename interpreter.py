import re


def normalize(text):
    return text.lower().strip()



def interpret_command(text):

    text = normalize(text)


    # أوامر الاهتزاز
    vibrate_words = [
        "اهتز",
        "اهتز الهاتف",
        "هز الهاتف",
        "هز الجوال",
        "اجعل الهاتف يهتز",
        "اجعل هاتفي يهتز",
        "اهتز هاتفي",
        "vibrate",
        "vibrate my phone",
        "make my phone vibrate"
    ]


    for word in vibrate_words:

        if word in text:


            # القيمة الافتراضية ثانية واحدة
            duration = 1000


            numbers = re.findall(
                r"\d+",
                text
            )


            if numbers:

                value = int(numbers[0])


                # تحويل الثواني إلى milliseconds
                if (
                    "ثانية" in text
                    or "ثواني" in text
                    or "second" in text
                    or "seconds" in text
                ):

                    duration = value * 1000

                else:

                    duration = value



            return {

                "action": "vibrate",

                "duration": duration

            }



    return {

        "action": "none"

    }