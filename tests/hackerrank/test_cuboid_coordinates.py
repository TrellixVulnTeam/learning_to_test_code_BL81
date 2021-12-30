from scripts.hackerrank.cuboid_coordinates import cuboid_coordinates


class Test:
    test_cases = [
        # x, y, z, n
        [[1, 1, 1, 2], [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]]
    ]
    testable_functions = [cuboid_coordinates]
    
    
    def test_cuboid_coordinates(self):
        for f in self.testable_functions:
            for case, expected in self.test_cases:
                assert f(*case) == expected