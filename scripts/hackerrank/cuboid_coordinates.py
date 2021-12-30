


def cuboid_coordinates(x, y, z, n):
    output = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                output.append([i, j, k])
    return [e for e in output if sum(e) != n]

    
if __name__ == "__main__":
    print(cuboid_coordinates(1, 1, 1, 2))
    assert cuboid_coordinates(1, 1, 1, 2) == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]