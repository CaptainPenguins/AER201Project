import cv2
import cv2.cv as cv
import numpy as np

img = cv2.imread("cols.jpg", 0);

#img = cv2.Canny(img, 60, 70)

#cv2.imshow("lol", img)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,25,param1=20,param2=26,minRadius=25,maxRadius=38)

# ??, 7

if circles is not None:
    circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        print(i[2])
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('stuff',cimg)

if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.waitKey(0)
    cv2.destroyAllWindows()


