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
        self.ball = pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)
    def update(self,hl,hr):
        if self.ball.colliderect(hr.bar):
            self.dx = -self.dx
            hr.score = hr.score + 1
            pygame.mixer.Sound.play(impactsound)
        
        if self.ball.colliderect(hl.bar):
            self.dx = -self.dx
            hl.score = hl.score + 1
            pygame.mixer.Sound.play(impactsound)

        self.x = self.x + self.dx
        self.y = self.y + self.dy

        if (self.y+self.radius>=HEIGHT or self.y <=0):
            self.dy = -self.dy
        #if (self.x+self.radius>=WIDTH or self.x<= 0):
        #    self.dx = -self.dx
        if self.x > WIDTH:
            self.miss = True
            hr.score = hr.score - 1
            pygame.mixer.music.stop()
        if self.x < 0:
            self.miss = True
            hl.score = hl.score - 1
            pygame.mixer.music.stop()
        
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
        self.bar = pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
    def update(self,win,dir):
        self.dir = dir
        if self.dir < 0: 
            self.y = self.y - self.dy
        if self.dir > 0:
            self.y = self.y + self.dy
        self.draw(win)

def redrawindow(dl,dr):
    win.fill((0,0,0))
    ball.update(handleleft,handleright)
    ball.draw(win)
    handleleft.update(win,dl)
    handleright.update(win,dr)
    pygame.display.update()

def initialize_game():
    global ball,handleleft,handleright
    win.fill((0,0,0))
    ball = Ball(int(WIDTH/2),int(HEIGHT/2),20,(147,7,246),4,4)
    ball.draw(win)
    handleleft = Bar(0,200,(40,222,60),20,200,10,37,0)
    handleright = Bar(int(WIDTH-20),200,(100,28,60),20,200,10,37,0)
    handleleft.draw(win)
    handleright.draw(win)
    pygame.display.update()

run = True
front_img = pygame.transform.scale(pygame.image.load('front.png'),(500,200))
play_but = pygame.transform.scale(pygame.image.load('play.png'),(146,147))
score_but = pygame.transform.scale(pygame.image.load('score.png'),(146,147))
ctrl_but = pygame.transform.scale(pygame.image.load('controls.png'),(146,147))

space = False
play_start =False
while run:
    direction_l = 0
    direction_r = 0
    if not play_start:
        win.fill((0,0,0)) 
        win.blit(front_img,(180,50))
        win.blit(play_but,(180,270))
        win.blit(score_but,(330,270))
        win.blit(ctrl_but,(480,270))
        pygame.display.update()
    else:
        if not space:
            initialize_game()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x>=180 and x<=326 and y>=270 and y<=417:
                    play_start = True
                    pygame.mixer.music.play(-1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                #move the left bar up
                direction_l = -1
            if event.key == pygame.K_s:
                #move the left bar down
                direction_l = 1
            if event.key == pygame.K_UP:
                #move the right bar up
                direction_r = -1
            if event.key == pygame.K_DOWN:
                #move the right bar up
                direction_r = 1
            if event.key == pygame.K_r:
                #restart game
                pass
            if event.key == pygame.K_SPACE:                
                space = True
    if space:
        redrawindow(direction_l,direction_r)        
pygame.quit() 
