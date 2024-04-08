import cv2
import imutils
#import os
import numpy as np

file_name = np.zeros((800, 900, 3), dtype = 'uint8')
#os.path.join(os.path.dirname(__file__), 'img.jpg')

file_name[:] = 255, 255, 255

cv2.rectangle(file_name,(300, 300), (350, 350), (0,255,0), -1)

cv2.rectangle(file_name,(700, 200), (650, 100), (17,201,97), -1)

cv2.circle(file_name,(447, 476), 63, (128,17,99), -1)

cv2.ellipse(file_name,(175, 405), (75, 50),  0,0,360,255,-1)

pts = np.array([[150,115],[220,230],[270,150],[250,110]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.fillPoly(file_name,[pts],(125,255,70))

cv2.imshow("Image", file_name)
gray = cv2.cvtColor(file_name, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = file_name.copy()
for c in cnts:
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
text = "1145. Ryabchenok Sergey Muradovich. Number of objects: {}".format(len(cnts))
cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (240, 0, 159), 2)
cv2.imshow("Contours", output)
print('Кол-во объектов:', len(cnts))
cv2.imshow('Thresh', thresh)
cv2.imshow('Gray',gray)
print(type(file_name))
cv2.waitKey(0)
