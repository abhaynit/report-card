import time
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
import  random
from selenium.webdriver.common.by import  By


driver = webdriver.Chrome(executable_path=(r"C:\Users\abhay\Downloads\chromedriver_win32\chromedriver.exe"))


driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button").click()
driver.find_element_by_xpath("//*[@id='origin']/span/input").send_keys("NEW DELHI - NDLS")
driver.find_element_by_xpath("//*[@id='destination']/span/input").send_keys("KOLKATA - KOAA")
driver.find_element_by_xpath("//*[@id='jDate']/span/input").click()
driver.find_element_by_xpath("//*[@id='jDate']/span/div/div/div[2]/table/tbody/tr[4]/td[6]/a").click()
driver.find_element_by_xpath("//*[@id='divMain']/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div/button").click()

time.sleep(10)
flag = driver.find_element_by_xpath("//*[@id='divMain']/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[1]/div[5]/div/table/tr/td[2]/div")
driver.execute_script("arguments[0].scrollIntoView();",flag)
flag.click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='divMain']/div/app-train-list/div[4]/div/div[5]/div[1]/div[1]/app-train-avl-enq/div[2]/div/span/span/button[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='divMain']/div/app-train-list/p-confirmdialog[1]/div/div/div[3]/button[1]/span[2]").click()
driver.find_element_by_xpath("//*[@id='divMain']/div/app-train-list/p-confirmdialog[2]/div/div/div[3]/button[1]/span[2]").click()
driver.find_element_by_xpath("//*[@id='userId']").send_keys("abhay")
driver.find_element_by_xpath("//*[@id='pwd']").send_keys("aman")

