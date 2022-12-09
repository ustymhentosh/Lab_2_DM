# Lab_2_DM

### read_csv()

> reads graph represented as matrix in .csv file and return it as dictionary where each key represents a vertex, while the value represent the list of matrices adjacent to the key.
> 

> return type: dict(key=int, value=list(int))
param file_name: string
return: graph
> 

```python
>>> read_csv('graph.csv')
	{0: [2, 5, 7], 1: [2, 6, 7], 2: [0, 1, 4, 5, 6, 7], 3: [6, 7], 4: [2, 5, 7], 5: [0, 2, 4, 7], 6: [1, 2, 3, 7], 7: [0, 1, 2, 3, 4, 5, 6]}
```