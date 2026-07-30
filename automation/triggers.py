import subprocess
import json
import datetime


def get_battery():

    try:

        result = subprocess.run(
            ["termux-battery-status"],
            capture_output=True,
            text=True
        )

        data = json.loads(
            result.stdout
        )

        return data.get(
            "percentage",
            100
        )

    except:

        return 100



def is_charging():

    try:

        result = subprocess.run(
            ["termux-battery-status"],
            capture_output=True,
            text=True
        )

        data = json.loads(
            result.stdout
        )

        status = data.get(
            "status",
            ""
        )


        return status.lower() == "charging"


    except:

        return False



def get_time():

    now = datetime.datetime.now()

    return now.hour



def check_trigger(trigger):

    trigger_type = trigger.get(
        "type"
    )


    if trigger_type == "battery":

        battery = get_battery()

        value = trigger.get(
            "value",
            0
        )

        condition = trigger.get(
            "condition",
            "<="
        )


        if condition == "<=":

            return battery <= value


        if condition == ">=":

            return battery >= value



    elif trigger_type == "charging":

        state = trigger.get(
            "state"
        )


        if state == "connected":

            return is_charging()



    elif trigger_type == "time":

        hour = trigger.get(
            "hour"
        )

        return get_time() == hour



    return False
