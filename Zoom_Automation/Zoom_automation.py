# Script to automate zoom login for unsigned users
# zoom should be installed on pc

import time
import pyautogui as pyg
import webbrowser

zoom_id = input("\nEnter zoom id or url: ")

if (zoom_id.startswith("https:")):
    webbrowser.open(zoom_id)
    time.sleep(5)
    pyg.press('tab',presses=2)
    time.sleep(1)
    pyg.press('enter')
else:
    zoom_pwd = input("Enter zoom password: ")
    name = input("Enter your name: ")

    time.sleep(0.5)

    pyg.press('win',interval=0.5)
    pyg.write('zoom')
    pyg.press('enter',interval=0.5)

    time.sleep(4)
    pyg.press('tab')
    pyg.press('enter')
    time.sleep(8)

    pyg.write(zoom_id)
    pyg.press('tab',presses=2)

    pyg.hotkey('ctrl','a')
    pyg.press('backspace')  # to remove existing name and enter a new name
    pyg.write(name)

    pyg.press('tab',presses=3)
    pyg.press('enter')      # to turn off the video
    pyg.press('tab')
    time.sleep(5)
    pyg.press('enter')

    time.sleep(5)
    pyg.write(zoom_pwd)
    pyg.press('tab')
    time.sleep(2)
    pyg.press('enter')

print("Meeting joined")
