"""Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.


non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
"""

str1 = "Hello"
str2 = "There"

combined = str1[1:] + str2[1:]
print(combined)

def non_start(a, b):
  return a[1:] + b[1:]