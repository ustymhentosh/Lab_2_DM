# Lab_2_DM

## bfs()

> perform breadth-first search on the graph and store its result in the list of vertices(integers that represent vertices)
> 

> return type: list(int)
param graph: dict(key=int, value=list(int))
return: bfs-result
> 

```python
>>> bfs({1: [2, 4], 2: [3, 5], 3: [], 4: [], 5: []})
    [1, 2, 4, 3, 5]
>>> bfs({1: [], 2: []})
    [1]
```

> Has two additional functions.
> 

**adjacent_are_defined()** - Decides whether adjacent vertices to j are defined(given numbers)

Takes three arguments     →          graph: dict, j: int, vertices: dict

```python
>>> adjacent_are_defined({1: [2, 3], 2: [1], 3:[1]}, 1, {'2': 3, '3': 2})
        True
>>> adjacent_are_defined({1: [2, 3], 2: [1], 3:[1]}, 1, {'2': 3})
        False
```

**not_defined()** - Returns adjacent vertices to j that are not defined(given numbers)

Takes three arguments      →         j: int, graph: dict, vertices: dict

```python
>>> not_defined(1, {1: [2, 3], 2: [1], 3:[1]}, {'2': 3})
        '3'
>>> not_defined(1, {1: [2, 3], 2: [1], 3:[1]}, {'2': 3, '3': 2})
        ''
```

> Main function also has possibility to return edges through which the search was made. Just type edges as second thing to return and bob's your uncle(and there it is)
>