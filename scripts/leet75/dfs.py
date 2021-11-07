from typing import Dict, List


def create_graph():
    return {
        "A" : ["B", "C"],
        "B" : ["D", "E"],
        "C" : ["F"],
        "D" : [],
        "E" : ["F"],
        "F" : []
    }

def dfs(graph, vertex, path=[]):
    path += [vertex]
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs(graph, neighbor, path)
    return path

def bfs(graph, vertex, path=[]):
    path += [vertex]
    queue = [vertex]
    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in path:
                queue.append(neighbor)
                path.append(neighbor)
    return path