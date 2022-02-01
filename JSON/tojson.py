item = [
        ['Rajma Chawal', 26],
        ['Momos' ,25,],
        ['Egg Curry',90],
        ['Litti Chokha',10],
        ['Chhole Kulche',20],
        ['Dosa', 50],
        ['Thukpa',45],
        ['Vada Pao',10]
       
    ]

book= dict(item)


import json
# here i have written dumps because we have to dump is as string
s = json.dumps(book)
print(s)
with open('restaurant_item.txt','w') as f:
    f.write(s)