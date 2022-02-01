from requests_html import HTML
from selenium import  webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

options =Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
url = 'https://dashboard.cowin.gov.in/'
driver.get(url)
time.sleep(1)
"""
nit = driver.find_element_by_id("state")
drp = Select(nit)
drp .select_by_visible_text('Bihar')

elem = driver.find_element_by_id("district")
el1 = Select(elem)
el1.select_by_visible_text('Begusarai')

time.sleep(2)
"""
body_el = driver.find_element_by_css_selector("body")
html_str = body_el.get_attribute("innerHTML")
html_obj = HTML(html = html_str)

# TOTAL REGISTRATION AND VACCINATION TODAY
de = html_obj.find('strong')
for i in de:
    print(i.text)

print()
#LIST OF THE TOAL DOES
abc = html_obj.find('h3')
count =0
for i in abc:
    print(i.text)
    count+=1
    if count==3:
        break
print()
rty = html_obj.find('p')
for i in rty:
    print(i.text)
"""
body_el = driver.find_element_by_css_selector("body")
html_str = body_el.get_attribute("innerHTML")
html_obj = HTML(html = html_str)


de = html_obj.find('table')
for i in de:
    ke = html_obj.find('tr')
    for j  in ke:
        vb = j.find('td')
        for p in vb:
            print(p.text,end=' ')
        print()
        """