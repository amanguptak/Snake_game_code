import pygame
from pygame.locals import *
import time
import random
size=40
Backgc =63, 54, 151
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
        self.x=random.randint(0,31)*size
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
       #self.ances.fill((Backgc))
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
        pygame.mixer.init()
        self.suface = pygame.display.set_mode((1280,800))
        #self.suface.fill((Backgc))
        self.snake= Snake(self.suface, 1)
        self.snake.draw()
        self.apple=Apple(self.suface)



    def renderbcg(self):
      bg=pygame.image.load("resourse/backg.jpg")
      self.suface.blit(bg,(0,0))


#collison concept
    def collison(self,x1,y1,x2,y2):
         if x1 >= x2 and x1 < x2+size:
             if y1 >= y2 and y1 < y2 + size:
                return True
         return False


    def score(self):
        font=pygame.font.SysFont('Courier',35,bold=True)
        #for displaying the score

        scorec =font.render(f"Score: {self.snake.length*10}",True,(207, 0, 0))
        self.suface.blit(scorec,(1000,5))

    def play(self):
        self.renderbcg()
        self.snake.walk()
        self.apple.draw()
        self.score()
        pygame.display.flip()
        if self.collison(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            sound =pygame.mixer.Sound("resourse/eata.wav")
            pygame.mixer.Sound.play(sound)

            self.snake.increselength()

            self.apple.move()

      #sake_collied_itself
        for i in range(3,self.snake.length):
            if self.collison(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                sound = pygame.mixer.Sound("resourse/gameo.wav")
                pygame.mixer.Sound.play(sound)
                raise "Game over"

    def game_over(self):
            self.renderbcg()
            font=pygame.font.SysFont('arila',30)
            line1=font.render(f"Game is over ! your score{self.snake.length*10}",True,(255,255,255))
            self.suface.blit(line1,(200,300))
            line2 = font.render(f"to play again press enter .for exit press Escape!", True, (255, 255, 255))
            self.suface.blit(line2, (200, 350))
            pygame.display.flip()
            pass
    def reset(self):
     self.snake=Snake(self.suface,1)


     self.apple = Apple(self.suface)
    def run(self):
         running = True
         pause=False
         while running:
             for event in pygame.event.get():
                 if event.type== KEYDOWN:
                     if event.key==K_ESCAPE:
                         running= False
                     if event.key == K_RETURN:
                         pause = False
                     if not pause:

                      if event.key==K_LEFT:
                         self.snake.movel()
                      if event.key == K_RIGHT:
                         self.snake.mover()
                      if event.key == K_UP:
                         self.snake.moveu()
                      if event.key == K_DOWN:
                            self.snake.moved()

                 elif event.type == QUIT:
                     running = False


             try:
               if not pause:
                self.play()
             except Exception as e:
                self.game_over()
                pause=True
                self.reset()

             time.sleep(0.2)


if __name__== "__main__":
    game=Game()
    game.run()
