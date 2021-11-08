import random
from algos import *
from data_structures import *

import pygame
from pygame.locals import *

import sys
import time

ROWS = 0
COLS = 0
TILE = 10
SLEEP_TIM = 0

KRUSKAL = 0
PRIM    = 1

PAUSED = True

def solution_generator( V , E , algo ):

    G = GRAPH()
    G.edges = E
    G.nodes = V

    for u , v in algo( G ):
        yield u , v
    
def draw_maze( surf , u , v )
    
    i , j = u//COLS , u%COLS
    p1 = ( TILE*( i + 1 ) , TILE*( j + 1) )

    i , j = v//COLS , v%COLS
    p2 = ( TILE*( i + 1 ) , TILE*( j + 1) )

    pygame.draw.line( surf , ( 255 , 255 , 255 ) , p1 , p2 )

def maze_init( row , col , seed ):

    global ROWS , COLS
    ROWS = row
    COLS = col

    random.seed( seed )
    vertices = set()
    edges = dict()

    for k in range ( row*col ):
        vertices.add( k )

        i , j = k//col , k%col
        if i < row - 1:
            edges[ ( k , k + col ) ] = random.random()

        if j < col - 1:
            edges[ ( k , k + 1 ) ] = random.random()
    return vertices , edges

def update_maze( ):

    if PAUSED: return

    global E
    for x in range( speed ):
        try:
            _ , E = next( animo )
        except StopIteration:
            continue

def main( args ):
    
    global ROWS , COLS, E, speed, animo 

    ROWS , COLS , seed , algo = map( int , args )
    # ROWS , COLS , seed , algo = 80, 160, 87, 1
    ROWS , COLS = COLS , ROWS
    V , E = maze_init( ROWS , COLS , seed )
    animo = solution_generator( V , E , algo )
    E = set()
    speed = 7
    pygame.init()
    surf = pygame.display.set_mode( ( (ROWS+1)*TILE , (COLS+1)*TILE ) )

    while True:

        surf.fill( ( 0 , 0 , 0 ) )
        
        update_maze( )
        draw_maze( surf , E )

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()
                return
            if event.type == KEYUP and event.key == K_LEFT:
                speed = min( speed + 1 , 10 )
                print( speed )
            
            if event.type == KEYUP and event.key == K_RIGHT:
                speed = max( speed - 1 , 1 )
                print( speed )
            
            if event.type == KEYUP and event.key == K_SPACE:
                global PAUSED
                PAUSED = not PAUSED

        time.sleep( SLEEP_TIM )
        pygame.display.update()

if __name__ == "__main__":
    main( sys.argv[ 1: ] )
