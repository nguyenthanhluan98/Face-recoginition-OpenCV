import cv2
import numpy
from PIL import Image

img = cv2.imread("thiacm.jpg")

print("Original dimenstions: ", img.shape)
print("width: ", img.shape[1])
print("height: ", img.shape[0])
path = "thiacm.jpg"
im = Image.open(path).convert('RGB') 

r = im.resize((551, 500), Image.ANTIALIAS)
open_cv_image = numpy.array(r) 
open_cv_image = open_cv_image[:, :, ::-1].copy() 
'''
scale_precent = 60
width = int(img.shape[1] * scale_precent / 100)
height = int(img.shape[0]* scale_precent / 100)
dim = (width, height)

print("dim: ", dim)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

print("resized dimestions: ", resized.shape)
'''

cv2.imshow("resized", open_cv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()