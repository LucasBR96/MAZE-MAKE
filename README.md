# MAZE MAKER

The purpose of this project is the craetion of a simple animation that generates a random maze 
using a MST algorithm.

## What is MST?

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
pseudo codigo aqui
```

```
explicacao aqui
```

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
pseudo codigo aqui
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

