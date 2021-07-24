import time
import pygame
import random

WIDTH = 1100
HEIGHT = 900
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (201,151,124)
BIGBRROWN=(138,86,57)

#制作棋盘list
qipan=[[0 for i in range(0,16)] for j in range(0,16)]
# initialize pygame and create window
pygame.init()
pygame.mixer.init()   #需要播放音效
pygame.mixer.music.load("../task2_version2.0/BGM.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" 单机小游戏 五子棋")
clock = pygame.time.Clock()

myfont = pygame.font.Font(None,40)
my2font = pygame.font.Font(None,45)

# Game loop
running = True
count = 0
start = time.time()
whi_img = pygame.image.load(r"../task2_version2.0/WCH.png")
bla_img = pygame.image.load(r"../task2_version2.0/GCH.png")
a=2

winner=0

                      
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    count+=1
    now = time.time()
    fps = count/(now-start)
    fpsImage = myfont.render('time_'+str((now-start)//1), True, WHITE)
    # Draw / render
    screen.fill(BROWN)
    screen.blit(fpsImage, (830, 10))
    def hint(hint,i,j):
        hintImage = my2font.render(hint, True, RED)
        screen.blit(hintImage, (i, j))
    def b_blit(i,j):
        screen.blit(bla_img, (i*50, j*50))   #绘制黑棋     #+++++++++++++++++++++++++++++++++++++++++++++++++++
    def w_blit(i,j):
        screen.blit(whi_img, (i*50, j*50))   #绘制白棋
    for i in range(0,850,50):
        pygame.draw.line(screen,BIGBRROWN, (i, 0), (i, 800), 2)         #绘制线条
    for j in range(0,850,50):
        pygame.draw.line(screen,BIGBRROWN, (0, j), (800, j), 2)         #绘制线条
    def blitall():
        for i in range(len(qipan)):
            for j in range(len(qipan[0])):
                if qipan[i][j]==1:
                    w_blit(i,j)
                elif qipan[i][j]==2:
                    b_blit(i,j)    #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                else:
                    pass


    #开始
    if(a==2):
        hint('black chess',850,100)
    elif(a==1):
        hint('white chess',850,100)

    if(event.type == pygame.MOUSEBUTTONUP):
        x, y = pygame.mouse.get_pos ()
        xx=x//50
        yy=y//50
        if(xx<16 and xx>=0 and yy<16 and yy>=0):
            if(qipan[xx][yy]==0):
                qipan[xx][yy]=a
                a=3-a
            
        blitall()
    for i in range(16):
        for j in range(16):   
            if qipan[i][j] != 0 :
            
                #检查 每行 是否有连续五个同一颜色的棋子            
                if i<12:                
                    if (qipan[i][j] == qipan[i+1][j]  == qipan[i+2][j]  == qipan[i+3][j]  == qipan[i+4][j]):
                        winner=qipan[i][j]
                        break
                if j<12:
                    if(qipan[i][j] == qipan[i][j+1] == qipan[i][j+2] == qipan[i][j+3] == qipan[i][j+4]):
                        winner=qipan[i][j]
                        break
                if (i<12 and j<12):
                    if(qipan[i][j] == qipan[i+1][j+1] == qipan[i+2][j+2] == qipan[i+3][j+3] == qipan[i+4][j+4]):
                        winner=qipan[i][j]
                        break
                if (j<12 and i>=4):
                    if(qipan[i][j] == qipan[i-1][j+1] == qipan[i-2][j+2] == qipan[i-3][j+3] == qipan[i-4][j+4]):
                        winner=qipan[i][j]
                        break
    if(winner==1):
        hint('white win!!!',850,400)
    elif(winner==2):
        hint('black win!!!',850,400)     
    blitall() #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()