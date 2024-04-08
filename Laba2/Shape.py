import cv2
import numpy as np
import math 
class ShapeDetector:
    def __init__(self):
        pass
    def detect(self, c):
        
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) == 3:
            """
            rect = cv2.minAreaRect(approx)
            box = cv2.boxPoints(rect)
            box = np.intp(box)
            (x,y), (w, h), betta = rect
            ar = w / float(h)
              shape = "GIGAtriangleEnjoyer" if ar >= 0.855 and ar <= 0.865 else "AveragetriangleFun"
            """
            s1 = math.sqrt((approx[0,0][0] - approx [1,0][0])**2 + (approx[0,0][1]-approx[1,0][1])**2)
            s2 = math.sqrt((approx[1,0][0] - approx [2,0][0])**2 + (approx[1,0][1]-approx[2,0][1])**2)
            s3 = math.sqrt((approx[0,0][0] - approx [2,0][0])**2 + (approx[0,0][1]-approx[2,0][1])**2)            
            if  (abs(s1-s2)<5) and (abs(s2-s3)<5) and (abs(s1 -s3)<5):    
                shape = "RegularTriangle"
            else: 
                shape = "Triangel"
        elif len(approx) == 4:

            """(x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
            """
            
            s1_ = math.sqrt((approx[0,0][0] - approx [1,0][0])**2 + (approx[0,0][1]-approx[1,0][1])**2)
            s2_ = math.sqrt((approx[1,0][0] - approx [2,0][0])**2 + (approx[1,0][1]-approx[2,0][1])**2)
            s3_ = math.sqrt((approx[2,0][0] - approx [3,0][0])**2 + (approx[2,0][1]-approx[3,0][1])**2)
            s4_ = math.sqrt((approx[3,0][0] - approx [0,0][0])**2 + (approx[3,0][1]-approx[0,0][1])**2)

            d1 = math.sqrt((approx[0,0][0] - approx [2,0][0])**2 + (approx[0,0][1]-approx[2,0][1])**2)
            d2 =  math.sqrt((approx[1,0][0] - approx [3,0][0])**2 + (approx[1,0][1]-approx[3,0][1])**2)

            alfa = np.degrees(np.arccos((s1_**2+s2_**2 - d1**2)/(2*s1_*s2_)))
            #shape = "Squere" if  (abs(s1_-s2_)<5) and (abs(s2_-s3_)<5) and (abs(s1_-s3_)<5) and (abs(d1 - d2)<5) else "Romb"
            if (abs(s1_-s2_)<5) and (abs(s2_-s3_)<5) and (abs(s1_-s3_)<5) and (abs(d1 - d2)<5):
                shape = "squere"
            elif( (abs(s1_-s2_)<5) and (abs(s2_-s3_)<5) and (abs(s1_- s3_)<5)):
                shape = "Rombus"
            elif alfa <= 95 and alfa >= 85: 
                shape = "rectangle"
            else:
                shape = "trapeze"

        elif len(approx) == 5:
            shape = "pentagon"
        else:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            if ar >= 0.95 and ar <= 1.05:
                shape = "Circle"
            else:
                shape = "Ellipse"
        return shape