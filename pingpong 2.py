import pygame
pygame.init()
WIDTH = 900
HEIGHT = 480
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('My First Game - PingPong')
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS',30)

impactsound = pygame.mixer.Sound('imp.wav')

music = pygame.mixer.music.load('bgmusic.mp3')
pygame.mixer.music.set_volume(0.3)

class Ball():
    def __init__(self,x,y,radius,color,dx,dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = dx
        self.dy = dy
        self.miss = False 
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
    def update(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

class Bar():
    def __init__(self,x,y,color,width,height,dx,dy,dir):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.dx = dx
        self.dy = dy
        self.dir = dir
        self.score = 0
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
    def update(self,dir):
        pass

ball = Ball(int(WIDTH/2),int(HEIGHT/2),20,(147,7,246),4,4)

run = True
front_img = pygame.transform.scale(pygame.image.load('front.png'),(500,200))
play_but = pygame.transform.scale(pygame.image.load('play.png'),(146,147))
score_but = pygame.transform.scale(pygame.image.load('score.png'),(146,147))
ctrl_but = pygame.transform.scale(pygame.image.load('controls.png'),(146,147))

while run:
    win.fill((0,0,0)) 
    win.blit(front_img,(180,50))
    win.blit(play_but,(180,270))
    win.blit(score_but,(330,270))
    win.blit(ctrl_but,(480,270))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('left button pressed')
                pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                #move the left bar up
                print('W pressed')
                pass
            if event.key == pygame.K_s:
                #move the left bar down
                print('S pressed')
                pass
            if event.key == pygame.K_UP:
                #move the right bar up
                pass
            if event.key == pygame.K_DOWN:
                #move the right bar up
                pass
            if event.key == pygame.K_r:
                #restart game
                pass
            if event.key == pygame.K_SPACE:
                #start game
                pass
pygame.quit() 
