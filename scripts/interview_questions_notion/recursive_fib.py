
def fib_recur(n):  # sourcery skip: inline-immediately-returned-variable
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib_recur(n-1) + fib_recur(n-2)
        return result

print(fib_recur(5))


# 1, 1, 2, 3, 5, 8, 13

# Fn = Fn - 1 + Fn - 2
# Where F0 = 0 and F1 = 1

# print(fib(3))

# 1st : result = fib_recur(n-1) + fib_recur(n-2)