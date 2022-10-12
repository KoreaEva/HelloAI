import pygame
import sys

FPS = 60
MAX_WIDTH = 400
MAX_HEIGHT = 600

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("space")
                    
        clock.tick(FPS) 
        screen.fill((255, 255, 255))
        
        pygame.display.update()

if __name__ == '__main__':
    main()