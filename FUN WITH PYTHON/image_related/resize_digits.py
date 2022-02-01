import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("four.jpeg", 1)
# Loading the image

half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(image, (1050, 1610))

stretch_near = cv2.resize(image, (780, 540),
			interpolation = cv2.INTER_NEAREST)
req_img = cv2.resize(image,(8,8))

final_path = (r'E:\abhay'+'.jpeg')
cv2.imwrite(final_path,req_img)
Titles =["Original", "Half", "Bigger", "Interpolation Nearest","requrired"]
images =[image, half, bigger,req_img, stretch_near]
count = 4
for i in range(count):
	plt.subplot(2, 2, i + 1)
	plt.title(Titles[i])
	plt.imshow(images[i])

plt.show()
