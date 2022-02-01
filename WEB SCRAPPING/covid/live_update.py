from requests_html import HTML
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
import time

options =Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
url = 'https://www.google.com/search?q=covid+cases+in+india&oq=covid&aqs=chrome.0.69i59l3j0i131i433i512l2j69i60l2j69i61.1702j0j7&sourceid=chrome&ie=UTF-8'
driver.get(url)
time.sleep(1)

body_el = driver.find_element_by_css_selector("body")
html_str = body_el.get_attribute("innerHTML")
html_obj = HTML(html = html_str)

date = html_obj.find('.c274Wb')
for i in date:
    print(i.text)
new_cases = html_obj.find('.GxwVnb')
for j in new_cases:
    #ab = j.find('span')
    ab = j.find('span')
    print(ab[0].text+ ab[1].text + ab[2].text)
    print(ab[3].text+ ab[4].text + ab[5].text)    