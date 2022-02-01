import  requests
from requests_html import HTML
from selenium import  webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

#open the site
options =Options()
options.add_argument("--headless")
driver = webdriver.Chrome('C:/Users/abhay/Downloads/chromedriver_win32/chromedriver.exe',options=options)
url = 'https://dashboard.cowin.gov.in/'
driver.get(url)
time.sleep(4)
#site open complete

nit = driver.find_element_by_id("state")
drp = Select(nit)
drp .select_by_visible_text('Bihar')

elem = driver.find_element_by_id("district")
el1 = Select(elem)
el1.select_by_visible_text('Samastipur')

time.sleep(2)

#data set
body_el = driver.find_element_by_css_selector("body")
html_str = body_el.get_attribute("innerHTML")
html_obj = HTML(html = html_str)
de = html_obj.find('table')
list_wise =[]
for i in de:
    ke = html_obj.find('tr')
    for j  in ke:
        vb = j.find('td')
        aaa = []
        for p in vb:
            #print(p.text,end=' ')
            aaa.append(p.text)
        list_wise.append(aaa)
        #print()

#data set complete
list_wise.sort()
import pandas as pd
df = pd.DataFrame(list_wise,columns=['state','today','total'])
df.to_csv('Bihar_Samastipur_vaccination_report.csv',index=False)