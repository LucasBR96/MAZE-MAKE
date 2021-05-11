# MAZE MAKER

The purpose of this project is the craetion of a simple animation that generates a random maze 
using a MST algorithm.

## What is a MST?

MST stands for *Minimum Spanning Tree*, a classic problem of graph theory. Given a graph **G( V , E )**
that is positive weighted and non-directional, find the subgraph **A( Va , Ea )** in **G** that fits the three
following rules:

* A have all nodes of G, i.e Va == V 
* A is a Tree, i.e have no cicles
* The total weight of A is the smallest possible.

the picture bellow gives a good example:

```
imagem aqui 
```

The two algorithms described bellow are the most known for solving the MST problem.

### Kruskal

The Kruskal aproach seeks to split the graph into many independent trees, then check,
for every edge of **G**, ascending order on weight, if the such edge bridges two distinct
trees of the split. If it does, then the trees are merged back together.

```
MST-KRUSKAL( G , w )

    // 1
    F = DIS-SETS( )
    for v in G.V
        F.MAKE-SET( v )

    // 2
    E' = SORT( G.E , w )

    A = GRAPH( )
    for u , v in E'
        S1 = F.GET-SET( u )
        S2 = F.GET-SET( v )
        if S1 == S2: continue

        // 3
        F.MERGE( S1 , S2 )
        
        // 4
        if not ( v in A.V )
            A.V = A.V + { v }
        if not ( u in A.V )
            A.V = A.V + { u }
        
        A.E = A.E + { ( u , v ) }
    return A
```

1. F is a data structure that represents **disjoint** sets.( where any pair of two sets in F have no 
common element. ) The details regarding its implementation are not really relevant for the project.
But, if you are interested, you can take look at [CORM09] chapter 21, as this is the implementation
used in the project.

2. Sorting the edges in ascending order by weight.

3. If the edge is valid, the sets S1 and S2 must be merged, so no other edge that conects those sets
can be considered valid in the future.

4. At least one of the nodes is not part of A, but it is not known whicht, so it is necessary to check
them both before adding to A in order to avoid duplicate, unless the data structure used to represent
the set of nodes in a Graph already handles this.

The following gif is an example of Kruskal implementation.
```
gif aqui
```

### Prim

The prim approch initializes **A** with a single node of **G**. Also, it creates 
set of candidate nodes, named **S**. At each iteration, **S** will contain the nodes of G
that are not part of **A** yet, but ech one of them have at least one edge that connects them to
A. So at each iteration the node with the smallest weight is removed from S and added to A, and S
is updated.

```
MST-PRIM( G , w , r )
    for each u in G.V
        u.key = inf
        u.parent = NULL
    r.key = 0
    Q = COPY( G.V )
    While Q
        u = EXTRACT-MIN( Q )
        for each v in G.Adj[ u ]
            if ( v in Q ) and w( u , v ) < v.key
                v.key = w( u , v )
                v.parent = u
    A = Graph()
    for v in G.V
        A.V = A.V + { v }
        A.E = A.E + { ( v , v.parent ) }
    return A
```

```
explicacao aqui
```

```
gif aqui
```

## The Maze itself

So, how can a random maze be built from a MST?

Well, lets supose the maze can be drawn following a 2d grid with M vertical
lines and N horizontal ones. Each wall can be drawn by connecting one point of the grid
to the one above, bellow, to its left or right.

Thinking as Graph, the segment connecting two adjacent points of the grid is a edge, and 
each of those points is itself a node. So basically it is just needed to assign to each edge
a random value between 0 and 1 and find the MST of the Graph.

```
gif aqui ( kruskal )
```

```
gif aqui ( prim )
```

## How to use

The program must be launched from the command prompt. The command line is:
```
python.exe maze_make.py row col seed algo
```

*row* *col* *seed* and *algo* are four distinct integers, each one meaning:
* row -> number of horizontal lines. ( Between 2 and 80 )
* col -> number of vertical lines.   ( Between 2 and 80 )
* seed -> the seed for the rng       ( any value )
* algo -> the choosen algorithm, 1 for prim and 0 for kruskall

Also, it is possible to manipulate the speed of the animation using the left and right arrow
keys. The speed is a integer between 1 and 10 inclusive, with default value of 5, and that indicates
the number of new walls added per frame. 

## References

