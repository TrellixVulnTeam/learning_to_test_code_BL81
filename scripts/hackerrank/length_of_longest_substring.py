
def is_unique(s):
    counts = {}
    for item in s:
        counts[item] = counts.get(item, 0) + 1
    return not any([v for k, v in counts.items() if v > 1])


s = "abcabcbb"
s = "pwwkew"
# s = "bbbbb"
# s = "aab"
max_substring = 0
indicies = []
for i in range(len(s)):
    for j in range(i, len(s)):
        temp = []
        for k in range(i, j):
            if s[k] not in temp:
                temp.append(s[k])
                if len(temp) > max_substring:
                    max_substring = len(temp)
                    indicies = s[i:j]
            else:
                break
print(max_substring)
print(indicies)
