import pygame
import random
#pygame -> module
#initialize
#start pygame
def color():
    return random.randint(0,255)
pygame.init()

#set 
#name of the game
#vriable storing data
name="My new game!"
#caption -> title
#wgy are we using the dots?
#pygame == actual complete game
#pygame.display -> actually setting the value inside pygame
#pygame {} -> disply-> caption
pygame.display.set_caption(name)
#no new screen ?
# print(pygame.QUIT)
#0.00000000603 10 to the power -8
#tuple? , more than two number and emmpty . It can't be modified
screen=pygame.display.set_mode((500,500)) #(height,width) #pixels 
#returns a screen
#fill solid colors
#tuple-> (red,green,blue)
#blue 0-255
#hexadecimal? 0-9 and A-F #0088ff
#why ff=255?
# f*64+f*0-> formula to convert from hexa to decimal 
#f=16 right
#hexadecimal -> 0-9 digits, A=11, B=12, C=13, D=14, E=15, F=16
# add your changes into the screen
#updates

# screen.fill((255,0,255)) #reddish blue
# pygame.display.update()
#why color is not changing
#flip wipes entire screen
#update just make the updates
#forecfully update the screen
#reference form your laptop
#1980/1080
#difference 
#as soon as i open pygame it closes itself
#why?
# we have to make the process keep running
#var
loop=True
#you can store function into variables but cannot use them exactly same
#we will have to onnect our loop and pygame
#pygame -> interact -> event
# if this event is not quit -> keep running
#list of events 
#background 
#screen 
#we move cursor and color gets changed
#image
#create a screen

#blit copies your image on the screen
#image and coordinates
#we load the image , we didn't set it , on the screen
#creating a cricle
#initial positions
xpos=250
ypos=250
speed=10
while loop:
    for event in pygame.event.get():
        # print(pygame.mouse.get_pos()) #position of cursor
        position=pygame.mouse.get_pos() #position
        
        #This reduces the image size and returns  a new image
        
        # screen.fill((color(), color(), color()))
        if event.type==pygame.QUIT:
            loop=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("Pressed LEft key")
                xpos-=speed
            if event.key==pygame.K_RIGHT:
                print("Pressed Right key")
                xpos+=speed
            if event.key==pygame.K_UP:
                print("Pressed Up key")
                ypos-=speed
            if event.key==pygame.K_DOWN:
                print("Pressed Down key")
                ypos+=speed
            image=pygame.image.load("rocket-min.png")
            image=pygame.transform.scale(image,(100,100))
            
            screen.blit(image,(xpos,ypos))
            # pygame.draw.circle(screen,(color(),color(),color()),(xpos,ypos),5)
            pygame.display.update()
            screen.fill((0,0,0))


