import cv2
import cv2.cv as cv
import numpy as np

class CA:

    circleList = None
    image = None


    startX = 15
    startY = 450
    numRow = 6
    numCol = 7
    vertDist = 70
    horiDist = 80

    @staticmethod
    def captureImage():
        img = cv2.imread("cols.jpg", 0);

        circles = cv2.HoughCircles(img,cv.CV_HOUGH_GRADIENT,1,25,param1=20,param2=26,minRadius=25,maxRadius=38)
        CA.circleList = circles
        CA.image = img

    @staticmethod
    def holdOn():
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    @staticmethod
    def getCircleArray():

        temp =np.zeros((6,7))

        endX = CA.startX + CA.numCol * CA.horiDist
        endY = CA.startY - CA.numRow * CA.vertDist

        for i in range(0, CA.numRow + 1):
            cv2.line(CA.image, (CA.startX, CA.startY - i * CA.vertDist),(endX, CA.startY - i * CA.vertDist), (0,255,255), 2)

        for i in range(0, CA.numCol + 1):
            cv2.line(CA.image, (CA.startX + i * CA.horiDist, CA.startY),(CA.startX + i * CA.horiDist, endY), (0,255,255), 2)

        if CA.circleList is not None:
            CA.circleList = np.uint16(np.around(CA.circleList))

            for i in CA.circleList[0,:]:

                col = (i[0] - CA.startX) / CA.horiDist
                row = (CA.startY - i[1]) / CA.vertDist

                avg = 0
                for a in range(i[0] - 5, i[0] + 5):
                    for b in range (i[1] - 5, i[1] + 5):
                        avg = avg + CA.image[b, a]

                avg = avg / 100

                print(i[0], i[1], col, row, CA.image[i[1], i[0]])

                if (avg > 100):
                    temp[CA.numRow - row - 1][col] = 1
                else:
                    temp[CA.numRow - row - 1][col] = 2

                cv2.circle(CA.image,(i[0],i[1]),i[2],(0,255,0),2)   # outer circle
                cv2.circle(CA.image,(i[0],i[1]),2,(0,0,255),3)      # inner circle

        print(temp)
        return temp

        cv2.imshow('stuff',CA.image)



