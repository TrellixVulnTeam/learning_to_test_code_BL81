


def dfs_graph(graph, start, path=[]):
    path += [start]
    
    for neighbor in graph[start]:
        if neighbor not in path:
            path = dfs_graph(graph, neighbor, path)
    
    return path

if __name__ == "__main__":
    # Using a Python dictionary to act as an adjacency list
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [5], 
        4: [6],
        5: [6],
        6: [7], 
        7: []
    }
    
    print(dfs_graph(graph, 1))