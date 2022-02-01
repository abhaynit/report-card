f=open("restaurant_item.txt",'r')
s=f.read()

import json
book = json.loads(s)
# the type of the book will be dictionary
print(type(book))
lis1=[]

for i in book:
   print(i,book.get(i))

