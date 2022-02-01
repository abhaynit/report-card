import time
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import  random


driver = webdriver.Chrome(executable_path=(r"C:\Users\abhay\Downloads\chromedriver_win32\chromedriver.exe"))

driver.get("http://127.0.0.1:8000/admin/")
driver.find_element_by_name("username").send_keys("abhay")
driver.find_element_by_name(("password")).send_keys("1234")
driver.find_element_by_xpath("//*[@id='login-form']/div[3]/input").click()



"""
driver.find_element_by_xpath("//*[@id='content-main']/div[2]/table/tbody/tr[1]/th/a").click()
driver.find_element_by_xpath("//*[@id='content-main']/ul/li/a").click()

cit = ["patna","kolkata","delhi","bombay","dimapur","jaipur","kohima","guwahati"]


for iwe in range(10):
    ele = driver.find_element_by_xpath("//*[@id='id_user']")
    drp = Select(ele)
    drp.select_by_visible_text('aman')
    driver.find_element_by_name('city').send_keys(random.choice(cit))
    driver.find_element_by_name('state').send_keys('bihar')
    driver.find_element_by_name('zip_code').send_keys("803202")
    driver.find_element_by_name('street').send_keys('kankarbagh')
    driver.find_element_by_name('mobile').send_keys('8581931941')
    driver.find_element_by_xpath("//*[@id='addressed_form']/div/div/input[2]").click()

"""
path_to_data = "C:/Users/abhay/Pictures/desired/laptop/"

import os
result = []
for entry in  os.scandir(path_to_data):
    c='/'
    ab = entry.path.split('/')
    #print(entry.path.split('/'))
    result.append(c.join(ab))
driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[5]/th/a').click()
driver.find_element_by_xpath("//*[@id='content-main']/ul/li/a").click()



for i in range(len(result)):
    driver.find_element_by_name("iname").send_keys("laptop"+str(i+1))
    ele = driver.find_element_by_xpath("//*[@id='id_itype']")
    drp = Select(ele)
    drp.select_by_visible_text("Laptop")
    driver.find_element_by_name("price").send_keys(str(random.randint(100,10000)))
    driver.find_element_by_id("id_pic").send_keys(result[i])
    driver.find_element_by_xpath("//*[@id='items_form']/div/div/input[2]").click()


