import json
import pystray
import pyperclip
import playsound

from PIL import Image
from name_generator import name

#Yes, I could've used PySimpleGUI for the system tray
#but I added the gui after the tray icon and I had already implemented pystray

with open("config.json") as read_file:
    do_sound = json.load(read_file)['sound']

def stop_program():
    tray_icon.stop()

def change_settings():
    import settings_gui

def copy_name():
    pyperclip.copy(name())
    if do_sound:
        playsound.playsound("confirmation.mp3")

tray_icon = pystray.Icon(
    "chungus",
    Image.open("icon.ico"),
    menu = pystray.Menu(
        pystray.MenuItem( #When right clicked
            "Close name generator",
            stop_program
        ),
        pystray.MenuItem(
            "Change settings",
            change_settings
        ),
        pystray.MenuItem( #When left clicked
            "Make name",
            copy_name,
            default = True,
            visible = False
        )
    )
)

tray_icon.run()