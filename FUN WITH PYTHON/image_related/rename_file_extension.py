import os
pa = "E:/ALL/PYTHON/BEST/maria sharapova"

j=1
for i in os.scandir(pa):
    ab = i.path.split('\\')
    ac = ab[0]+ str(j)+'.jpg'
    os.rename(i,ac)
    j+=1
    