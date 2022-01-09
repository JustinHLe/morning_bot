import os #used for operating system functionality
import pyautogui
from time import sleep
import sys
from datetime import datetime

# Open teams
desktop_path = "C:/Users/Justin/Desktop"
os.startfile(desktop_path + '/Microsoft Teams.lnk')
sleep(6)

#full screen
pyautogui.keyDown("win")
pyautogui.press("up")
pyautogui.keyUp("win")

sleep(1)
pyautogui.moveTo(600,20)
pyautogui.click()

#search for dm
pyautogui.typewrite("Le, Justin H. (EL)")
sleep(1)
pyautogui.moveTo(600,150)
pyautogui.click()

#get search bar
pyautogui.moveTo(750,975)
pyautogui.click()

now = datetime.now()
current_time = int(now.strftime("%H%M%S"))
#5 is friday
current_date = int(now.strftime("%w"))

print("current time " + str(current_time))
print("curren date " + str(current_date))

if 170000 <= current_time <= 170100:
    if current_date == 5:
        pyautogui.typewrite("Have a good weekend!")
    else:
        pyautogui.typewrite("Good Night!")
    pyautogui.typewrite(["enter"])
    sleep(1)
    os.system("TASKKILL /F /IM Teams.exe")
    sys.exit()

if 80000 <= current_time <= 80100:
    if current_date == 5:
        pyautogui.typewrite("Happy Friday!")
    else:
        pyautogui.typewrite("Good Morning!")
    pyautogui.typewrite(["enter"])
    sys.exit()


