from collections import deque
import random
import sys

class GRAPH:
    
    #--------------------------------------------------
    # Rudimentary implementation of graph functions as
    # a Class. Represents weighted, undirected graphs.
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
        
        if u > v : u , v = v , u
        if self.edge_val( u , v ) is not None:
            return
        self.edges[ ( u , v ) ] = w
    
    def dim( self ):
        N = len( self.nodes )
        M = len( self.edges )
        return N , M
    
    def edge_val( self , u , v ):

        if ( u , v ) in self.edges:
            return self.edges[ ( u , v ) ]
        
        #--------------------------------------------------
        # ( u , v ) = ( v , u ). To avoid redundancy only ( u , v ) is
        # stored.
        if ( v , u ) in self.edges:
            return self.edges[ ( v , u ) ]
        
        # edge dos not exist
        return None

    def Adj_tab( self ):
        
        #--------------------------------------------------
        # returns the adjency table of the graphs. Each entry
        # is a node, and the nodes of the graph that are conected
        # to it.
        A = dict()
        for u , v in self.edges:
            A[ u ] = A.get( u , [] ) + [ v ]
            A[ v ] = A.get( v , [] ) + [ u ]
        return A
    
    def rand_node( self ):
        return random.choice( list( self.nodes ) )

class FCD:

    def __init__( self, max_elements ):
        
        #--------------------------------------------------
        # This data structure is not very widespread. But it
        # interesting to use in the kruskal algorithm as it 
        # represents a forest of disjoint sets. ( sets where no
        # not two of them have a common value ).

        # Each set is represented by a tree ( hence forest ) and
        # each node of the tree points to its parent node, all the
        # way to the root. Each node has a counter with the number 
        # of nodes of the tree rooted by it. 
        
        # the values themselves. 
        self.keys    = set()

        # who each node point to.
        self.parents = dict()

        # the amount of descendants.
        self.rank    = dict()
        
        # total number of elements
        self.t = 0
        self.max_elem = max_elements

        self.full = lambda : ( self.t >= self.max_elem )

    def make_set( self , x ):

        #---------------------------------------------------
        # adding a new element means creating a new tree

        if self.full():
            return False

        self.t += 1
        self.keys.add( x )
        self.parents[ x ] = x
        self.rank[ x ] = 0
        return True

    def __getitem__( self , x ):
        
        #--------------------------------------------------
        # getting the set which the element belongs, if the element
        # is in the forest.

        if x not in self.keys:
            return None

        if self.parents[ x ] == x: return x
        pivot = self.parents[ x ]
        while pivot != self.parents[ pivot ]:
            pivot = self.parents[ pivot ]
        return pivot

    def flat( self , x ):
        
        if self[ x ] is None or self[ x ] == x:
            return
        
        root = self[ x ]
        rk_sum = 0 
        while selr.parent[ x ] != root
            self.parents[ x ] = root
            aux = self.rank[ x ]
            self.rank[ x ] -= rk_sum
            rk_sum += aux + 1

    
    def merge( self , x , y ):

        self.flat( x )
        self.flat( y )
        r1 , r2 = self.rank[ self[ x ] ] , self.rank[ self[ y ] ]
        t = self[ x ] if r1 > r2 else self[ y ]
        t_men = y if t == x else x

        self.parents[ t_men ] = t
        self.rank[ t ] = r1 + r2 + 1
    
class HEAP_MIN:
    
    #--------------------------------------------------
    # heap min implementation using three dicts. Working that
    # way it can search elements in the heap in O( 1 ) time.
    # 
    # each entry in this heap have three variables:
    #
    # 1 - key: what is actually being stored in the heap, things
    # lik SSNs, Names, Graph nodes, etc.
    #
    # 2 - val: The score for each key. It can be recovered like
    # a dict, and it is used to compute the ...
    #
    # 3 - rank: The position of the pair ( key , val ) in the heap
    def __init__( self , n = 10**3 ):

        self.key2val = dict()
        self.key2rank = dict()
        self.rank2key = dict()
        self.max_size = n
        self.total = 0
    
    def __getitem__( self , k ):
        return self.key2val.get( k , None )
    
    def __setitem__( self , k , val ):
        
        #--------------------------------------------------
        # basically, this data structure is made to look like
        # a dict. So the line:
        #
        # H[ x ] = 100
        #
        # Could mean either "insert x on the heap and set value
        # 100" or "find key x and set value 100". The line bellow is
        # an edge case for insertion: the heap is already full.
        if not( k in self.key2val ) and self.total >= self.max_size:
            return False
        
        #--------------------------------------------------
        # Now it is just adding a new one
        if not( k in self.key2val ):

            self.total += 1
            t = self.total # new rank
            self.key2rank[ k ] = t
            self.rank2key[ t ] = k

        old = self.key2val.get( k , sys.maxsize )
        self.key2val[ k ] = val
        
        #------------------------------------------------
        # Since it is a min heap, if the new value is lesser
        # than the old, it must go up. Down otherwise.
        fun = self._up
        if val >= old:
            fun = self._down

        fun( k )
        return True
    
    def __len__( self ): return self.total
    
    def remove( self , x ):
        
        if self[ x ] is None:
            return
        
        #--------------------------------------------------
        # when removing. The key must be pushed to the bottom
        # of the heap. For that we set its value equal to the
        # max integer of the system
        self[ x ] = sys.maxsize
        t = self.total
        self.total -= 1

        self.rank2key.pop( t )
        self.key2rank.pop( x )
        self.key2val.pop( x )

    def pop( self ):
        
        if self.total == 0: return
        k = self.rank2key[ 1 ]
        v = self.key2val[ k ]

        self.remove( k )
        return ( k , v )

    def _up( self , k ):
        
        val = self.key2val[ k ]
        rank = self.key2rank[ k ]
        while rank != 1:

            parent_rank = rank//2
            parent_key = self.rank2key[ parent_rank ]
            parent_val = self.key2val[ parent_key ]

            if parent_val <= val:
                break
            
            #--------------------------------------------------
            # exchanging ranks, as the parent takes place of 
            # the node
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
