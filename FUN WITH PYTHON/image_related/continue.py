import pyautogui as pt
from time import sleep
from faker import Faker
ab = Faker()
sleep(2)
for i in range(100):
    pt.moveTo(596,694)
    pt.click()
    pt.typewrite(ab.address())
    pt.press('enter')