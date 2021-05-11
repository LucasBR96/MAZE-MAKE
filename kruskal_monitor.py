from data_structures import FCD , GRAPH

#GLOBAL VARIABLE VISIBLE BY FILE ONLY ------------------------------------------------
END      = -1
SELECT   = 0
CONSIDER = 1
UPDATE   = 2
global_status = SELECT

E_prime = []
T = FCD(10**5)

#GLOBAL VARIABLE VISIBLE BY OUTSIDERS------------------------------------------------
CONSIDERED = 0
REJECTED   = 1
ACCEPTED   = 2
edge_status = CONSIDERED
current_edge = ( -1 , -1 )

Va = set()
Ea = set()
UNVISITED = set()

N = 0
pos = 0 

#MONITOR FUNCTIONS------------------------------------------------------------------
def _select_fun():

    global current_edge, edge_status, global_status
    current_edge  = E_prime[ pos ]
    edge_status   = CONSIDERED
    global_status = CONSIDER

def _consider_fun( ):

    global edge_status, global_status
    ( x , y ) = current_edge
    r1 = T[ x ]
    r2 = T[ y ]
    edge_status = REJECTED 
    if r1 != r2: 
        edge_status = ACCEPTED
        T.merge( x , y )
    global_status = UPDATE

def _update_fun( ):

    global Va, Ea, current_edge, edge_status, T, global_status, UNVISITED
    if edge_status == ACCEPTED:
        ( x , y ) = current_edge
        Va.add( x )
        Va.add( y )
        Ea.add( ( x , y ) )
        
        UNVISITED -= { x , y }
    
    global pos , N
    pos = pos + 1
    global_status = SELECT if UNVISITED else END

def _init( V , E ):

    global E_prime , N
    E_prime = [ tup for tup in E ]
    E_prime.sort( key = lambda x : E[ x ] )
    N = len( E_prime )

    global T, UNVISITED
    for x in V: T.make_set( x )
    UNVISITED = V.copy()    

def _next( ):

    if global_status == END:
        return False

    if global_status == SELECT:
        _select_fun()
    elif global_status == CONSIDER:
        _consider_fun()
    elif global_status == UPDATE:
        _update_fun()
    return True

def get_variables():

    return( edge_status , current_edge , Va.copy() , Ea.copy() )