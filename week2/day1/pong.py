import pygame, sys


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
#------------------------------

pygame.display.set_caption("PONG")