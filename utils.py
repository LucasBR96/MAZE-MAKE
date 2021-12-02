from itertools import product

from algos import *
from data_structures import *
from constantes import *

def solution_generator( G , algo ):

    foo = Kruskal
    if algo == DIJKSTRA:
        foo = Dijkstra
    elif algo == RND_DFS:
        foo = DFS

    return foo( G )

def maze_init( seed ):

    random.seed( seed )
    G = GRAPH()

    for p in product( range( COLS ) , range( ROWS ) ):

        G.nodes.add( tuple( p ) )

        x , y = p
        p1 = ( x + 1 , y )
        p2 = ( x , y + 1 )
    
        q = 0 if random.random() < BIAS else 1
        if x + 1 < COLS:
            G.add_edge( p , p1 , q )
        if y + 1 < ROWS:
            G.add_edge( p , p2 , 1 - q ) 
    
    return G