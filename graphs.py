from typing import List
from typing import Union

#! Supports O(1) addition and removal of elements from left and right, like a doubly linked list, whereas normal queue,basically a list, an array is O(n) from shifting
from collections import deque

def main():
    dirEdges = [[6,5],[0,1],[0,2],[1,0],[1,2],[1,3],[2,0],
                [2,1],[2,4],[3,1],[3,4],[4,2],[4,3],
                [4,5],[5,4],[5,6],[5,6]]
    udirEdges = [[6,5],[1,0],[1,2],[1,3],[2,0],
                [3,4],[4,2],[4,5]]

    adjListDirected = makeAdjList(True, dirEdges)
    adjListUndirected = makeAdjList(False, udirEdges)

    print(adjListDirected)
    print(adjListUndirected)

    print(bfsList(adjListUndirected, 5))


def bfsList(graph: dict, start: int) -> dict:
    if graph is None: return None
    if start not in graph: raise Exception("Starting Vertex not in Graph")

    result = {key: -1 for key in graph}
    queue = deque()
    dist = 0
    result[start] = dist

    queue.append(start)
    while queue:
        key = queue.popleft() # O(1)
        values = graph[key]
        for value in values:
            if result[value] == -1:
                result[value] = result[key] + 1
                queue.append(value)

    return result


def makeAdjList(directed: bool, edges: List[List[int]]) -> Union[None, dict]:
    if edges is None: return None

    dupes = list()
    result = dict()

    for key, value in edges:
        if [key, value] not in dupes:
            if key not in result: result[key] = [value]
            else: result[key].append(value)
            dupes.append([key, value])
        if not directed:
            if [value, key] not in dupes:
                if value not in result:result[value] = [key]
                else: result[value].append(key)
            dupes.append([value, key])

    return result

def makeAdjMatrix(n: int, edges: List[List[int]]) -> Union[None, List[List[int]]]:
    if n < 0:
        raise Exception("Range must be larger than 0")
    if edges == None:
        return None
    
    matrix = []
    for i in range(n + 1):
        row = []
        for j in range(n + 1):
            row.append(0)
        matrix.append(row)
    
    for key, value in edges:
        matrix[key][value] = 1

    return matrix

main()