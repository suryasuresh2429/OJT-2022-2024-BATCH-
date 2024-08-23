import cv2 
import numpy as np

image=cv2.imread('img.jpg')

if image is None:
    print("could not read the image ")
    exit()

#original image
# cv2.imshow('original image',image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#convert to grayscale
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow('grayscale image',gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#gaussian blur 
blurred_image=cv2.GaussianBlur(image,(5,5),0)
# cv2.imshow('blurred image',blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#edge detection using canny in cv2
edges=cv2.Canny(blurred_image,100,200)

cv2.imshow('original image',image)
cv2.waitKey(0)

cv2.imshow('grayscale image',gray_image)
cv2.waitKey(0)

cv2.imshow('blurred image',blurred_image)
cv2.waitKey(0)

cv2.destroyAllWindows()