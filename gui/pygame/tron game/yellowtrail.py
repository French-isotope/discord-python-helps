import pygame

pygame.init()

import random

HEIGHT = 600
WIDTH = 800

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 102, 0)
BLUE = (0, 0, 255)
BROWN = (26, 9, 0)

HSPEED = 100
VSPEED = 100
speedbx = random.randint(1, WIDTH)
speedby = random.randint(1, HEIGHT)
speedX = 0
speedY = -VSPEED
font = pygame.font.SysFont('Ariel Black', 60)
gameTxt = font.render('GAME ON Click the mouse to exit', 1, BLACK)
segx = [WIDTH // 2 + 200] * 3
segy = [HEIGHT - 200, HEIGHT + VSPEED, HEIGHT + 2 * VSPEED]


class Bikes:
    def __init__(self, player):
        self.player=player
        self.playernum = pygame.transform.scale(player, (70, 30))
        self.x = [WIDTH // 2 + 200] * 3
        self.y = [HEIGHT - 200, HEIGHT + VSPEED, HEIGHT + 2 * VSPEED]
        self.HSPEED = 5
        self.VSPEED = 5
        self.SPACE = True
        self.LEFT = False
        self.RIGHT = False
        self.UP = True
        self.DOWN = False
        self.speedX = 0
        self.speedY = -self.VSPEED
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.current_rect = None
        self.path = list()


    def move(self, up, down, right, left):
        keys = pygame.key.get_pressed()
        for i in range(1,len(self.y)):
            if self.x[0]==self.x[i] and self.y[0]==self.y[i]:
                gameOver=True
                inPlay=False
                print('yo')
        if self.x[0] == 0 or self.x[0] == 800 or self.y[0] == 600 or self.y[0] == 0:
            Game.Exit = True
            Game.Ingame = False
        if keys[pygame.K_SPACE] and self.SPACE:
            self.SPACE = False
        if not self.SPACE:
            keys = pygame.key.get_pressed()
            self.up = keys[up]
            self.down = keys[down]
            self.right = keys[right]
            self.left = keys[left]
            if keys[left]:
                self.speedX = - self.HSPEED
                self.speedY = 0
                self.LEFT = True
                if self.RIGHT:
                    Game.Exit = True
                    Game.ingame = False

                self.RIGHT = False
                self.UP = False
                self.DOWN = False
            if keys[right]:
                self.speedX = self.HSPEED
                self.speedY = 0
                self.RIGHT = True
                if self.LEFT:

                    Game.ingame = False
                    print('lol')
                self.LEFT = False
                self.UP = False
                self.DOWN = False
            if keys[up]:
                self.speedX = 0
                self.speedY = -self.VSPEED
                self.UP = True
                if self.DOWN:
                    Game.ingame = False

                self.LEFT = False
                self.RIGHT = False
                self.DOWN = False
            if keys[down]:
                self.speedX = 0
                self.speedY = self.VSPEED
                self.DOWN = True
                if self.UP:
                    Game.ingame = False

                self.LEFT = False
                self.RIGHT = False
                self.UP = False
            self.x.append(self.x[-1])
            self.y.append(self.y[-1])
#            print(self.x)
#            print(self.y)
            for i in range(len(segy) - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]
            self.x[0] = self.x[0] + self.speedX
            self.y[0] = self.y[0] + self.speedY
            if self.RIGHT:
                self.playerright=pygame.transform.rotate(self.playernum,0)
                self.screen.blit(self.playerright, (self.x[0] - 35, self.y[0] - 9))
            if self.LEFT:
                self.playerleft = pygame.transform.rotate(self.playernum, 180)
                self.screen.blit(self.playerleft, (self.x[0] - 10, self.y[0] - 9))
            if self.DOWN:
                self.playerdown = pygame.transform.rotate(self.playernum, 270)
                self.screen.blit(self.playerdown, (self.x[0] - 8, self.y[0] - 49))
            if self.UP:
                self.playerup = pygame.transform.rotate(self.playernum, 270)
                self.screen.blit(self.playerup, (self.x[0] - 8, self.y[0] - 9))

            for pos_x, pos_y in zip(self.x, self.y):
                rect = pygame.Rect((pos_x, pos_y), (15, 15))
                pygame.draw.rect(self.screen, YELLOW, rect)

#            pygame.display.update()

#    def draw_line(self):



class speedboostd:
    introScreen = True

    def distance(x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + 20:
            if y1 >= y2 and y1 <= y2 + 20:
                return True
        return False


class Play:
    def __init__(self):
        self.StartScreen = True
        self.Exit = False
        self.f = pygame.font.SysFont('Ariel Black', 60).render
        self.Ingame = True
        self.EndGame = False
        self.alreadydrawn = False

    def Draw(self, COLOUR, IMAGE, colour, x, y):
        self.Screen(COLOUR)
        TXT = self.f(IMAGE, 1, colour)
        self.screen.blit(TXT, (x, y))

    def Screen(self, colour):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.fill = self.screen.fill(colour)

    def game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.StartScreen = False
                self.Exit = True
            if event.type == pygame.MOUSEBUTTONDOWN and not self.StartScreen:
                self.Ingame = False
                self.EndGame = True
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.StartScreen = False

        if self.StartScreen:
            self.Draw(ORANGE, 'Press SPACE to start', BLUE, 10, 150)
            #pygame.display.update()

        if not self.StartScreen and not self.EndGame:
            if not self.alreadydrawn:
                self.Draw(RED, 'GAME ON: Click to exit.', BLACK, 10, 150)
                self.alreadydrawn = True
            Player1.move(pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT)
#            Player1.draw_line()

            Player2.move(pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a)
#            Player2.draw_line()

            pygame.display.update()

        if not self.Ingame:
            self.Draw(BROWN, 'GAME OVER', YELLOW, 20, 50)

        pygame.display.update()


Game = Play()
Player1 = Bikes(pygame.image.load(r'C:\python\p1bike.png'))

Player2 = Bikes(pygame.image.load(r'C:\python\p2bike.png'))
Player2.x = [HEIGHT // 2-200] * 3

while not Game.Exit:

    Game.game()
    pygame.time.delay(60)

