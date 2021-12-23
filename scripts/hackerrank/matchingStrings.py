


def matchingStrings(strings, queries):
    array = [0] * len(queries)
    for (idx, query) in enumerate(queries):
        for string in strings:
            if query == string:
                array[idx] += 1
    return array



if __name__ == "__main__":
    strings = ["ab", "ab", "abc"]
    queries = ["ab", "abc", "bc"]
    print(matchingStrings(strings, queries))