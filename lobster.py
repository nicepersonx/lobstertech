import keyboard
import win32api, win32con
import time
import colored
import requests
import time
import pyautogui
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

pink = colored.fg(205)
white = colored.fg(15)
black = colored.fg(0)
print(pink + "Lobstertech active")
print(""""###############################################################################################
###########################%&@%#####################################################################
########################%&####%@%###################################################################
#######################%#######%&###################################################################
###############################%&%#########%@@@@@@@%%@@@@%######%#########%%%%%#####################
##########################%%%@@&&%@@@%#%#%@@&&%##%@%%&@@@@@@&%@@@@%@@@@&@@@@&%%@@@@&%###############
#####################%&@@@@@@%@&&%@@@@&@@@@%#%%%&@@@@@@@@@@@@@@%@@@@%@@@@%@@@&@@@%@@@@@%############
###################&@@@@@@@@@&&&&%@@@%&&@@@@@@@@@@@@&@@@@@@@@@@@%@@@&&@@@@&@@@&@@@&&@@@@&###########
#################&@@@@@@@@@@@&&%@%&&@@@@@@@@@@@@@@@@@&@@@@@@@@@@@%@@@%@@@@%@@@&@@&&@@@@@@@&%########
###############%@@@@@@@@@@@@@@%###%%&@@@@%%@@@@@@@@@@&@@@@@@@@@@@%@%%%@@@@%@@@%####%&@@@@@@%########
###############@@@@@@@@@@@@@@@%#%&@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@%@@@&#%&###########################
##############@@@@@@@@@@@@@@@@%###&@@@@&@&%%%%%&&&%%%%&&@@@@@@@%@@@@@@%@@@&#########################
#############%@@@@@@@@@@@&@@@@%###@&%%@@@%%&%&&@@&&&&%%%%&@@@@&&%%%&@@#%&@@@%#######################
##############@@@@@@@@@@#%@@@%###%@%######%@@@@@&@@@&%@@@@@@@@@%%%@@@@%###%@&#######################
###############@@@@@@@&&#@@@%#######%%&%%############%%%%%%&@@@@@%#%&&#%&&&&&%##%###################
################%@@@@@@%&%######################%&@@@@@@@@@@@@&%@&#%@@######%@&#####################
####################%%%############&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#%@@#######%@%####################
################################&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%##################################
##############################&@@@&&&%%&&@@@@@@@@@@@@@@@@@@@@@@@%###################################
#############################%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#####################################
###############################&@@@@@@@@@@@@@@@@@@@@@@@@@@&%########################################
##################################%&@@@@@@@@@@@@@@@@&%%#############################################
##########################################%%%#######################################################""".replace('@',pink+"@"+black).replace('%',pink+'%'+black))

while 1:
    # if keyboard.is_pressed('space') == True:
    #     response = requests.get("https://127.0.0.1:2999/liveclientdata/activeplayer", verify=False)
    #     attackspeed = float((response.json()['championStats']['attackSpeed']))
    #     windup = 0.032
    #     ping = 0.048
    #     movefactor = 0.89
    #     if attackspeed > 3.7:
    #         movefactor = 0.62
    #         windup = 0.042
    #     # windup = 0.032
    #     # ping = 0.048
    #     # movefactor = 0.62
    #     # if attackspeed > 3.2:
    #     #     movefactor = 0.54
    #     #     windup = 0.022
    #     #     attackspeed=attackspeed*0.92 JINX
    #     keyboard.press('c')
    #     win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    #     time.sleep((((1/attackspeed)*movefactor)-ping-0.097))
    #     try:
    #         x = pyautogui.locateOnScreen('hp.png', confidence=0.99, grayscale=True, region=(220,110,1115,817))
    #         resetto = win32api.GetCursorPos()
    #         win32api.SetCursorPos((x[0] + 47, x[1]+120))
    #         win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
    #         time.sleep(0.002)
    #         win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0)
    #         time.sleep(0.002)
    #         win32api.SetCursorPos(resetto)
    #         time.sleep((1/attackspeed)*0.19+windup - 0.01)
    #     except:
    #         print("No target found")
    #     if keyboard.is_pressed('space') == False:
    #         keyboard.release('c')

    if keyboard.is_pressed('space') == True:
        response = requests.get("https://127.0.0.1:2999/liveclientdata/activeplayer", verify=False)
        attackspeed = float((response.json()['championStats']['attackSpeed']))
        windup = 0.032
        ping = 0
        movefactor = 0.70
        attackspeed=attackspeed*0.98
        keyboard.press('c')
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        time.sleep(((((1/attackspeed)*movefactor)-ping)))
        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0)
        time.sleep((1/attackspeed)*0.19+windup - 0.001)
        if keyboard.is_pressed('space') == False:
            keyboard.release('c')
