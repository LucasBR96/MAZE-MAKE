from data_structures import GRAPH , FCD , HEAP_MIN
import sys
from collections import deque

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

    pivot = G.rand_node()
    unvisited = G.nodes - { pivot }

    queue = deque( [ pivot ] )
    while queue:

        x = queue.popleft()
        for y in A[ x ]:
            if y not in unvisited: continue

            yield ( x , y )
            unvisited.discard( y )
            queue.append( y )
    
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
    for u in G.nodes:
        A[ u ].sort( key = lambda v : G.edge_val( u , v ) )
    
    def relax( u , v ):

        if H[ u ] + G.edge_val( u , v ) < H[ v ]:
            H[ v ] = G.edge_val( u , v ) + H[ u ]
            parents[ v ] = u
            return True
        return False
    
    while H:

        u = H.rank2key[ 1 ]
        for v in A[ u ]:

            if H[ v ] is None: 
                continue
            
            if relax( u , v ):
                yield u , v
        
        H.pop()




            

