

def pageCount(n: int, p: int) -> int:
    total_turns = n / 2
    from_start = p / 2
    from_end = total_turns - from_start
    return int(from_end if from_start > from_end else from_start)
    


if __name__ == "__main__":
    n = 5
    p = 3
    print(pageCount(n, p))