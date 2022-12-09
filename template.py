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


def bfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform bfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph: dict(key=int, value=list(int))
    :return: bfs-result
    """
    # Your code goes here(delete "pass" keyword)
    pass


def dfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform dfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph:  dict(key=int, value=list(int))
    :return: dfs-result
    """
    # Your code goes here(delete "pass" keyword)
    pass


def calc_pow(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """
    calculate power of every vertex of your graph(i.e. number adjacent edges)
    :rtype: dict(key=int, value=int)
    :param graph: dict(key=int, value=list(int))
    :return: vertices and their powers
    """
    # Your code goes here(delete "pass" keyword)
    pass


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

    # graph = dict(graph)

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
