import requests
import bs4
import shutil

url = "https://www.bollywoodhungama.com/photos/first-look/"
response = requests.get(url)
#if status_code is 200 then its successful
print(response.status_code)

#response.content gives the value of the whole html page
htmlcontent = response.content
#parese the html content such that we can use them
soup = bs4.BeautifulSoup(htmlcontent,'html.parser')
ab = soup.find_all('img', attrs={'class':'attachment-bh_255_auto size-bh_255_auto'})
count = 1
for i in ab:
    res = requests.get(i.get('src'),stream=True)
    with open('abhay_image_'+str(count)+'.jpg','wb') as f:
        shutil.copyfileobj(res.raw,f)
    count+=1