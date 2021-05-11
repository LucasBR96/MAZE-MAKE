from collections import deque
from data_structures import HEAP_MIN , GRAPH
from sys import maxsize

#GLOBAL VARIABLE VISIBLE BY FILE ONLY ------------------------------------------------
END      = -1
SELECT   = 0
CONSIDER = 1
UPDATE   = 2
global_status = SELECT

FUN_DICT = dict( )
# UNVISITED = set( )

Adj_lst = dict()
P = dict()
H = HEAP_MIN( 10**6 )

#GLOBAL VARIABLE VISIBLE BY OUTSIDERS------------------------------------------------
CONSIDERED = 0
REJECTED   = 1
ACCEPTED   = 2
edge_status = CONSIDERED
current_edge = ( -1 , -1 )

A = GRAPH()
G = GRAPH()

#MONITOR FUNCTIONS------------------------------------------------------------------

def _select_fun():

    global global_status
    global_status = CONSIDER if H else END

def _consider_fun():

    global global_status
    global_status = UPDATE

def _update_fun():

    x , _  = H.pop()
    for y in Adj_lst[ x ]:
        a = -1 if H[ y ] is None else H[ y ]
        if G.edge_val( x , y ) < a:
            H[ y ] = G.edge_val( x , y )
            P[ y ] = x
    
    A.add_node( x )
    y = P[ x ]
    if not( y is None ):
        A.add_node( y )
        w = G.edge_val( x , y )
        A.add_edge( x , y , w )

    global global_status
    global_status = SELECT

def _init( V , E ):

    FUN_DICT[ SELECT ]   = _select_fun
    FUN_DICT[ CONSIDER ] = _consider_fun
    FUN_DICT[ UPDATE ]   = _update_fun

    G.nodes = V
    G.edges = E

    global Adj_lst, H , P
    Adj_lst = G.Adj_tab()
    for x in G.nodes:
        H[ x ] = maxsize
        P[ x ] = None
    root = G.rand_node()
    H[ root ] = 0 


def get_variables():

    return( A.nodes , A.edges )

def _next():

    if global_status == END:
        return False

    f = FUN_DICT[ global_status ]
    f()
    return True

if __name__ == "__main__":

    V = set( ["a" , "b" , "c" , "d", "e" ] )
    E = {
        ('a','b'):2,
        ('a','c'):3,
        ('a','d'):4,
        ('c','d'):1,
        ('b','d'):2,
        ('d','e'):7,
        ('c','e'):3,
        ('a','e'):2
    }

    _init( V , E )
    while _next():
        if global_status == UPDATE:
            input()
            print( "-"*25 )
            print( A )
    print( A )
    pass