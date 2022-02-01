import cv2
import os
if os.path.exists(r'E:\abhay\shopping_website_image'):
    pass
else:
    for i in os.scandir(r'c:\users\abhay\pictures\desired'):
        os.makedirs(r'E:\abhay\shopping_website_image' +'\\' +  i.path.split('\\')[-1])
for i in os.scandir(r'c:\users\abhay\pictures\desired'):
    name , count = (i.path.split('\\')[-1]) ,1
    for k in os.scandir(i):
        abhay = cv2.imread(k.path)
        simi = cv2.resize(abhay,(256,256))
        final_path = (r'E:\abhay\shopping_website_image'+'\\'+i.path.split('\\')[-1]+ '\\' + name+str(count)+'.jpg')
        cv2.imwrite(final_path,simi)
        count+=1