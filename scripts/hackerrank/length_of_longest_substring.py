

s = "abcabcbb"
s = "pwwkew"
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
    print(temp, j)
    print("--")
print(max_substring)
print(indicies)
