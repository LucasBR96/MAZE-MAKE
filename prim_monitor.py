from collections import deque
from data_structures import HEAP_MIN , GRAPH

#GLOBAL VARIABLE VISIBLE BY FILE ONLY ------------------------------------------------
END      = -1
SELECT   = 0
CONSIDER = 1
UPDATE   = 2
global_status = SELECT
Possible_neighbors = deque([])
Adj_lst = dict()
E_val = dict()

#GLOBAL VARIABLE VISIBLE BY OUTSIDERS------------------------------------------------
CONSIDERED = 0
REJECTED   = 1
ACCEPTED   = 2
edge_status = CONSIDERED
current_edge = ( -1 , -1 )
Va = set()
Ea = set()

#AUXILIARY FUNCTIONS ---------------------------------------------------------------
def intercal( arr1 , arr2 , foo ):

    i , j = 0 , 0
    seq = []

    while i < len( arr1 ) or j < len( arr2 ):

        if i >= len( arr1 ):
            seq.append( arr2[ j ] )
            j += 1
        elif j >= len( arr2 ):
            seq.append( arr1[ i ] )
            i += 1
        elif foo( arr1[ i ] ) < foo( arr2[ j ] ):
            seq.append( arr1[ i ] )
            i +=1
        else:
            seq.append( arr2[ j ] )
            j += 1
    
    return seq

#MONITOR FUNCTIONS------------------------------------------------------------------

def _select_fun():

    global Possible_neighbors , current_edge, edge_status , global_status
    current_edge = Possible_neighbors.popleft()
    edge_status = CONSIDERED
    global_status = CONSIDER 

def _consider_fun():

    global edge_status, global_status
    a , b = current_edge
    r1 = a in Va
    r2 = b in Va
    edge_status = ACCEPTED if r1^r2 else REJECTED
    global_status = UPDATE

def _update_fun():

    global global_status
    if edge_status == ACCEPTED:
  
        global Ea, Va
        Ea.add( current_edge )
        ( a , b ) = current_edge
        y = a if b in Va else b
        Va.add( y )

        global Adj_lst, E_val, Possible_neighbors
        new_edges = [ tup for tup in Adj_lst[ y ] if tup != ( a , b ) ]
        Possible_neighbors = deque( intercal( Possible_neighbors , new_edges , lambda x: E_val[ x ] ) )
    
    global_status = END if len( Possible_neighbors ) == 0 else SELECT

def _init( V , E ):

    global E_val
    E_val = E

    E_set = list( tup for tup in E )
    E_set.sort( key = lambda x: E[ x ] )

    global Adj_lst
    for edge in E_set:
        ( a , b ) = edge
        Adj_lst[ a ] = Adj_lst.get( a , [] ) + [ edge ]
        Adj_lst[ b ] = Adj_lst.get( b , [] ) + [ edge ]
    
    global Possible_neighbors , Va, Ea
    Possible_neighbors.extend( Adj_lst[ a ] )
    Va.add( a )

def get_variables():

    return( edge_status , current_edge , Va.copy() , Ea.copy() )

def _next():

    if global_status == END:
        return False

    if global_status == SELECT:
        _select_fun()
    elif global_status == CONSIDER:
        _consider_fun()
    elif global_status == UPDATE:
        _update_fun()
    return True
