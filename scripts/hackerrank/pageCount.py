
"""
I had similar logic in my code. I'll do my best to explain.

It is checking if p is even using the modulus opperator. n % 2 == 0, or n divided by 2 has a remainer of zero.

The reason this is necessary is because if counting from the end of the book and dividing by 2 an even number will give the wrong page count, since the even number will be on the left page.

For instance, if you turn to page 5 in a 6 page book (n-p) will return 1/2, or 0 pages, but it actually requires 1 page, so we increment even numbers [of pages]up 1
"""

# n == pages
# p == page wanted
def pageCount(n, p):
    # if p == 1 or p == n:
    #     return 0
    if p in [1, n]:
        return 0
    mid = n//2
    if p <= mid:
        return (p)//2
    if n % 2 == 0:
        return (n-p+1)//2
    return (n - p)//2

def pageCount2(n, p):
    mid = n//2
    # if p == 1 or p == n:
    #     return 0
    if p in [1, n]:
        return 0
    elif p <= mid:
        return (p)//2
    # if page # is even
    elif n % 2 == 0:
        return (n-p+1)//2
    else:
        return (n - p)//2
    
def pageCount_fails_one_test(n: int, p: int) -> int:
    """
    This function fails just one of the 27 "hidden" test cases on LeetCode. Must be a premium member to get hidden test cases and can't figure out what potential input and expected output this wont pass for.
    """
    total_turns = n / 2
    from_start = p / 2
    from_end = total_turns - from_start
    return int(from_end if from_start > from_end else from_start)


if __name__ == "__main__":
    n = 5
    p = 3
    print(pageCount(n, p))