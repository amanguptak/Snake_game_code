import pygame
from pygame.locals import *
import time
class Snake:
    def __init__(self,ances):
        self.ances=ances
        self.block=pygame.image.load("resourse/sb.png").convert()
        self.x=100
        self.y=100
        self.direction = 'down'
    def draw(self):
        self.ances.fill((201, 188, 167))
        self.ances.blit(self.block, ((self.x, self.y)))
        pygame.display.flip()


    def movel(self):
        self.direction='left'

    def mover(self):
        self.direction='right'

    def moved(self):
        self.direction = 'down'

    def moveu(self):
        self.direction = 'up'

    def walk(self):
     if self.direction=='up':
         self.y-=10
     if self.direction=='down':
         self.y+=10
     if self.direction=='left':
         self.x-=10
     if self.direction=='right':
         self.x+=10
     self.draw()

class Game:

    def __init__(self):
        pygame.init()
        self.suface = pygame.display.set_mode((1000,800))
        self.suface.fill((201, 188, 167))
        self.snake= Snake(self.suface)
        self.snake.draw()

    def run(self):
         running = True

         while running:
             for event in pygame.event.get():
                 if event.type== KEYDOWN:
                     if event.key==K_ESCAPE:
                         running= False

                     if event.key==K_LEFT:
                         self.snake.movel()
                     if event.key == K_RIGHT:
                         self.snake.mover()
                     if event.key == K_UP:
                         self.snake.moveu()
                     if event.key == K_DOWN:
                            self.snake.moved()

             self.snake.walk()
             time.sleep(0.3)


if __name__== "__main__":
    game=Game()
    game.run()