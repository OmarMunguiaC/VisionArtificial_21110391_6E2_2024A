"""
Práctica 2: Clasificador
"""
import cv2
import numpy as np

imagen=cv2.imread('imagen1.jpg')
m,n,c=imagen.shape

#Clasificador
imagen_bn=np.zeros((m,n))
for x in range(m):
    for y in range(n):
        if 26<imagen[x,y,0]<195 \
            and 36<imagen[x,y,1]<192 \
                and 51<imagen[x,y,2]<207:
                    imagen_bn[x,y]=255

cv2.imshow('Original',imagen)
cv2.imshow('Blanco y negro',imagen_bn)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('imagen_bn.jpg',imagen_bn)
