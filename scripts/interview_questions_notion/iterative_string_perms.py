


def iterative_string_perms(word: str) -> list:
    stack = list(word)
    results = [stack.pop()] # c
    while stack:
        c = stack.pop() # b
        new_results = []
        for w in results:
            for i in range(len(w) + 1):
                print(w[:i], c, w[i:])
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results

if __name__ == "__main__":
    print(iterative_string_perms("abc"))

    #abc
    # a
    # abc, bac, bca
    # b
    # acb
    # c
    # cab, cba
    # forward, back, inbetween

    # cat
    # c
    # cat, atc, act
    # a
    # cta
    # t
    # tac, tca 