from Debug import DB
from Camera import CA

import FAKEGPIO as GPIO

testArray = [[0,0,0,0,0,0,0],
             [0,0,0,1,0,0,0],
             [0,0,2,1,0,0,0],
             [0,2,2,2,2,1,1],
             [1,1,2,1,1,1,2],
             [2,1,2,1,1,2,2]]

DB.init()

DB.drawOnField(100,100)
DB.drawCompass(150,200)


CA.captureImage()

tempArray = CA.getCircleArray()
CA.holdOn()

DB.drawC4(tempArray)



