import cv2
import numpy as np
import math 
class ShapeDetector:
    def __init__(self):
        pass
    def detect(self, cnts):
        Tcnt = 0
        shape = "unidentified"
        peri = cv2.arcLength(cnts, True)
        approx = cv2.approxPolyDP(cnts, 0.04 * peri, True)
        if len(approx) == 3:
            s1 = math.sqrt((approx[0,0][0] - approx [1,0][0])**2 + (approx[0,0][1]-approx[1,0][1])**2)
            s2 = math.sqrt((approx[1,0][0] - approx [2,0][0])**2 + (approx[1,0][1]-approx[2,0][1])**2)
            s3 = math.sqrt((approx[0,0][0] - approx [2,0][0])**2 + (approx[0,0][1]-approx[2,0][1])**2)            
            if  (abs(s1-s2)<5) and (abs(s2-s3)<5) and (abs(s1 -s3)<5):    
                shape = "Regular Triangel"
            else: 
                shape = "Triangel"

        elif len(approx) == 4:
            
            s1_ = math.sqrt((approx[0,0][0] - approx [1,0][0])**2 + (approx[0,0][1]-approx[1,0][1])**2)
            s2_ = math.sqrt((approx[1,0][0] - approx [2,0][0])**2 + (approx[1,0][1]-approx[2,0][1])**2)
            s3_ = math.sqrt((approx[2,0][0] - approx [3,0][0])**2 + (approx[2,0][1]-approx[3,0][1])**2)
            s4_ = math.sqrt((approx[3,0][0] - approx [0,0][0])**2 + (approx[3,0][1]-approx[0,0][1])**2)

            d1 = math.sqrt((approx[0,0][0] - approx [2,0][0])**2 + (approx[0,0][1]-approx[2,0][1])**2)
            d2 =  math.sqrt((approx[1,0][0] - approx [3,0][0])**2 + (approx[1,0][1]-approx[3,0][1])**2)

            alfa = np.degrees(np.arccos((s1_**2+s2_**2 - d1**2)/(2*s1_*s2_)))
            if (abs(s1_-s2_)<5) and (abs(s2_-s3_)<5) and (abs(s1_-s3_)<5) and (abs(d1 - d2)<5):
                shape = "Squere"
            elif( (abs(s1_-s2_)<5) and (abs(s2_-s3_)<5) and (abs(s1_- s3_)<5)):
                shape = "Rombus"
            elif alfa <= 95 and alfa >= 85: 
                shape = "Rectangle"
            else:
                shape = "Trapeze"

        elif len(approx) == 5:
            shape = "Pentagon"
        else:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            if ar >= 0.95 and ar <= 1.05:
                shape = "Circle"
            else:
                shape = "Ellipse"
        return shape