import faker 
import pyautogui
import random
import time
from faker import Faker

fake = Faker()
def posit():
    print(pyautogui.position())

#print(fake.name())

pyautogui.moveTo(x=1266,y=12 ,duration=0)
pyautogui.click()
for i in range(500):
    pyautogui.moveTo(x=530,y=699 ,duration=.1)
    pyautogui.click()
    pyautogui.typewrite(fake.address())
    pyautogui.press('enter')
