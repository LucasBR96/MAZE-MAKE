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
   
    parent   = { u : None for u in G.nodes }

    min_cost = HEAP_MIN( len( G.nodes ) )
    root = G.rand_node()
    for u in G.nodes:
        if u == root: continue
        min_cost[ u ] = sys.maxsize
    min_cost[ root ] = 0
    
    A = G.Adj_tab()

    def relax( u , v , c ):

        if c + G.edge_val( u , v ) < min_cost[ v ]:
            min_cost[ v ] = c + G.edge_val( u , v )
            parent[ v ] = u

    while len( min_cost ):

        u , c = min_cost.pop()
        for v in A[ u ]:
            if min_cost[ v ] is None: continue
            relax( u , v , c )

            if u == parent[ v ]: yield ( u , v )

