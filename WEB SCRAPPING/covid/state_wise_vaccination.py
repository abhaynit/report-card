import requests
from requests_html import HTML
from selenium import  webdriver
from selenium.webdriver.support.ui import Select #this is for drop down menu
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
url = 'https://www.mygov.in/covid-19'
driver.get(url)
time.sleep(2)
driver.find_element_by_id('statewise-data').click()

time.sleep(2)

body_el = driver.find_element_by_css_selector('body')
html_str = body_el.get_attribute('innerHTML')
html_obj = HTML(html=html_str)

state_wise_vaccine = []
heading = []
aa = html_obj.find('table')
count = 0
print(len(aa))
for i in range(0,len(aa)):
    bb = aa[i].find('tr')
    for p in range(0,1):
        cc = bb[p].find('th')
        abbb = []
        for k in cc:
            print(k.text,end=" ")
            abbb.append(k.text)
        heading.append(abbb)
        print()
    for j in range(1,len(bb)): #for j in range(1,len(bb)):
        cc = bb[j].find('td')
        abbb = []
        #print(cc[0].text,end=" ")
        abbb.append(cc[0].text)
        for k in range(1,4):
            xxxx = cc[k].text
            yyyy = 0
            for y in cc[k].find('.data-up'):
                #print(y.text,end=' ')
                yyyy = y.text
            #ky = xxxx[:xxxx.find(yyyy)]+'/_/'+yyyy
            # if we want only initail data not todays data
            ky = xxxx[:xxxx.find(yyyy)]
            #print(ky,end=" ")
            abbb.append(ky)
        #print(cc[4].text)
        abbb.append(cc[4].text)
        state_wise_vaccine.append(abbb)
        #print()
    count+=1
    if count==1:
        break

qqq = pd.DataFrame(state_wise_vaccine,columns=heading)
qqq.to_csv('state_wise_vaccination_list.csv',index=False)