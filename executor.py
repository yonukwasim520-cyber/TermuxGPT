import os
import importlib


PLUGIN_FOLDER = "plugins"



def load_plugins():

    plugins = {}


    if not os.path.exists(PLUGIN_FOLDER):

        return plugins



    for file in os.listdir(PLUGIN_FOLDER):

        if (
            file.endswith(".py")
            and file != "__init__.py"
        ):

            name = file[:-3]


            try:

                module = importlib.import_module(
                    f"{PLUGIN_FOLDER}.{name}"
                )


                if hasattr(module, "ACTION"):

                    plugins[module.ACTION] = module


            except Exception as e:

                print(
                    "Plugin error:",
                    name,
                    e
                )


    return plugins




PLUGINS = load_plugins()




def execute_command(command):


    if not isinstance(command, dict):

        return "أمر غير صحيح"



    action = command.get(
        "action"
    )


    if not action:

        return "لا يوجد Action"



    print(
        "Executing:",
        action
    )



    # تشغيل Plugin

    if action in PLUGINS:


        plugin = PLUGINS[action]


        if hasattr(
            plugin,
            "run"
        ):

            try:

                return plugin.run(
                    command
                )


            except Exception as e:

                print(
                    "Plugin execution error:",
                    e
                )

                return (
                    "حدث خطأ أثناء التنفيذ: "
                    + str(e)
                )



        else:

            return (
                "Plugin لا يحتوي run()"
            )



    # تشغيل AI Executor كخطة احتياطية

    try:

        from ai_executor import run_ai_action


        result = run_ai_action(
            command
        )


        if result:

            return result



    except Exception as e:

        print(
            "AI Executor Error:",
            e
        )



    return "الأمر غير مدعوم."