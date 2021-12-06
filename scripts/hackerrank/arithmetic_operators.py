import numpy as np


def operators(a, b) -> None:
    # sum of two integers line 1
    line1 = sum([a, b])
    print(line1)
    
    # differnence of two integers line 2 
    # first - second
    line2 = (a - b)
    print(line2)
    
    # product of two integers line 3
    line3 = np.prod([a, b])
    print(line3)
    
def operators2(a: int, b: int) -> None:
    print(f"{a+b}\n{a-b}\n{a*b}")
    
    
if __name__ == "__main__":
    operators(3, 2)
    print("--")
    operators2(3, 2)
    print(operators(3, 2) == operators2(3, 2))