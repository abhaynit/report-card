import os
path_to_data = "C:/Users/abhay/Pictures/desired/shoe/"
result = []
for entry in  os.scandir(path_to_data):
    print(entry.path)
    ab = entry.path
    print('media/'+ ab.split('/')[-1])