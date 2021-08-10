"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

def string_bits(str):
    output_string = ""
    for i in range(0, len(str), 2):
        output_string += str[i]
    return output_string


def string_bits_refactor1(str):
    return "".join(str[i] for i in range(0, len(str), 2))

# test = "Hello"
# for i in range(0, len(test), 2):
#     print(test[i])

print(string_bits("Hello"))
print(string_bits_refactor1("Hello"))

"""
Coding Bat Solution:
def string_bits(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
"""