import time
import pyautogui
print(pyautogui.size())

def posit():
    print(pyautogui.position())

pyautogui.moveTo(x=1266,y=12 ,duration=0)
pyautogui.click()
pyautogui.moveTo(x=341,y=324 ,duration=2)
pyautogui.doubleClick()
time.sleep(2)
pyautogui.moveTo(x=180,y=56 ,duration=2)
pyautogui.click()

pyautogui.typewrite("https://www.irctc.co.in/nget/train-search")
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)

"""
pyautogui.moveTo(x=780,y=456 ,duration=1)
pyautogui.click()
time.sleep(1)
pyautogui.scroll(-2000)
pyautogui.moveTo(x=700,y=656 ,duration=1)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(x=350,y=126 ,duration=1)
pyautogui.click()
time.sleep(2)

"""



