
import pygame
from pygame.locals import *
import time
import random
size=40

class Apple:
    def __init__(self, ances):
        self.ances=ances
        self.image=pygame.image.load("resourse/fish.png").convert()
        self.x=size*3
        self.y=size*3

    def draw(self):
        self.ances.blit(self.image, (self.x, self.y))
        pygame.display.flip()
    def move(self):
        self.x=random.randint(0,24)*size
        self.y = random.randint(0, 19) * size

class Snake:
    def __init__(self, ances, length):
        self.length=length
        self.ances=ances
        self.block=pygame.image.load("resourse/ghgjh.jpg").convert()
        self.x=[size]*length
        self.y=[size]*length
        self.direction = 'down'


    def increselength(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)



    def draw(self):
       self.ances.fill((63, 54, 151))
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
#in this line we move block at the postion of previous block like at the place of 8 , 9 will come
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
        self.suface.fill((63, 54, 151))
        self.snake= Snake(self.suface, 1)
        self.snake.draw()
        self.apple=Apple(self.suface)

#collison concept
    def collison(self,x1,y1,x2,y2):
         if x1 >= x2 and x1 < x2+size:
             if y1 >= y2 and y1 < y2 + size:
                return True
         return False


    def score(self):
        font=pygame.font.SysFont('arial',35)
        #for displaying the score

        scorec =font.render(f"Score: {self.snake.length*10}",True,(255, 255, 255))
        self.suface.blit(scorec,(800,5))

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.score()
        pygame.display.flip()
        if self.collison(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increselength()
            self.apple.move()
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

             self.play()
             time.sleep(0.3)


if __name__== "__main__":
    game=Game()
    game.run()
