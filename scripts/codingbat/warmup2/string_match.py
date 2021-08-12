"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""

str1 = 'xxcaazz'
str2 = 'xxbaaz'

count = 0
for i in range(0, len(str1) - 1):
    print(str1[i:i+2])
    sub1 = str1[i:i+2]
    
    for j in range(0, len(str2) - 1):
        print(str2[j:j+2])
        sub2 = str2[j:j+2]
        if sub1 == sub2:
            count += 1
        print(f"comparing: {sub1, sub2}")
print(count)

def string_match(a, b):
    count = 0

    for i in range(0, len(a) - 1):
        sub1 = a[i:i+2]
        for j in range(0, len(b) - 1):
            sub2 = b[i:i+2]
        if sub1 == sub2:
            count += 1
    return count

print(string_match(str1, str2))