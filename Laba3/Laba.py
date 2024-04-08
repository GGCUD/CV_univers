import cv2
from ShapeColor import ShapeColorDetector
import numpy as np

file_name = np.zeros((760,900, 3), dtype = 'uint8')
file_name[:] = 255, 255, 255

cv2.rectangle(file_name,(200, 300), (250, 350), (56,44,255), -1)

cv2.rectangle(file_name,(700, 200), (650, 100), (225,31,209), -1)

cv2.circle(file_name,(447, 476), 63, (31,202,205), -1)

cv2.ellipse(file_name,(175, 405), (75, 50),  0,0,360,255,-1)

pts = np.array([[150,115],[220,230],[270,150],[250,110]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.fillPoly(file_name,[pts],(27,225,225))

pts = np.array([[300,150],[550,150],[425,366]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.fillPoly(file_name,[pts],(255,0,0))

pts = np.array([[100,630],[440,670],[255,425]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.fillPoly(file_name,[pts],(213,31,217))

pts = np.array([[600,300],[750,200],[900,300],[750,400]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.fillPoly(file_name,[pts],(150,250,100))


sd1 = ShapeColorDetector()
output = file_name.copy()
sd1.detectColor(output)
cv2.imshow("Contours", output)

cv2.waitKey(0)