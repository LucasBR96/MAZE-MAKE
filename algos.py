from data_structures import GRAPH , FCD , HEAP_MIN
import sys
from collections import deque
import random

def DFS( G ):

    A = G.Adj_tab()
    for u in G.nodes:
        A[ u ].sort( key = lambda v : G.edge_val( u , v ) )

    pivot = G.rand_node()
    unvisited = G.nodes - { pivot }

    stack = [ pivot ]
    while stack:

        x = stack[ -1 ]
        if not A[ x ]:
            stack.pop()
            continue
        
        y = A[ x ].pop()
        if y not in unvisited:
            continue

        stack.append( y )
        unvisited.discard( y )

        yield ( x , y )
    
def WFS( G ):

    A = G.Adj_tab()
    for u in G.nodes:
        A[ u ].sort( key = lambda v : G.edge_val( u , v ) )
        # random.shuffle( A[ u ] )

    pivot = G.rand_node()
    parents = { x:None for x in G.nodes }

    queue = deque( [ pivot ] )
    while queue:

        x = queue.popleft()
        if not( parents[ x ] is None ):
            yield ( x , parents[ x ] )
            
            
        for v in A[ x ]:
            if parents[ v ] is None:
                parents[ v ] = x
                queue.append( v )
    
def Kruskal( G ):
    
    F = FCD( len( G.nodes ) )
    for u in G.nodes:
        F.make_set( u )
    
    edge_list = list( G.edges.keys() )
    edge_list.sort( key = lambda e : G.edge_val( e[ 0 ] , e[ 1 ] ) )
    for u , v in edge_list:

        A = F[ u ]
        B = F[ v ]
        if A != B:
            F.merge( A , B )
            yield ( u , v )
    
def Dijkstra( G ):
   
    root = G.rand_node()
    H = HEAP_MIN( n = len( G.nodes ) )
    parents = dict()

    for u in G.nodes:
        H[ u ] = sys.maxsize
        parents[ u ] = None
    H[ root ] = 0

    A = G.Adj_tab()
    
    def relax( u , v ):

        if H[ u ] + G.edge_val( u , v ) < H[ v ]:
            H[ v ] = G.edge_val( u , v ) + H[ u ]
            parents[ v ] = u
            return True
        return False
    
    while len( H ):

        u , _ = H.minimum()
        if not ( parents[ u ] is None ):
            yield u , parents[ u ]

        for v in A[ u ]:
            if H[ v ] is None:
                continue 
            relax( u , v )
        H.pop()




            

