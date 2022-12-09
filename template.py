"""
member1: <Name Surname>
member2: <Name Surname>
"""
from typing import List, Dict
from collections import defaultdict


def read_csv(file_name: str) -> Dict[int, List[int]]:
    """
    read graph represented as matrix in .csv file and return it
    as dictionary where each key represents a vertex, while the value
    represent the list of matrices adjacent to the key
    :rtype: dict(key=int, value=list(int))
    :param file_name: string
    :return: graph
    """
    # Your code goes here(delete "pass" keyword)
    with open(file_name, 'r') as read_file:
        dct = {}
        readed = read_file.read()
        lst = readed.split('\n')
        for vertex in range(len(lst)):
            vertex_1 = lst[vertex].split(',')
            dct[(vertex)] = [i for i in range(len(vertex_1)) if vertex_1[i] == '1']
        return dct


def bfs(graph: Dict[int, List[int]]):
    """
    perform bfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph: dict(key=int, value=list(int))
    :return: bfs-result
    >>> bfs({1: [2, 4], 2: [3, 5], 3: [], 4: [], 5: []}
    [1, 2, 4, 3, 5]
    >>> bfs({1: [], 2: []})
    [1]
    """

    # additional function
    def adjacent_are_defined(graph: dict, j: int, vertices: dict):
        """
        Decides whether adjacent vertices to j are defined(given numbers)
        >>> adjacent_are_defined({1: [2, 3], 2: [1], 3:[1]}, 1, {'2': 3, '3': 2})
        True
        >>> adjacent_are_defined({1: [2, 3], 2: [1], 3:[1]}, 1, {'2': 3})
        False
        """
        for i in graph[j]:
            if vertices.get(str(i)) is None:
                return False
        return True
    # additional function
    def not_defined(j: int, graph: dict, vertices: dict):
        """
        Returns adjacent vertices to j that are not difided(given numbers)
        >>> not_defined(1, {1: [2, 3], 2: [1], 3:[1]}, {'2': 3})
        '3'
        >>> not_defined(1, {1: [2, 3], 2: [1], 3:[1]}, {'2': 3, '3': 2})
        ''
        """
        string = ''
        for i in graph[j]:
            if vertices.get(str(i)) is None:
                string += str(i)
        return string
    
    vertices = {}
    vertices[str(list(graph.keys())[0])] = 1
    queue = str(list(graph.keys())[0])
    count = 1
    edges = []
    while queue:
        j = queue[0]
        while not adjacent_are_defined(graph, int(j), vertices):

            not_defined_el = not_defined(int(j), graph, vertices)[0]
            edges.append([queue[0], not_defined_el])
            vertices[not_defined_el] = count + 1
            count += 1
            queue += not_defined_el

        queue = queue[1:]

    return [int(i) for i in vertices.keys()]


def dfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform dfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph:  dict(key=int, value=list(int))
    :return: dfs-result

    >>> dfs({1: [2, 4], 2: [3, 5], 3: [], 4: [], 5: []})
    [1, 2, 3, 5, 4]
    >>> dfs({1: [], 2: []})
    [1]
    """
    result = []
    visited_points = []
    stack = []

    visited_points.append(list(graph.keys())[0]) # start with first point
    stack.append(list(graph.keys())[0])

    while stack:
        s = stack.pop()
        result.append(s)

        for point in reversed(graph[s]): # reversed to not mix points in stack
            if point not in visited_points:
                visited_points.append(point)
                stack.append(point)

    return result


def calc_pow(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """
    calculate power of every vertex of your graph(i.e. number adjacent edges)
    :rtype: dict(key=int, value=int)
    :param graph: dict(key=int, value=list(int))
    :return: vertices and their powers
    >>> calc_pow({1: [2, 3], 2: [1, 4], 3: [1, 4], 4:[3, 2]})
    {1: 2, 2: 2, 3: 2, 4: 2}
    >>> calc_pow({1: [2], 2: [1, 3], 3: [2]})
    {1: 1, 2: 2, 3: 1}
    """
    result = {}
    for vertex in graph:
        result[vertex] = len(graph[vertex])
    return result


def find_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    here is another way of representing a graph:
    edges - is a list of edges of a graph,
    where each edge is also a list of two integers,
    which represent 2 adjacent vertices
    find if there is a way from the source vertex to the destination one
    :rtype: bool
    :param n: int
    :param edges: list(list(int))
    :param source: int
    :param destination: int
    :return:
    >>> find_path(4, [[0, 1], [0, 2]], 3, 0)
    False
    >>> find_path(4, [[0, 1], [0, 2]], 3, 3)
    True
    >>> find_path(4, [[0, 1], [0, 2]], 1, 2)
    True
    """
    visited_points = []
    stack = []
    graph = defaultdict(list)
    for pair in edges:
        if not graph[pair[0]]:
            graph[pair[0]] = [pair[1]]
        else:
            graph[pair[0]] = graph[pair[0]] + [pair[1]]
        if not graph[pair[1]]:
            graph[pair[1]] = [pair[0]]
        else:
            graph[pair[1]] = graph[pair[1]] + [pair[0]]

    visited_points.append(source) # start with first point
    stack.append(source)

    while stack:
        s = stack.pop()
        if s == destination:
            return True

        for point in reversed(graph[s]): # reversed to not mix points in stack
            if point not in visited_points:
                stack.append(point)
                if point == destination:
                    return True

    return False

import doctest
print(doctest.testmod())
