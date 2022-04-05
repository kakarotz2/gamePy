import pygame
from random import randint

# khoi tao
pygame.init()
# man hinh kich thuoc x = 480, y = 720
x = 460
y = 680
screen = pygame.display.set_mode((x, y))
# Ten Game
pygame.display.set_caption('Flapy Bird')

# tốc độ game
Fps = pygame.time.Clock()
fps = 60
# Chèn backgroud sàn
x_bird = 100
y_bird = y/2
backGround = pygame.image.load('img/bg.png')
floor = pygame.image.load('img/floor.png')
# Chen chim
bird_dow = pygame.image.load('img/bird-down.png')
bird_mid = pygame.image.load('img/bird-mid.png')
bird_up = pygame.image.load('img/bird-up.png')
bird_list = [bird_dow, bird_mid, bird_up]
index = 1
bird = bird_list[index]
birdRect = bird.get_rect(center=(x_bird, y_bird))

birdFlap = pygame.USEREVENT
pygame.time.set_timer(birdFlap, 200)
# vị trí sàn ban đầu
floorPos = 0
# chim rơi
gravity = 0.5
birdMove = 0
# Tạo ống
tubeMove = 4  # Tốc độ chạy của ống
tube1_x = 400
tube2_x = 600
tube3_x = 800
tube_Width = 40
tubeHeight_1 = randint(100,450)
tubeHeight_2 = randint(100,450)
tubeHeight_3 = randint(100,450)
tubeDow =  pygame.image.load('img/dow.png')
tubeUp =  pygame.image.load('img/up.png')
tube_k = 200

# Score
score = 0
font = pygame.font.Font('04b_19.ttf',40)
font1 = pygame.font.SysFont('san',40)
tubePass_1 = False 
tubePass_2 = False 
tubePass_3 = False 
# sound
sound = pygame.mixer.Sound('sound/sfx_wing.wav')
sound_score = pygame.mixer.Sound('sound/sfx_point.wav')
# Game over
gameActivity = False
gameOver = pygame.image.load('img/gameOver.png')
