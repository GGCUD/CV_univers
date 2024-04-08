import cv2
import numpy as np
from Shape import ShapeDetector
import test
class ShapeColorDetector:
    def __init__(self):
        pass
    def detectColor(self, output):
        hsv = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
        masks = {
        "Yellow": ((25, 200, 200), (30, 255, 255)),
        "Green": ((65, 150, 150), (70, 255, 255)),
        "Red": ((175, 200, 200), (180, 255, 255)),
        "Blue": ((115, 150, 150), (120, 255, 255)),
        "Pirple": ((145, 100, 100), (155, 255, 255)),
                }
        colors = ["Yellow", "Green", "Red", "Blue", "Pirple"]
        
        sd = ShapeDetector()

        counter = 0
        cnt_triangle = cnt_regular_triangle = cnt_squre = cnt_Rombus = cnt_trapeze = cnt_rectangle = cnt_pentagon = cnt_circle = cnt_Ellipse = 0

        file_path = 'C:\\pyproj\\CV\\Laba3\\file.txt'
        

        for color in colors:
            mask = cv2.inRange(hsv, masks[color][0], masks[color][1])
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
            contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 10]

            for cnt in contours:
                M = cv2.moments(cnt)
                cX = int((M["m10"] / M["m00"]))
                cY = int((M["m01"] / M["m00"]))
                Size = str(cv2.contourArea(cnt))
                shape = sd.detect(cnt)
                cv2.drawContours(output, [cnt], -1, (0, 255, 0), 2)
                cv2.circle(output, (cX, cY), 2, (255, 255, 255), -1)
                cv2.putText(output, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                cv2.putText(output, color, (cX + 15, cY + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                cv2.putText(output, Size, (cX + 15, cY + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
                new_line =  shape +' '+ color +' size {}'.format(Size)
                match shape:
                    case "Triangel":  cnt_triangle += 1
                    case "Regular Triangel":  cnt_regular_triangle += 1
                    case "Squere":  cnt_squre += 1
                    case "Rombus":  cnt_Rombus += 1
                    case "Rectangle": cnt_rectangle += 1
                    case "Trapeze": cnt_trapeze += 1
                    case "Pentagon": cnt_pentagon += 1
                    case "Circle":  cnt_circle += 1
                    case "Ellipse": cnt_Ellipse += 1
                with open(file_path, 'a+') as f:
                    f.write(new_line + '\n')

            counter = counter + len(contours)
        
        
        
        text = "1145. Ryabchenok Sergey Muradovich. Number of objects: {}".format(counter)
        cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (240, 0, 159), 2)
        print('Number of obj. :', counter, '\n')

        test.find_lines_with_keywords(file_path, 'Triangel'),
        print('=========\n','Number of triangles :', cnt_regular_triangle + cnt_triangle, '\n')
        
        test.find_lines_with_keywords(file_path, 'Rombus'),
        test.find_lines_with_keywords(file_path, 'Rectangle'),
        test.find_lines_with_keywords(file_path, 'Trapeze'),
        test.find_lines_with_keywords(file_path, 'Squere'),        

        print('=========\n','Number of rectangles :', cnt_squre + cnt_trapeze + cnt_Rombus + cnt_rectangle,'\n')    
        
        test.find_lines_with_keywords(file_path, 'Pentagon'),
        test.find_lines_with_keywords(file_path, 'Circle'),
        test.find_lines_with_keywords(file_path, 'Ellipse'),

        print('=========\n','Number of others obj. :', cnt_pentagon + cnt_circle + cnt_Ellipse, '\n')
        cv2.waitKey(0)
        #open(file, 'w').close()
        with open(file_path, 'a+') as f:
            f.truncate(0)

        return 1