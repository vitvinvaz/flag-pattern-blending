import numpy as np
import cv2 as cv


#Reading Images
flag = cv.imread('images/flag.jpg')
pattern = cv.imread('images/pattern.jpg')


#Showing error if image is not loaded properly
if flag is None:
    raise FileNotFoundError('Flag image failed to load.')
if pattern is None:
    raise FileNotFoundError('Pattern image failed to load.')

#Resizing the images for visiblity
flag = cv.resize(flag , (600 ,400))
pattern = cv.resize(pattern , (600 ,400))

#Blending the images using addWeighted() method
blended_img = cv.addWeighted(flag, 0.4, pattern, 0.8, 0)

#Showing the output
cv.imshow('flag', blended_img)
cv.imwrite('Output.jpg', blended_img)
cv.waitKey(0)
cv.destroyAllWindows()

