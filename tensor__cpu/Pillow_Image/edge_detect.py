# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:41:09 2017

@author: Administrator
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from timeit import default_timer as timer

input_img = cv2.imread('65210119890101353x.jpg', 0)

cv2.imshow("Input img", input_img)
cv2.waitKey(2)

canny_edge_time_total = 0
morph_edge_time_total = 0
test_iterations = 1000

for iterations in range(0, test_iterations):
    canny_start = timer()
    canny_edges = cv2.Canny(input_img, 50, 150)
    canny_end = timer()
    canny_edge_time_total = canny_edge_time_total + (canny_end - canny_start)

    morph_start = timer()
    retval, black_and_white_mask = cv2.threshold(input_img, 125, 255, cv2.THRESH_BINARY)
    black_and_white_mask = cv2.bitwise_not(black_and_white_mask)
    kernel = np.ones((3, 3), np.uint8)
    img_dilation = cv2.dilate(black_and_white_mask, kernel, iterations=1)
    morph_edges = img_dilation - black_and_white_mask
    morph_end = timer()
    morph_edge_time_total = morph_edge_time_total + (morph_end - morph_start)

canny_edge_time_avg = canny_edge_time_total / test_iterations
morph_edge_time_avg = morph_edge_time_total / test_iterations

cv2.imshow("Canny Edges", canny_edges)
cv2.waitKey(2000)
#cv2.destroyAllWindows()
cv2.imshow("Morphology Edges", morph_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Canny edge detection took " + str(canny_edge_time_avg) + " seconds on average")
print("Morphology edge detection took " + str(morph_edge_time_avg) + "seconds on average")