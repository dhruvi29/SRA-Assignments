import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image as im
import math


img=im.open("SRA-Assignments/img_processing/edge-detection.png")
hexme=np.array(img)
h,w,c=hexme.shape
# print(hexme)

def gray_me(hexme):
    gray=np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            gray[i,j]=0.3*hexme[i,j,0]+0.59*hexme[i,j,1]+0.11*hexme[i,j,2]
    return gray

def apply_kernel(kernel,img):
    print(kernel)
    local=np.zeros((3,3),img.dtype)
    h,w=img.shape
    for i in range(3,h-3):
        for j in range(3,w-3):
            local=img[i-1:i+2,j-1:j+2]
            kernel=local*kernel
            print(kernel)
            kernel=np.sum(kernel,axis=0)
            kernel=np.sum(kernel,axis=0)
            if(kernel<0):kernel=0
            elif(kernel>255):kernel=255
            img[i,j]=kernel
            
    # img=img/img.max()*255
    return img

img=gray_me(hexme)
kernel=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
img=apply_kernel(kernel,img)
# hexme=vertical_edge(hexme)
# hexme=horizontal_edge(hexme)
# hexme=sobel_edge(hexme)
# hexme=gray_me(hexme)
# hexme=weighted_filter(hexme)
po = im.fromarray(img)
im._show(po)