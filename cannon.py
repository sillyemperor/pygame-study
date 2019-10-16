"""
通过调节炮管角度，让炮弹击中随机距离外的目标。炮弹出膛速度，大地引力风阻是固定的。
"""
import sys, pygame
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(BASE_DIR)

pygame.init()

screen = pygame.display.set_mode((600, 480))

ball_center = (30, 30)
ball_color = [0, 255, 0]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 255, 255))
    # 在前进方向上移动一步
    pygame.draw.circle(screen, ball_color, ball_center, 10)
    pygame.display.flip()
