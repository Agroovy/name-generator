#Entry point of the application
import os
import json

with open("config.json") as read_file:
    data = json.load(read_file)

if data["first_time"]:
    modules = ["pyperclip", "PySimpleGUI", "pystray", "playsound"]
    command = "python -m pip install " + " ".join(modules)
    os.system(command)
    import settings_gui

import tray

#If it's the first time, import all modules and run settings_gui.py
#Regardless, run tray.py