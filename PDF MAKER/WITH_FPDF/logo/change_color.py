import cv2 
import matplotlib.pyplot as plt

img = cv2.imread('./logo/pen.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# create a copy of the original image
img_rgb = img.copy()

# extract blue channel of the rgb image
b = img_rgb[:,:,2] 

# increase the pixel values by 100
b = b + 100    

# if pixel values become > 255, subtract 255 
cond = b[:, :] > 255
b[cond] = b[cond] - 255 

# assign the modified channel to image
img_rgb[:,:,2] = b 

plt.imshow(img_rgb)