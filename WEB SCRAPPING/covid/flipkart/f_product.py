from requests_html import HTML
from selenium import  webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

options =Options()
options.add_argument("--headless")
driver = webdriver.Chrome('C:/Users/abhay/Downloads/chromedriver_win32/chromedriver.exe',options=options)

url = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
driver.get(url)
time.sleep(1)



body_el = driver.find_element_by_css_selector("body")
html_str = body_el.get_attribute("innerHTML")
html_obj = HTML(html = html_str)

# TO GET THE DETAIL OF THE PRODUCT:
de = html_obj.find('._1fQZEK')

for i in de:
    print(i.text) 
    print()
    print()