#GUI which configures settings
import sys
import json
import PySimpleGUI as sg
import name_generator

layout = [
#Name entry

    [sg.Text("Welcome! There's just a few more details you have to enter before you can get some silly names\n")],
    [sg.Text("Enter your name. If you don't have an middle name, leave the field blank")],
    [
        sg.Text("First name: ", font = "Courier 12"),
        sg.In(size = (30, 1), enable_events = True, key = "first_name")
    ],
    [
        sg.Text("Middle name:", font = "Courier 12"),
        sg.In(size = (30, 1), enable_events = True, key = "middle_name")
    ],
    [
        sg.Text("Last name:  ", font = "Courier 12"),
        sg.In(size = (30, 1), enable_events = True, key = "last_name")
    ],
    [sg.HorizontalSeparator()],
#Gender choice
    [sg.Text("Choose what genders you want to include for your names.")],
    [sg.Text("Genderless titles like 'Alien' or 'Big Chungus' will be included regardless of your choice")],
    [
        sg.Checkbox("Male", key="m"),
        sg.Checkbox("Female", key="f")
    ],
#Audio choice

    [sg.HorizontalSeparator()],
    [
        sg.Checkbox(
            "Make sound when a name is copied from the notification area",
            key="sound",
            default=True
        )
    ],
#Save and quit
    [sg.Text("Once you save, a red circle will appear in the taskbar.")],
    [sg.Text("Click it for a name to be copied to your clipboard")],
    [sg.Text("Right click it for a menu to close the program or change settings")],
    [sg.Button("Save and close", key="save", button_color=("black", "red"))]
]

with open("config.json") as read_file:
    config = json.load(read_file)

if config["first_time"] == False:
    title = name_generator.name()
else:
    title = "Settings"

window = sg.Window(title, layout, finalize=True, icon="icon.ico")

#Load in all the values
window["first_name"].update(config["first_name"])
window["middle_name"].update(config["middle_name"])
window["last_name"].update(config["last_name"])

window["m"].update(config["m"])
window["f"].update(config["f"])
window["sound"].update(config["sound"])

while True:
    event, values = window.read()
    if event == "Exit":
        break
    if event == sg.WIN_CLOSED:
        sys.exit()

    if event == "save":
        
        config["first_name"] = values["first_name"]
        config["middle_name"] = values["middle_name"]
        config["last_name"] = values["last_name"]

        config["m"] = values["m"]
        config["f"] = values["f"]
        config["sound"] = values["sound"]

        config["first_time"] = False

        with open("config.json", "w") as write_file:
            json.dump(config, write_file)
        
        break 

window.close()