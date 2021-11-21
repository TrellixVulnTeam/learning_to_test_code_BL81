import re

"""
address = "1.1.1.1"
substring = "."
matches = re.finditer(substring, address)
match_positions = [m.start() for m in matches]
print(match_positions)
"""

def find_index_all_occurances_string(input_list):
    return [x for x, v in enumerate(input_list) if v == "."]

def find_index_all_occurances_string2(input_list):
    index = 0
    found_at = []
    while index < len(input_list):
        index = input_list.find(".", index)
        if index == -1:
            break
        found_at.append(index)
        index += 1
    return found_at

# print(find_index_all_occurances_string("1.1.1.1"))
# print(find_index_all_occurances_string2("1.1.1.1"))

# input_list = "1.1.1.1"
# output = []
# period_indicies = find_index_all_occurances_string(input_list)
# for index, char in enumerate(input_list):
#     if index in period_indicies:
#         output.append("[.]")
#     else:
#         output.append(char)
# print("".join(output))    

input_string = "1.1.1.1"
input_list = list(input_string)
print(f"original: {input_list}")
for index, char in enumerate(input_list):
    if char == ".":
        input_list = input_list[:index] + ["[" + input_list[index] + "]"] + input_list[index+1:]
print("".join(input_list))