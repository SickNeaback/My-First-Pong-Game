#Nicks First Pong Game

#import pygame also sys to exit the game
import pygame, sys

#initialize pygame
pygame.init()

#set the screen size
screen_width = 1280
screen_height = 800

#creates the screen with the screen size
#center point is 640,400
screen = pygame.display.set_mode((screen_width, screen_height))
#set a title with caption
pygame.display.set_caption("Nick's First Pong Game")

#create a clock object
clock = pygame.time.Clock()
#basics now complete

#now lets work on game loop
#loop is like a heart beat

#Draw 1st object
ball = pygame.Rect(0,0,30,30)
ball.center = (screen_width/2, screen_height/2)

#HEARTBEAT OF THE GAME BEGINS
while True:
    #check for events
    for event in pygame.event.get():
        #if event is quit or closed
        if event.type == pygame.QUIT:
            #exit the game
            pygame.quit()
            sys.exit()
    screen.fill('black')

    #Draw the game objects
    #at first we had rect function but now changed to ellipse to round the ball
    pygame.draw.ellipse(screen, 'white', ball)

    #update the display
    pygame.display.update()
    #set the FPS boi
    # #60 good for now
    clock.tick(60)    

#Now run the game we have a small white square in the center! Wooohoooo!


