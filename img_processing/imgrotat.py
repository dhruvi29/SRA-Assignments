from PIL import Image as im
import numpy as np

img=im.open("rotate.png")
img=img.rotate(90,expand=True)
img=img.rotate(180,expand=True)
img.show()