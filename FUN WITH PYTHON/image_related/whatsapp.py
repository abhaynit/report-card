import pyautogui as pt
from time import sleep
import pyperclip
import random


sleep(2)



#getsmessage
def get_message():
    #global x,y
    position = pt.locateOnScreen("gg.png",confidence = .9)
    #print(position)
    sleep(1)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y,duration=.05)
    pt.click()
    while True:
        if pt.pixel(510,641)==(255,255,255):
            pt.moveTo(510,641,duration=.05)
            pt.tripleClick()
            pt.rightClick()
            pt.moveTo(579,517)
            pt.click()
            print("the received message is : ",pyperclip.paste())
            pt.moveTo(596,694)
            pt.click()
            pt.typewrite(pyperclip.paste())
            pt.press('enter')
            sleep(1)
        else:
            sleep(1)
   


get_message()

"""
while True:
    posXY = pt.position()
    print(posXY, pt.pixel(posXY[0],posXY[1]))
    sleep(1)
    if posXY[0]==0:
        break
"""