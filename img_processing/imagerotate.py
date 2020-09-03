import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image as im
import math

img=im.open("rotate.png")
hexme=np.array(img)
h,w,c=hexme.shape
don=np.zeros((h+500,w+500,c),dtype=np.uint8)
radians=math.pi/180*input("enter your angle")
c, s = math.cos(radians), math.sin(radians)
lol = np.array([[c, -s], [s, c]])
for i in range(h):
    if(radians==math.pi):
        don=hexme[::-1]
        break
    for j in range(w):
        n=np.array([i-h/2,j-w/2]).reshape(2,1)
        m=np.dot(lol,n)
        x,y=int(m[0]+(h/2)),int(m[1]+(h/2))
        # don[i,j]=hexme[i,j]
        if(x>=0 and y>=0 and x<822 and y<1100):
            don[x,y]=hexme[i,j]
po = im.fromarray(don)
im._show(po)
# print(don)
