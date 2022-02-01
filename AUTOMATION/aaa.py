path_to_data = "C:/Users/abhay/Pictures/desired/laptop/"
awe =[]
import os
for i in os.scandir(path_to_data):
    print(i.path)
    awe.append('c://ankit/abhay/abhinav/' + i.path.split('/')[-1])

print(awe)
