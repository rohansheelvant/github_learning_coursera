import cv2
import numpy as  np

img1 = np.ones((256,256))

img1[50:100, 50:100] = 0

img2 = np.zeros((256,256))
img2[0:100, 0:100] = 1

img3 = img1 * img2

img3 = img3*255

img3 = img3[:,:,np.newaxis]

#add same files as main breach in new brach for testing