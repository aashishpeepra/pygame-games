import pygame
import time
pygame.init()
import random

pygame.display.set_caption("First game!")

screen=pygame.display.set_mode((500,500))
print("loading")
image=pygame.image.load("rocket-min.png")
image.set_colorkey((255,0,255))
image=pygame.transform.scale(image,(100,100))
screen.fill((00,64,255))
screen.blit(image,(200,250))

pygame.display.flip()
print("loaded")
running=True
xpos=50
ypos=50
speed=-10
def move():
    global xpos
    global ypos
    global speed
    print(xpos,ypos)
    if xpos>450 or xpos<0:
        xpos-=xpos
    if ypos>450 or ypos<0:
        ypos-=ypos
    xpos+=0
    ypos+=random.randint(5,20)
    screen.fill((00,64,255))
    screen.blit(image,(xpos,ypos))
    pygame.display.flip()
def letsMove():
    time.sleep(0.1)
    move()

while True:
    letsMove()
while running:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            running=False

