"""
member1: <Name Surname>
member2: <Name Surname>
"""
from typing import List, Dict


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
    pass


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

    >>> dfs({1: [2, 4], 2: [3, 5], 3: [], 4: [], 5: []}, 1)
    [1, 2, 3, 5, 4]
    >>> dfs({1: [], 2: []}, 1)
    [1]
    """
    result = []
    visited_points = []
    stack = []

    visited_points.append(graph.keys()[0]) # start with first point
    stack.append(graph.keys()[0])

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
    """
    # Your code goes here(delete "pass" keyword)
    pass
