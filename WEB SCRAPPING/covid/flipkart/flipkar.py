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


"""
final_list = []
def result(url):
    driver.get(url)
    time.sleep(2)
    body_el = driver.find_element_by_css_selector("body")
    html_str = body_el.get_attribute("innerHTML")
    html_obj = HTML(html = html_str)
    de = html_obj.find('._1fQZEK')

    for i in de:
        abhay = []
        aa = i.find('._4rR01T')
        bb = i.find('._30jeq3')
        for j in aa:
            #print(j.text) 
            abhay.append(j.text)
        for k in bb:
            #print(k.text)
            abhay.append(k.text[1:])
            final_list.append(abhay)
    #print(final_list)

    
def create_csv():
    final_list.sort(key=lambda x :x[1])
    import pandas as pd
    abc = pd.DataFrame(final_list,columns=['mobile_name','price'])
    abc.to_csv('flipkart_laptop.csv',index=False)



#this url is for laptop
result('https://www.flipkart.com/search?q=lap&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
time.sleep(3)
for qq in range(2,30):
    try:
        ww = 'https://www.flipkart.com/search?q=lap&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' + str(qq)
        result(ww)
        print('couting value',qq)
        time.sleep(1)
    except:
        continue

create_csv()

"""
"""
#this url is for mobile
#result('https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
for qq in range(2,40):
    try:
        ww = 'https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' + str(qq)
        result(ww)
    except:
        continue

create_csv()
"""





# TO GET THE DETAIL OF THE PRODUCT:
de = html_obj.find('._1fQZEK')

for i in de:
    print(i.text) 
    print()
    print()
