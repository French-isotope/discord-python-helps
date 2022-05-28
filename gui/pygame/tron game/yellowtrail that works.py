import pygame

pygame.init()

import random

HEIGHT = 600
WIDTH = 800

speedboost = pygame.image.load(r'C:\python\p1bike.png')
speedboost = pygame.transform.scale(speedboost, (20, 20))

font = pygame.font.SysFont('Ariel Black', 60)
p1 = pygame.image.load(r'C:\python\p1bike.png')
p2 = pygame.image.load(r'C:\python\p2bike.png')

p1 = pygame.transform.scale(p1, (70, 30))

BLACK = (0, 0, 0)
RED = (255, 0, 0)

YELLOW = (255, 255, 0)
ORANGE = (255, 102, 0)
BLUE = (0, 0, 255)
BROWN = (26, 9, 0)
outline = 0
BODYSIZE = 15
HSPEED = 10
VSPEED = 10
speedbx = random.randint(1, WIDTH)
speedby = random.randint(1, HEIGHT)
speedX = 0
speedY = -VSPEED
segx = [WIDTH // 2 + 200] * 3
segy = [HEIGHT - 200, HEIGHT + VSPEED, HEIGHT + 2 * VSPEED]

if speedbx == segx[0]:
    speedbx = -30
print(speedbx, segx[0])
screen = pygame.display.set_mode((WIDTH, HEIGHT))
LEFT = False
RIGHT = False
UP = True
DOWN = False

BODYSIZE = 15
HSPEED = 10
VSPEED = 10


class Bikes:
    def __init__(self):
        self.p1 = pygame.image.load(r'C:\python\p1bike.png')
        self.p2 = pygame.image.load(r'C:\python\p2bike.png')
        self.x = [WIDTH // 2 + 200] * 3
        self.y = [HEIGHT - 200, HEIGHT + VSPEED, HEIGHT + 2 * VSPEED]

    def drawbike(self):
        self.screen = self.blit(self.p1, (self.x[0], self.y[0]))

    def move(self):
        self.up = keys[pygame.K_UP]
        self.down = keys[pygame.K_DOWN]
        self.right = keys[pygame.K_RIGHT]
        self.left = keys[pygame.K_LEFT]

    def Trons(self):
        pass


class speedboostd:
    def distance(x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + 20:
            if y1 >= y2 and y1 <= y2 + 20:
                return True
        return False


class Play:
    def __init__(self, colour):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.fill = self.screen.fill(colour)

    def game(self):
        pass


def redrawScreen():
    screen.fill(RED)
    gameTxt = font.render('GAME ON Click the mouse to exit', 1, BLACK)
    screen.blit(gameTxt, (10, 150))
    for x in range(len(segx)):
        print(segx)
        pygame.draw.rect(screen, BLUE, (segx[x], segy[x], BODYSIZE, BODYSIZE), outline)

    if not speedboostd.distance(segx[0], segy[0], speedbx, speedby) and speedboosts == 0:
        screen.blit(speedboost, (speedbx, speedby))

    if RIGHT:
        screen.blit(p1, (segx[0] - 35, segy[0] - 9))
    if LEFT:
        p1left = pygame.transform.rotate(p1, 180)
        screen.blit(p1left, (segx[0] - 10, segy[0] - 9))
    if DOWN:
        p1down = pygame.transform.rotate(p1, 270)
        screen.blit(p1down, (segx[0] - 8, segy[0] - 49))
    if UP:
        p1up = pygame.transform.rotate(p1, 270)
        screen.blit(p1up, (segx[0] - 8, segy[0] - 9))

    pygame.display.update()


def endGameScreen():
    screen.fill(BROWN)
    endTxt = font.render('GAME OVER', 1, YELLOW)
    screen.blit(endTxt, (20, 150))
    pygame.display.update()


def startGameScreen():
    screen.fill(ORANGE)
    startTxt = font.render('Press SPACE to Start the Game ', 1, BLUE)
    screen.blit(startTxt, (10, 150))
    pygame.display.update()


inPlay = True
introScreen = True

while introScreen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            introScreen = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        introScreen = False

    startGameScreen()
speedboosts = 0
Player1 = Bikes()
Player2 = Bikes()
print(Player2.x)
while inPlay:
    if speedboostd.distance(segx[0], segy[0], speedbx, speedby) and speedboosts == 0:
        speedboosts += 1
        HSPEED += 10
        VSPEED += 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False  #
        if event.type == pygame.MOUSEBUTTONDOWN:
            gameOver = True
            inPlay = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        speedX = - HSPEED
        speedY = 0
        LEFT = True
        if RIGHT:
            gameOver = True
            inPlay = False
        RIGHT = False
        UP = False
        DOWN = False
    if keys[pygame.K_d]:
        speedX = HSPEED
        speedY = 0
        RIGHT = True
        if LEFT:
            gameOver = True
            inPlay = False
        LEFT = False
        UP = False
        DOWN = False
    if keys[pygame.K_w]:
        speedX = 0
        speedY = -VSPEED
        UP = True
        if DOWN:
            gameOver = True
            inPlay = False
        LEFT = False
        RIGHT = False
        DOWN = False
    if keys[pygame.K_s]:
        speedX = 0
        speedY = VSPEED
        DOWN = True
        if UP:
            gameOver = True
            inPlay = False
        LEFT = False
        RIGHT = False
        UP = False

    segx.append(segx[-1])
    segy.append(segy[-1])

    for i in range(len(segy) - 1, 0, -1):
        segx[i] = segx[i - 1]
        segy[i] = segy[i - 1]
    segx[0] = segx[0] + speedX
    segy[0] = segy[0] + speedY
    if segx[0] == 0 or segx[0] == 800 or segy[0] == 600 or segy[0] == 0:
        gameOver = True
        inPlay = False

    for i in range(1, len(segx)):
        if segx[0] == segx[i] and segy[0] == segy[i]:
            gameOver = True
            inPlay = False
    redrawScreen()
    pygame.time.delay(1000)

while gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = False  #

    endGameScreen()
    pygame.time.delay(1000)

pygame.quit()