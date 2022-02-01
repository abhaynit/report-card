import requests
import bs4
import shutil

pat = "E:\ALL\PYTHON\BEST\top_wear"
url = "https://www.amazon.com/s?k=laptop&ref=nb_sb_noss"
response = requests.get(url)

htmlcontent = response.content

soup = bs4.BeautifulSoup(htmlcontent,'html.parser')
ab = soup.find_all('img')
print(len(ab))



count = 1000
for i in ab:
    a = i.get('src')
    abc = str(a)
    if abc.startswith("https:"):
        #filen = str(count)+'.jpg'
        #res = requests.get(a,stream=True)
        #with open(filen,'wb') as file:
        #    shutil.copyfileobj(res.raw,file)
        count +=1
print(count)
