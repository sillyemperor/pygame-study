"""
作为初始代码，目标是有的一个固定大小的球，给定一个初识速度，和一个固定阻力，演示球运动的过程。每一个循环的时间与现实时间一致。
从最初代码开始演示如何一步步完善代码最终完成功能的过程。
"""
import sys, pygame
import os.path
import random
import time
import math
#pygame.font.init()
#myfont = pygame.font.SysFont('Comic Sans MS', 30)

def hit_A(x, y):
    return y <= 10

def hit_B(x, y):
    return x >= 590

def hit_C(x, y):
    return y >= 470

def hit_D(x, y):
    return x <= 10


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(BASE_DIR)

pygame.init()

screen = pygame.display.set_mode((600, 480))


ball_color = [255, 0, 0]

x, y = random.randint(10, 590), random.randint(10, 390)
speed = random.randint(100, 300)
u = random.random()*math.pi
f = 20
t = time.time()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 255, 255))
    t1 = time.time()
    dt = t1-t
    d = speed*dt
    dx, dy = d*math.cos(u), d*math.sin(u)
    x += dx
    y += dy
    if hit_B(x, y):
        u = math.pi - u
    elif hit_C(x,y):
        u = 2*math.pi - u
    elif hit_D(x,y):
        u = 3*math.pi - u
    elif hit_A(x, y):
        u = 2*math.pi - u
    speed -= f*dt
    if speed < 0:
        speed = 0
    # 在前进方向上移动一步
    pygame.draw.circle(screen, ball_color, (int(x), int(y)), 10)

    #textsurface = myfont.render(f'{dx} {dy}', False, (0, 0, 0))
    #screen.blit(textsurface,(x,y))
    
    pygame.display.flip()
    t = t1
