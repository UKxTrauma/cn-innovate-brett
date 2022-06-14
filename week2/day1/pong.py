import pygame, sys, random, math
from pygame.locals import *

###general setup###
pygame.init()
# initiates all pygame modules
#reuired in all pygame projects
clock = pygame.time.Clock()
#variable clock
screen_width = 1920
screen_height = 1080
#screen size
screen = pygame.display.set_mode((screen_width, screen_height))
#screen creation
table = pygame.display.set_mode((1920, 1080))
#------------------------------
pygame.display.set_caption("Air Hockey")
#------------------------------

###Game rectangles###
# puck = pygame.Rect(30, 30) # <=== previous line, replaced on line 24 #
#takes x & y position & the height and width of the rect#
#(the puck is 30px high and 30 px wide)#
puck = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
#screen widht and height divided by 2 and then minus half of puck size#
player = pygame.Rect(screen_width - 150, screen_height/2 - 50, 100, 100)
#defining siz eof player and it's position#
#10px wide and 140px height#
#setting player to top left (-20)#
#screen_height is /2 and then - half the player height (140)#
opponent = pygame.Rect(50, screen_height/2 - 50, 100, 100)
#same height as player#
#positioned left of screen#
l_goal = pygame.Rect(0, screen_height/2 - 200, 10, 400)
r_goal = pygame.Rect(screen_width -10, screen_height/2 - 200, 10, 400)
top_boost = pygame.Rect(screen_width/2 - 620, 0, 1240, 10)
bottom_boost = pygame.Rect(screen_width/2 - 620, screen_height -10, 1240, 10)

###Colours###
white = ('white')
orange = pygame.Color('orange')
blue = pygame.Color('blue')
black = pygame.Color('black')
red = pygame.Color('red')

###animation###
puck_speed_x = 7 * random.choice((1, -1))
puck_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

def puck_animation():
    global puck_speed_x, puck_speed_y, l_goal, r_goal
    puck.x += puck_speed_x
    puck.y += puck_speed_y
    #if the puck hits the top or the bottom, reverse vertical path#
    if puck.top <= 0 or puck.bottom >= screen_height:
        puck_speed_y *= -1
    #if the puck hits the top or the bottom, reverse horizontal path#
    if puck.left <= 0 or puck.right >= screen_width:
        puck_speed_x *= -1
    if puck.colliderect(l_goal):
        puck_restart()
    if puck.colliderect(r_goal):
        puck_restart()
    #reverse horizontal speed if the puck collides with player or opponent
    if puck.colliderect(player) or puck.colliderect(opponent):
        puck_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.top < puck.y:
        opponent.top += opponent_speed
    if opponent.bottom > puck.y:
        opponent.bottom -= opponent_speed
    #---------------------
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def puck_restart():
    global puck_speed_x, puck_speed_y
    puck.center = (screen_width/2, screen_height/2)
    puck_speed_y *= random.choice((1, -1))
    puck_speed_x *= random.choice((1, -1))

###While loop###
while True:
    #user input handling
    for event in pygame.event.get():
        #all user input is classed as an ebent in pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #checks to see if the 'x' has been clicked by user
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    puck_animation()
    player_animation()
    opponent_animation()
    ###Visuals###        
    screen.fill(black)
    pygame.draw.rect(table, black, pygame.Rect(30, 30, 60, 60), 2, 3)
    table.fill(white)
    pygame.draw.aaline(screen, black, (screen_width/2,0), (screen_width/2,screen_height))
    pygame.draw.arc(screen, black, (0, 0, 680, 680), math.pi/2, math.pi, width=10)
    pygame.draw.arc(screen, black, (0, 400, 680, 680), -math.pi, -math.pi/2, width=10)
    pygame.draw.arc(screen, black, (1240, 0, 680, 680), math.pi*2, math.pi/2, width=10)
    pygame.draw.arc(screen, black, (1240, 400, 680, 680), -math.pi/2, -math.pi*2, width=10)
    pygame.draw.rect(screen, red, top_boost)
    pygame.draw.rect(screen, red, bottom_boost)
    pygame.draw.rect(screen, blue, r_goal)
    pygame.draw.rect(screen, orange, l_goal) 
    pygame.draw.ellipse(screen, black, puck)
    pygame.draw.ellipse(screen, blue, player)
    pygame.draw.ellipse(screen, orange, opponent)
    #ellipse uses it's own frame to draw an ellipse#
    #because all sides are same size, ellipse becomes a circle#

    #draw line down centre of screen, aaline stands for anti-alias line#
    # pygame.draw.rect(screen, color = pygame.Color('white'), rect = (1920, 1080, -1920, -1080), width = 30, border_radius = 300)
    #(display, color, start point, end point)#
    #start point is 1/2 screen width, with 0 being middle of top window#
    #end point is 1/2 screen width and screen height, (middle of bottom window)#

    pygame.display.flip()
    #draws pic from everything found in the while loop#
    clock.tick(60)
    #limits how fast the loop runs#

# l_goal = pygame.Rect(0, screen_height/2 - 70, 10, 250)
# r_goal = pygame.Rect(screen_width -10, screen_height/2 - 125, 10, 250)