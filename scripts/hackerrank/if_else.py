

def conditional(n: int) -> str:
    # odd
    if n % 2 != 0:
        return("Weird")
    # even if not odd
    else:
        if 2 <= n <= 5:
            return("Not Weird")
        elif 6 <= n <= 20:
            return("Weird")
        elif n > 20:
            return("Not Weird")

def conditional2(n: int) -> str:
    if n%2==0 and (n in range(2, 6) or n>20):
        return("Not Weird")
    else:
        return("Weird")

if __name__ == "__main__":
    print(conditional(1))
    print(conditional2(1))