import cv2
import numpy as np


imgString = "img.png"

img = cv2.imread(imgString,0)
print(len(img))
print(img.shape)
h = img.shape[0]
w = img.shape[1]


img = img.reshape(w, h)
print(img.shape)

cv2.imshow ( 'image' , img)

cv2.waitKey(0)
cv2.destroyAllWindows()
