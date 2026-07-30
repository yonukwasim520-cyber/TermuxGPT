from flask import Flask, request, jsonify
import threading

from command_ai import understand
from ai import ask_ai
from executor import execute_command
from action_parser import parse_action

from automation.monitor import start as start_monitor


pending_setup = None



def process_message(text):

    global pending_setup


    # =========================
    # Setup Flow
    # =========================

    if pending_setup:


        if pending_setup["type"] == "notification":


            if pending_setup["step"] == 1:


                pending_setup["title"] = text

                pending_setup["step"] = 2


                return "اكتب وصف الإشعار"



            elif pending_setup["step"] == 2:


                command = {

                    "is_command": True,

                    "action": "notification",

                    "title": pending_setup["title"],

                    "message": text

                }


                pending_setup = None


                return execute_command(command)




    # =========================
    # Action Parser
    # =========================

    parsed = parse_action(text)


    if parsed:


        return execute_command(parsed)




    # =========================
    # AI Understanding
    # =========================

    command = understand(text)


    print(
        "AI RESULT:",
        command
    )



    if isinstance(command, dict):


        command["original_text"] = text



        if command.get(
            "is_command",
            False
        ):



            if command.get(
                "action"
            ) == "notification_setup":


                pending_setup = {


                    "type": "notification",

                    "step": 1


                }


                return "اكتب عنوان الإشعار"




            return execute_command(command)




    # =========================
    # Normal AI Chat
    # =========================

    return ask_ai(text)





bridge = Flask(__name__)





@bridge.route("/", methods=["GET"])
def home():


    return "TermuxGPT Bridge Running"





@bridge.route("/bridge", methods=["POST"])
def receive_command():


    try:


        data = request.get_json()



        print(
            "REQUEST:",
            data
        )



        text = data.get(

            "message",

            ""

        )



        if not text:


            return jsonify({

                "status": "error",

                "message": "Empty message"

            })




        print(

            "USER MESSAGE:",

            text

        )



        result = process_message(text)




        print(

            "AI RESPONSE:",

            result

        )




        return jsonify({


            "status": "success",

            "result": str(result)


        })




    except Exception as e:



        print(

            "ERROR:",

            e

        )



        return jsonify({


            "status": "error",

            "message": str(e)


        })





if __name__ == "__main__":



    threading.Thread(

        target=start_monitor,

        daemon=True

    ).start()



    bridge.run(

        host="0.0.0.0",

        port=8765,

        debug=False

    )