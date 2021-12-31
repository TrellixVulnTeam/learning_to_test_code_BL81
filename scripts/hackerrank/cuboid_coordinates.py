"""
In this hackerrank problem, we are given integers representing the dimensions of a cuboid and an integer. We need to pint a list of all of the possible coordinates where the sum of the coordinate points is not equal to n. This problem is supposed to be solved with list comprehension per the problem statement, but I have also included the for loop "brute force" solution also.
"""


def cuboid_coordinates(x, y, z, n):
    output = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                output.append([i, j, k])
    return [e for e in output if sum(e) != n]

def cuboid_coordinates_list_comp(x, y, z, n):
    return [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i, j, k]) != n]

    
if __name__ == "__main__":
    print(cuboid_coordinates(1, 1, 1, 2))
    assert cuboid_coordinates(1, 1, 1, 2) == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    assert cuboid_coordinates_list_comp(1, 1, 1, 2) == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]