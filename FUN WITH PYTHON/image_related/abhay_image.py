import cv2
import os
abhay = cv2.imread('2.jpeg',0)
simi = cv2.resize(abhay,(400,256))
cv2.imshow('aadhar',simi)
cv2.imwrite('front.jpeg',simi)
cv2.waitKey(0)