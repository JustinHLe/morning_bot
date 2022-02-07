import os #used for operating system functionality
import pyautogui
from time import sleep
import sys
from datetime import datetime
import subprocess
import psutil
import pygetwindow as gw  


pyautogui.FAILSAFE = False

now = datetime.now()
current_date = int(now.strftime("%w"))
current_time = int(now.strftime("%H%M%S"))

if 70000 <= current_time <= 80100:
    sleep(60)

opened = False
#check if teams is open
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        if(processName == "Teams.exe"):
            print("found team process")
            opened = True
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass


desktop_path = "C:/Users/Justin/Desktop"
# Open teams
if (opened):
    subprocess.call(r'C:\Users\Justin\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe"')
    sleep(6)
else:
    subprocess.call(r'C:\Users\Justin\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe"')
    sleep(20)
    win = gw.getWindowsWithTitle('Microsoft Teams')[0] 
    win.minimize()
    win.maximize()

#move to search bar
pyautogui.keyDown("ctrl")
pyautogui.press("e")
pyautogui.keyUp("ctrl")

sleep(1)


#enter query
pyautogui.typewrite("UI Development")
sleep(6)
pyautogui.keyDown("down")
pyautogui.keyDown("enter")
pyautogui.keyUp("down")
pyautogui.keyUp("enter")


#move to text bar
pyautogui.keyDown("alt")
pyautogui.keyDown("shift")
pyautogui.keyDown("c")

pyautogui.keyUp("alt")
pyautogui.keyUp("shift")
pyautogui.keyUp("c")

# 0 sunday
# 1 Monday
# 2 Tues
# 3 Wedn
# 4 Thurs
# 5 Fri
print("current time " + str(current_time))
print("current  date " + str(current_date))

if current_date == 1 or current_date == 4 or current_date == 5:
    if 164500 <= current_time <= 170100:
        if current_date == 5:
            pyautogui.typewrite("Have a good weekend!")
        else:
            pyautogui.typewrite("Good night!")
        pyautogui.typewrite(["enter"])
        sleep(1)
        os.system("TASKKILL /F /IM Teams.exe")
        sys.exit()

    if 70000 <= current_time <= 80100:
        print("Morning")
        if current_date == 5:
            pyautogui.typewrite("Happy Friday!")
        else:
            pyautogui.typewrite("Good Morning!")
        pyautogui.typewrite(["enter"])
        sys.exit()
    
    print("Not Correct Time")
else:
    print("Not Correct Date")
    sys.exit()


