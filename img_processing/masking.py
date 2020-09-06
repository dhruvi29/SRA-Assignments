import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image as im
import math

hsv=cv.imread("SRA-Assignments/img_processing/mask.jpg",1)
# hexme=np.array(img)
h,w,c=hsv.shape
kent=np.zeros_like(hsv)
# print(hsv.shape)
hsv=cv.cvtColor(hsv,cv.COLOR_BGR2HSV)
for i in range(h):
    for j in range(w):
        if(hsv[i,j,0]>90 and hsv[i,j,0]<130 and  hsv[i,j,1]>50 and hsv[i,j,2]>50):
            kent[i,j]=hsv[i,j]



img=cv.cvtColor(kent,cv.COLOR_HSV2BGR)
cv.imshow("heyya",img)
key=cv.waitKey(1000000)
if(key==27):
    cv.destroyAllWindows()