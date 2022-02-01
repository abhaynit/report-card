path_to_data = "C:/Users/abhay/Pictures/desired/laptop/"
path_to_cr_data = "C:/Users/abhay/Pictures/desired"

import os

# SCAN THE DIRECTORY AND THE FOLDER INSIDE THEM
"""
img_dirs = []
for entry in os.scandir(path_to_data):
    if entry.is_dir():
        img_dirs.append(entry.path)
print(img_dirs)
"""

# REMOVE FOLDER IF PRESENT AND ADD 
"""
import shutil 
if os.path.exists(path_to_cr_data):
    shutil.rmtree(path_to_cr_data)
os.mkdir(path_to_cr_data)
"""

result = []
for entry in  os.scandir(path_to_data):
    c='/'
    ab = entry.path.split('/')
    #print(entry.path.split('/'))
    result.append(c.join(ab))

print(result)



