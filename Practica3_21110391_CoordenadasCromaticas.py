"""
Práctica 3: Coordenadas Cromaticas
"""

import cv2
import numpy as np

imagen=cv2.imread('imagen1.jpg')
imagen=imagen.astype(np.float32)
m,n,c=imagen.shape
imagen2=imagen*0.8
imagen2=imagen2.astype(np.float32)
imagen3=imagen*0.5
imagen3=imagen3.astype(np.float32)

cv2.imwrite('imagen2.jpg',imagen2)
cv2.imwrite('imagen3.jpg',imagen3)

def cCromaticas(imagen):
    imagen_c = imagen
    imagenCromatica = np.zeros((m,n,c))
    imagen_c=imagen_c.astype(np.float64)
    for z in range(c): 
     for x in range(m):
       for y in range(n):
        val=(imagen_c[x,y,0]+ imagen_c[x,y,1] + imagen_c[x,y,2])
        if val==0:
            imagenCromatica[x,y,0]==0    
        else: 
            imagenCromatica[x,y,z]=imagen_c[x,y,z]/(imagen_c[x,y,0]+imagen_c[x,y,1]+imagen_c[x,y,2])
    result=cv2.normalize(imagenCromatica,dst=None,alpha=0,beta=255,norm_type=cv2.NORM_MINMAX,dtype=cv2.CV_8U)
    return result

imagenc1=cCromaticas(imagen)
imagenc2=cCromaticas(imagen2)
imagenc3=cCromaticas(imagen3)

cv2.imwrite('imagenc1.jpg',imagenc1)
cv2.imwrite('imagenc2.jpg',imagenc2)
cv2.imwrite('imagenc3.jpg',imagenc3)

imagenc1=cv2.imread('imagenc1.jpg')
m,n,c=imagenc1.shape
imagenb1=np.zeros((m,n))
for x in range(m):
    for y in range(n):
        if 51<imagenc1[x,y,0]<87 \
            and 63<imagenc1[x,y,1]<91 \
                and 88<imagenc1[x,y,2]<139:
                    imagenb1[x,y]=255

imagenc2=cv2.imread('imagenc2.jpg')
m,n,c=imagenc2.shape
imagenb2=np.zeros((m,n))
for x in range(m):
    for y in range(n):
        if 51<imagenc2[x,y,0]<87 \
            and 63<imagenc2[x,y,1]<91 \
                and 88<imagenc2[x,y,2]<139:
                    imagenb2[x,y]=255

imagenc3=cv2.imread('imagenc3.jpg')
m,n,c=imagenc3.shape
imagenb3=np.zeros((m,n))
for x in range(m):
    for y in range(n):
        if 51<imagenc3[x,y,0]<87 \
            and 63<imagenc3[x,y,1]<91 \
                and 88<imagenc3[x,y,2]<139:
                    imagenb3[x,y]=255

cv2.imwrite('imagenb1.jpg',imagenb1)
cv2.imwrite('imagenb2.jpg',imagenb2)
cv2.imwrite('imagenb3.jpg',imagenb3)

cv2.imshow("Atenuado 1",imagen2)
cv2.imshow("Atenuado 2",imagen3)
cv2.imshow("Cromatico 1",imagenc1)
cv2.imshow("Cromatico 2",imagenc2)
cv2.imshow("Cromatico 3",imagenc3)
cv2.imshow("Blanco y Negro 1",imagenb1)
cv2.imshow("Blanco y Negro 2",imagenb2)
cv2.imshow("Blanco y Negro 3",imagenb3)
cv2.waitKey(0)
cv2.destroyAllWindows()
