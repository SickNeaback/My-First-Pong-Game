#Nicks First Pong Game v1
#I am following this tutorial https://www.youtube.com/watch?v=5NkTzvMchMw

#import pygame also sys to exit the game
import pygame, sys , random 
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = screen_width/2 -10
    ball.y = random.randint(10,100)
    ball_speed_x *= random.choice([-1,1])
    ball_speed_y *= random.choice([-1,1])
def point_won(winner):
    global cpu_points, player_points

    if winner == "CPU":
        cpu_points += 1
    if winner == "Player":
        player_points += 1 
    reset_ball()  

def animate_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1
    if ball.right >= screen_width:
        point_won("CPU")
    if ball.left <= 0:
        point_won("Player")
    if ball.colliderect(player) or ball.colliderect(cpu):
        ball_speed_x *= -1
def animate_player():
    player.y += player_speed

    #Make sure the paddles don't go off the screen
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def animate_cpu():
    #Declate global to make work lol this took forever to figure out
    global cpu_speed
    cpu.y += cpu_speed
    
    if ball.centery <= cpu.centery:
        cpu_speed = -6
    if ball.centery >= cpu.centery:
        cpu_speed = 6
    if cpu.top <= 0:
        cpu.top = 0
    if cpu.bottom >= screen_height:
        cpu.bottom = screen_height

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


#Create the paddles now
cpu = pygame.Rect(0,0,20,100)
#Lets move the paddle down a little
cpu.centery = screen_height/2

#Creat player paddle left 
player = pygame.Rect(0,0,20,100)

#Change midright value right paddle
player.midright = (screen_width, screen_height/2)

#Animation Section
ball_speed_x = 4
ball_speed_y = 4
player_speed = 0
cpu_speed = 6

#Player Score
cpu_points, player_points = 0, 0

score_font = pygame.font.Font(None, 100)

#HEARTBEAT OF THE GAME BEGINS
while True:
    #check for events
    for event in pygame.event.get():
        #if event is quit or closed
        if event.type == pygame.QUIT:
            #exit the game
            pygame.quit()
            sys.exit()
        #Move the player paddle up and down using the keyboard
        if event.type == pygame.KEYDOWN:
            #Player has pressed a key down but which one?
            #Check constants for key values online
            if event.key == pygame.K_UP:
                player_speed = -6
            if event.key == pygame.K_DOWN:
                player_speed =6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed = 0
            if event.key == pygame.K_DOWN:
                player_speed =0    
    #Draw the background but also clear the screen
    screen.fill('black')

    #Moves the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    #Make the ball bounce off the top and bottom of the screen 
    animate_ball()
    animate_player()
    animate_cpu()

    #Draw the game objects
    #Score 
    cpu_score_surface = score_font.render(str(cpu_points), True, "white")
    player_score_surface = score_font.render(str(player_points), True, "white")  
    screen.blit(cpu_score_surface, (screen_width/4,20))
    screen.blit(player_score_surface, (3*screen_width/4,20))
    #Draw a line that seperates the screen 2 sides
    pygame.draw.aaline(screen, 'white', (screen_width/2, 0), (screen_width/2, screen_height))
    #At first we had rect function but now changed to ellipse to round the ball
    pygame.draw.ellipse(screen, 'white', ball)
    #Draw CPU paddle
    pygame.draw.rect(screen, 'white', cpu)
    pygame.draw.rect(screen, 'white', player)


    #update the display
    pygame.display.update()
    #set the FPS boi
    # #60 good for now
    clock.tick(60)    



#Nick Foot Notes 
#Now run the game we have a small white square in the center! Wooohoooo!
#Lets go got a center line now
#Moving onto animation time 
#Just made the ball bounce around and it remind me of the DVD logo bouncing around the screen
#My next goal is to make a DVD logo bounce clone program
#Moving onto AI paddle now
#Created a AI CPU sick
#Moving onto collision now, the cpu_speed had me almost crashing out
#Last but not least, scoring to end it off