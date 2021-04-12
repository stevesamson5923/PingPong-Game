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

run = True
front_img = pygame.transform.scale(pygame.image.load('front.png'),(500,200))
play_but = pygame.transform.scale(pygame.image.load('play.png'),(146,147))
score_but = pygame.transform.scale(pygame.image.load('score.png'),(146,147))
ctrl_but = pygame.transform.scale(pygame.image.load('controls.png'),(146,147))

while run:
    win.fill((0,0,0)) 
    win.blit(front_img,(180,50))
