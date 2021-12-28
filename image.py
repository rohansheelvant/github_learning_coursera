import cv2
import numpy as  np

img1 = np.ones((256,256))

img1[50:100, 50:100] = 0

img2 = np.zeros((256,256))

img3 = img1 * img2