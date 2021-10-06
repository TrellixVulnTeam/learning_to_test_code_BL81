"""Given an array of strings, return another array containing all of its longest strings.
Example:
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be allLongestStrings(inputArray) = ["aba", "vcd", "aba"]."""

# my answer
strings_list = ["aba", "aa", "ad", "vcd", "aba"]

# find the length of the longest string by looping through all the possibilities
max_len = 0
result = []
for e in strings_list:
    if len(e) > max_len:
        max_len = len(e)
print(max_len)

# use list comp to get the elements whose length is longest (in this case want all strings with len = 3)
longest_strings = [i for i in strings_list if len(i) == max_len]
print(longest_strings)


# github answer
def allLongestStrings(inputArray):
    length = max([len(word) for word in inputArray])
    result = [word for word in inputArray if len(word) == length]
    return result


# below is my first try and keeping this to show one type of problem dictionary doesnt work well for because there are duplicates that need to be preserved in the input array that have the same length (see "aba" and "aba" below are both length of 3 but if use dict only one is kept because keys are unique in a dict)
"""
#strings_list = ["aba", "aa", "ad", "vcd", "aba"]
# counts = {}
# for element in strings_list:
#     counts[element] = len(element)
# print(counts)

# output = {k for k, v in counts.items() if v == max(counts.values())}
# print(output)
# ^^ problem with using dict is that each key in the dict is unique so duplicate values are only shown once, which is why below I used a list instead so that the duplicate entries are preserved
# if you use a dict, "aba" above only shows up once when it should be in there twice because its a string of the max length
# """