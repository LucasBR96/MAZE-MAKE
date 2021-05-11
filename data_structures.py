from collections import deque
import random
import sys

class GRAPH:

    def __init__( self ):
        self.nodes = set()
        self.edges = dict()
    
    def __str__( self ):

        s_nodes = "nodes: " + " ".join( str( x ) for x in self.nodes )
        s_edges = "edges: "
        for ( x , y ) , w in self.edges.items():
            s_iter = "{} | {} -> {}".format( x , y , w )
            s_edges += "\n" + s_iter
        
        return s_nodes + "\n\n" + s_edges

    def add_node( self , x ):
        self.nodes.add( x )
    
    def add_edge( self , u , v , w ):
        self.edges[ ( u , v ) ] = w
    
    def dim( self ):
        N = len( self.nodes )
        M = len( self.edges )
        return N , M
    
    def edge_val( self , u , v ):

        if ( u , v ) in self.edges:
            return self.edges[ ( u , v ) ]
        
        if ( v , u ) in self.edges:
            return self.edges[ ( v , u ) ]
        
    def Adj_tab( self ):

        A = dict()
        for u , v in self.edges:
            A[ u ] = A.get( u , [] ) + [ v ]
            A[ v ] = A.get( v , [] ) + [ u ]
        return A
    
    def rand_node( self ):
        return random.choice( list( self.nodes ) )

class FCD:

    def __init__( self, max_elements ):

        self.keys = set()
        self.parents = dict()
        self.rank    = dict()

        self.t = 0
        self.max_elem = max_elements

        self.full = lambda : ( self.t >= self.max_elem )

    def make_set( self , x ):

        if self.full():
            return False

        self.t += 1
        self.keys.add( x )
        self.parents[ x ] = x
        self.rank[ x ] = 0
        return True

    def _push( self , x ):

        par = [ x ]
        while True:
            pos = par.pop()
            y = self.parents[ pos ]
            if y == pos:
                root = y
                break
            par.append( pos ) 
            par.append( y ) 

        rk_sum = 0 
        for i , x in enumerate( par[ : -1 ] ):
            self.parents[ x ] = root
            aux = self.rank[ x ]
            self.rank[ x ] -= rk_sum
            rk_sum += aux + 1

    def __getitem__( self , x ):
        if self.parents[ x ] == x: return x
        self._push( x )
        return self.parents[ x ]
    
    def merge( self , x , y ):

        x = self[ x ]
        y = self[ y ]

        r1 , r2 = self.rank[ x ] , self.rank[ y ]
        t = x if r1 > r2 else y
        t_men = y if t == x else x

        self.parents[ t_men ] = t
        self.rank[ t ] = r1 + r2 + 1
    
class HEAP_MIN:

    def __init__( self , n = 10**3 ):

        self.key2val = dict()
        self.key2rank = dict()
        self.rank2key = dict()
        self.max_size = n
        self.total = 0
    
    def __getitem__( self , k ):
        return self.key2val.get( k , None )
    
    def __setitem__( self , k , val ):

        if not( k in self.key2val ) and self.total >= self.max_size:
            return False
        
        if not( k in self.key2val ):

            self.total += 1
            t = self.total
            self.key2rank[ k ] = t
            self.rank2key[ t ] = k

        old = self.key2val.get( k , sys.maxsize )
        self.key2val[ k ] = val

        fun = self._up
        if val >= old:
            fun = self._down

        fun( k )
        return True
    
    def __len__( self ): return self.total

    def pop( self ):

        u = self.rank2key[ 1 ]
        val = self.key2val[ u ]
        self.key2val.pop( u )
        self.key2rank.pop( u )
        
        v = self.rank2key[ self.total ]
        self.rank2key.pop( self.total )
        self.total -= 1

        if self.total != 0: 
            self.rank2key[ 1 ] = v
            self.key2rank[ v ] = 1

            self._down( v )
            
        return ( u , val )

    def _up( self , k ):
        
        val = self.key2val[ k ]
        rank = self.key2rank[ k ]
        while rank != 1:

            parent_rank = rank//2
            parent_key = self.rank2key[ parent_rank ]
            parent_val = self.key2val[ parent_key ]

            if parent_val <= val:
                break

            parent_rank , rank = rank , parent_rank 
            self.key2rank[ k ] = rank
            self.rank2key[ rank ] = k
            self.key2rank[ parent_key ] = parent_rank
            self.rank2key[ parent_rank ] = parent_key

    def _down( self , k ):
        
        val = self.key2val[ k ]
        rank = self.key2rank[ k ]
        while rank <= self.total//2:

            smallest = k

            right_rank = 2*rank
            right_key = self.rank2key[ right_rank ]
            right_val = self.key2val[ right_key ]
            if right_val < val:
                smallest = right_key
             
            left_rank = min( right_rank + 1 , self.total)
            left_key = self.rank2key[ left_rank ]
            left_val = self.key2val[ left_key ]
            if left_val < self.key2val[ smallest ]:
                smallest = left_key
            
            if smallest == k: break

            smallest_rank = self.key2rank[ smallest ]
            smallest_rank , rank = rank , smallest_rank 
            self.key2rank[ k ] = rank
            self.rank2key[ rank ] = k
            self.key2rank[ smallest ] = smallest_rank
            self.rank2key[ smallest_rank ] = smallest
