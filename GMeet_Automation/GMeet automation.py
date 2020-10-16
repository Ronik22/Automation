# Script to automate google meet login

import webbrowser
import time
import pyautogui as pyg

meet_id = input("\nEnter meeting id or url: ")
gmail = input("Enter the email address which you want to use to join the meeting [Press Enter to skip and select default]: ")

if (gmail==""):
    if (meet_id.startswith("https:")):
        target_url = meet_id
    else:
        target_url = f"https://meet.google.com/{meet_id}"
else:
    if (meet_id.startswith("https:")):
        target_url = f"{meet_id}?authuser={gmail}"
    else:
        target_url = f"https://meet.google.com/{meet_id}?authuser={gmail}"

webbrowser.open(target_url)
time.sleep(5)

pyg.hotkey('ctrl','d')  # to mute the mic
pyg.hotkey('ctrl','e')  # to turn off the video
time.sleep(3)

pyg.press('tab',presses=6)

time.sleep(1)
pyg.press('enter')
print("Meeting joined")
