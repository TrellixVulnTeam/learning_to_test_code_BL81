

def dynamicArray(n, queries):
    # Write your code here
    answers = []
    lastAnswer = 0
    arrays = [[] for j in range(n)]
    for query in queries:
        query_type, x, y = query[0], query[1], query[2]
        if query_type == 1:
            idx = (x ^ lastAnswer) % n
            arrays[idx].append(y)
            
        elif query_type == 2:
            idx = ((x ^ lastAnswer) % n)
            lastAnswer = arrays[idx][y % len(arrays[idx])]
            answers.append(lastAnswer)
            
    return answers
            
if __name__ == "__main__":
    queries = [
        [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1]
    ]
    n = 2
    
    arrays = (dynamicArray(2, queries))
    print(arrays)