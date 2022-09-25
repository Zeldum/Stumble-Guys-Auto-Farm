#Trophy AutoFarm, not Crown
#Crown = Wins
#Thophies = Participation Reward

#Packages: opencv-python, pillow, pyautogui

import pyautogui as pt
from time import sleep
import time

#Helper Function:
def nav_to_image(image, clicks, off+x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=0.7)

    if position is None:
        print(f'{image} not found...')
        return 0
    else:
        pt.moveTo(position, duration=0.1)
        pt.moveRel(off_x, off_y, duration=0.1)
        pt.click(clicks=clicks, interval=0.3)




#Moves The Character
# x = Attack
# c = Place

#pt.moveTo(1700,968)           ;           PLAY BUTTON



def locate_button():
    position = pt.locateCenterOnScreen("Code\Stumble Guys.py\Images\PlayButton.PNG, confidence = 0.8"):
    
    if position is None:
        return False
    else:
    