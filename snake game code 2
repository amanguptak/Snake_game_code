import pygame
from pygame.locals import *
import time
size=38
class Snake:
    def __init__(self, ances, length):
        self.length=length
        self.ances=ances
        self.block=pygame.image.load("resourse/sb.png").convert()
        self.x=[size]*length
        self.y=[size]*length
        self.direction = 'down'

    def draw(self):
       self.ances.fill((201, 188, 167))
       for i in range(self.length):
           self.ances.blit(self.block, (self.x[i], self.y[i]))
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

     for i in range(self.length-1,0,-1):
         self.x[i]=self.x[i - 1]
         self.y[i] = self.y[i - 1]



     if self.direction=='up':
         self.y[0]-=size
     if self.direction=='down':
         self.y[0]+=size
     if self.direction=='left':
         self.x[0]-=size
     if self.direction=='right':
         self.x[0]+=size
     self.draw()

class Game:

    def __init__(self):
        pygame.init()
        self.suface = pygame.display.set_mode((1000,800))
        self.suface.fill((201, 188, 167))
        self.snake= Snake(self.suface, 2)
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
