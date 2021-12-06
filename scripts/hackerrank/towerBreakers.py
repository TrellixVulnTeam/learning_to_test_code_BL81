from itertools import permutations

def isOkay(n):
    l = []
    for i in range(1, n+1):
        if n % i == 0:
            print(i,n)
            l.append(i)
    # print([i for i in permutations(l)]

    print(l)
    for i in range(len(l)):
        for j in range(0, len(l)+1):
            tmp = []
            for k in range(i, j):
                tmp.append(l[k])
            print(tmp)
            

            
if __name__ == "__main__":
    isOkay(6)