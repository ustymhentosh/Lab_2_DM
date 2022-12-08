# Lab_2_DM

### calc_pow()

> calculate power of every vertex of your graph(i.e. number adjacent edges)
> 

> return type: dict(key=int, value=int)
param graph: dict(key=int, value=list(int))
return: vertices and their powers
> 

```python
>>> calc_pow({1: [2, 3], 2: [1, 4], 3: [1, 4], 4:[3, 2]})
    {1: 2, 2: 2, 3: 2, 4: 2}
>>> calc_pow({1: [2], 2: [1, 3], 3: [2]})
    {1: 1, 2: 2, 3: 1}
```
