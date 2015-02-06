import pygame
import math

class DB:

    # Screen
    scrWidth = 700
    scrHeight = 400

    # Game Board
    boardX = 5
    boardY = 10
    boardXend = 10
    boardYend = 10
    boardXsize = 0
    boardYsize = 0
    boardSq = 40
    numCol = 9
    numRow = 10
    xMax = 160.0
    yMax = 180.0

    # Compass
    comX = 420
    comY = 100
    comR = 80
    comMaxR = 300

    # Connect 4
    c4X = 350
    c4Y = 220
    c4Xend = 0
    c4Yend = 0
    c4Width = 25
    c4numCol = 7
    c4numRow = 6
    c4R = 8

    black = (0,0,0)
    white = (255,255,255)
    blue = (0,100,255)
    red = (255,0,0)
    orange = (255,100,0)
    screen = None

    @staticmethod
    def init():
        pygame.init()
        DB.screen = pygame.display.set_mode((DB.scrWidth,DB.scrHeight), 0)
        DB.screen.fill(DB.white)

        DB.boardXend = DB.boardX + (DB.numCol - 1) * DB.boardSq
        DB.boardYend = DB.boardY + (DB.numRow - 1) * DB.boardSq
        DB.boardXsize = DB.boardXend - DB.boardX
        DB.boardYsize = DB.boardYend - DB.boardY

        DB.c4Xend = DB.c4X + DB.c4Width * DB.c4numCol
        DB.c4Yend = DB.c4Y + DB.c4Width * DB.c4numRow

    @staticmethod
    def drawOnField(x, y):

        for i in range(0, DB.numCol):
            pygame.draw.line(DB.screen, DB.black, (DB.boardX + i * DB.boardSq, DB.boardY),\
                (DB.boardX + i * DB.boardSq, DB.boardYend), 3)

        for i in range(0, DB.numRow):
            pygame.draw.line(DB.screen, DB.black, (DB.boardX, DB.boardY + i * DB.boardSq),\
                (DB.boardXend, DB.boardY + i * DB.boardSq), 3)

        plotX = int(DB.boardX + x / DB.xMax * DB.boardXsize)
        plotY = int(DB.boardY + y / DB.yMax * DB.boardYsize)

        print(plotX, ',' , plotY)

        pygame.draw.circle(DB.screen, DB.blue, (plotX, plotY), 7, 0)
        pygame.display.update()

    @staticmethod
    def drawCompass(x,y):
        l = math.sqrt(x * x + y * y)
        angle = math.atan2(y, x)
        disL = l / DB.comMaxR * DB.comR
        disX = disL * math.cos(angle)
        disY = disL * math.sin(angle)

        myfont = pygame.font.SysFont("monospace", 15)
        myfont.set_bold(True)
        label = myfont.render('{:.2f}'.format(angle / 3.1415926 * 180), 1, (50,50,255))
        DB.screen.blit(label, (DB.comX + disX, DB.comY - disY))

        pygame.draw.circle(DB.screen, DB.orange, (DB.comX, DB.comY), 5, 0)
        pygame.draw.circle(DB.screen, DB.black, (DB.comX, DB.comY), DB.comR, 3)
        pygame.draw.line(DB.screen, DB.black, (DB.comX, DB.comY), (DB.comX + disX, DB.comY - disY), 3)
        pygame.draw.line(DB.screen, DB.black, (DB.comX - DB.comR, DB.comY), (DB.comX + DB.comR, DB.comY), 1)
        pygame.draw.line(DB.screen, DB.black, (DB.comX , DB.comY - DB.comR), (DB.comX , DB.comY + DB.comR), 1)

        pygame.draw.line(DB.screen, DB.black, (DB.comX, DB.comY), (DB.comX + disX, DB.comY - disY), 3)
        pygame.display.update()

    @staticmethod
    def drawC4(array):
        for i in range(0, DB.c4numCol + 1):
            pygame.draw.line(DB.screen, DB.black, (DB.c4X + i * DB.c4Width, DB.c4Y),\
                (DB.c4X + i * DB.c4Width, DB.c4Yend), 3)

        if (array == None):
            pass
        else:
            for i in range(DB.c4numRow - 1, 0, -1):
                for j in range(0, DB.c4numCol):
                    if (array[i][j] == 1):
                        centerX = DB.c4X + j * DB.c4Width + DB.c4Width / 2
                        centerY = DB.c4Yend - (DB.c4numRow - i) * DB.c4Width + DB.c4Width / 2
                        pygame.draw.circle(DB.screen, DB.blue, (centerX, centerY), DB.c4R, 0)
                    elif (array[i][j] == 2):
                        centerX = DB.c4X + j * DB.c4Width + DB.c4Width / 2
                        centerY = DB.c4Yend - (DB.c4numRow - i) * DB.c4Width + DB.c4Width / 2
                        pygame.draw.circle(DB.screen, DB.red, (centerX, centerY), DB.c4R, 0)
        
        pygame.draw.line(DB.screen, DB.black, (DB.c4X, DB.c4Yend), (DB.c4Xend, DB.c4Yend), 3)
        pygame.display.update()
