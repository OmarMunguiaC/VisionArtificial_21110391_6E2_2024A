"""
Práctica 4: White patch
"""
import cv2
import numpy as np

imagen1=cv2.imread('imagen1.jpg')
m,n,c=imagen1.shape
imagencolor1=imagen1.copy()
imagencolor2=imagen1.copy()
imagencolor3=imagen1.copy()

def Clasificador(imagen):
    imagenb1=np.zeros((m,n))
    for x in range(m):
        for y in range(n):
            if 26<imagen[x,y,0]<195 \
                and 36<imagen[x,y,1]<192 \
                    and 51<imagen[x,y,2]<207:
                        imagenb1[x,y]=255
    return imagenb1

def ClasificadorA(imagen):
    imagenb2=np.zeros((m,n))
    for x in range(m):
        for y in range(n):
            if 35<imagen[x,y,0]<245 \
                and 42<imagen[x,y,1]<237 \
                    and 58<imagen[x,y,2]<245:
                        imagenb2[x,y]=255
    return imagenb2

def WhitePatch(imagen):
    imagenc=imagen1.astype(float)
    whiteP=np.zeros((m,n,c))
    b=np.max(imagenc[:,:,0])
    g=np.max(imagenc[:,:,1])
    r=np.max(imagenc[:,:,2])
    for x in range(m):
       for y in range(n):
             whiteP[x,y,0]=(255/b)*imagenc[x,y,0]
             whiteP[x,y,1]=(255/g)*imagenc[x,y,1]
             whiteP[x,y,2]=(255/r)*imagenc[x,y,2]      
    whiteP=whiteP.astype(np.uint8)
    return whiteP

imagencolor1[:,:,0]=imagencolor1[:,:,0]+50
imagencolor2[:,:,1]=imagencolor2[:,:,1]+50
imagencolor3[:,:,2]=imagencolor3[:,:,2]+50

wp1=WhitePatch(imagen1)
wp2=WhitePatch(imagencolor1)
wp3=WhitePatch(imagencolor2)
wp4=WhitePatch(imagencolor3)
clA1=Clasificador(wp1)
clA2=Clasificador(wp2)
clA3=Clasificador(wp3)
clA4=Clasificador(wp4)
clB1=ClasificadorA(wp1)
clB2=ClasificadorA(wp2)
clB3=ClasificadorA(wp3)
clB4=ClasificadorA(wp4)

cv2.imwrite('imagencolor1.jpg',imagencolor1)
cv2.imwrite('imagencolor2.jpg',imagencolor2)
cv2.imwrite('imagencolor3.jpg',imagencolor3)

cv2.imwrite('imagenWP1.jpg',wp1)
cv2.imwrite('imagenWP2.jpg',wp2)
cv2.imwrite('imagenWP3.jpg',wp3)
cv2.imwrite('imagenWP4.jpg',wp4)

cv2.imwrite('imagenA_c1.jpg',clA1)
cv2.imwrite('imagenA_c2.jpg',clA2)
cv2.imwrite('imagenA_c3.jpg',clA3)
cv2.imwrite('imagenA_c4.jpg',clA4)

cv2.imwrite('imagenB_c1.jpg',clB1)
cv2.imwrite('imagenB_c2.jpg',clB2)
cv2.imwrite('imagenB_c3.jpg',clB3)
cv2.imwrite('imagenB_c4.jpg',clB4)

cv2.imshow('imagen original',imagen1)
cv2.imshow('color 1',imagencolor1)
cv2.imshow('color 2',imagencolor2)
cv2.imshow('color 3',imagencolor3)
cv2.imshow('white patch 1',wp1)
cv2.imshow('white patch 2',wp2)
cv2.imshow('white patch 3',wp3)
cv2.imshow('white patch 4',wp4)
cv2.imshow('clasificador 1',clA1)
cv2.imshow('clasificador 2',clA2)
cv2.imshow('clasificador 3',clA3)
cv2.imshow('clasificador 4',clA4)
cv2.imshow('clasificador ajustado 1',clB1)
cv2.imshow('clasificador ajustado 2',clB2)
cv2.imshow('clasificador ajustado 3',clB3)
cv2.imshow('clasificador ajustado 4',clB4)

cv2.waitKey()
cv2.destroyAllWindows()
