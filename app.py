import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()
    width = 900
    height = 600
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("snake game")

    clock = pygame.time.Clock()

    # red = 0
    x = 400
    y = 300
    r = 50
    moving = True
    vx, vy = 0, 0
    positions = [[x, y], [x-r, y], [x-2*r, y], [x-3*r, y]]
    while True:
        screen.fill((0,0,0))
        for i in range(len(positions)):
            if i == 0: #頭なら色はyellow
                pygame.draw.rect(screen, "yellow", (positions[i], (r, r)))
            else:
                pygame.draw.rect(screen, "white", (positions[i], (r, r)))
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key in [K_DOWN, K_UP, K_LEFT, K_RIGHT]:
                    moving = True
                    
                if event.key == K_DOWN:
                    vx, vy = 0, 10
                if event.key == K_UP:
                    vx, vy = 0, -10
                if event.key == K_LEFT:
                    vx, vy = -10, 0
                if event.key == K_RIGHT:
                    vx, vy = 10, 0
                
                #if リンゴを食べたなら(apple == positions[0]):
                    positions.append([positions[-1][0]-r, positions[-1][1]])#positions[-1][0]はpositionsの-1番目に追加する
            if event.type == KEYUP:
                if event.key in [K_DOWN, K_UP, K_LEFT, K_RIGHT]:
                    moving = False
                
        
        if moving:
            for i in range(len(positions)):
                positions[i][0] += vx
                positions[i][1] += vy

        clock.tick(60)

if __name__ == "__main__":
    main()