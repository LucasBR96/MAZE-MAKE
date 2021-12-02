import random
import sys
import time
from itertools import product

import pygame
from pygame.locals import *

from algos import *
from data_structures import *
from constantes import *
from utils import *

def update_maze( ):

    for _ in range( SPEED ):
        try:
            E.add( next( animo ) )
        except StopIteration:
            break
    
def draw_maze():
    
    for p1 , p2 in E:
        true_points = []
        for p in ( p1 , p2 ):

            x , y = p
            row   = ( x + 1 )*TILE 
            col   = ( y + 1 )*TILE

            true_points.append( ( row , col ) )

        t1 , t2 = true_points
        pygame.draw.line( surf , FOREGROUND_COLOR , t1 , t2 )

def init_globals():

    global surf
    surf = pygame.display.set_mode( ( SCREEN_W , SCREEN_H ) )

    global E
    E = set()

    global animo
    G = maze_init( 115 )
    animo = solution_generator( G , RND_DFS ) 

def main():
    
    init_globals()

    while True:

        update_maze()

        surf.fill( BACKGROUND_COLOR )
        draw_maze()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()

        pygame.display.update()

if __name__ == "__main__":
    main( )
