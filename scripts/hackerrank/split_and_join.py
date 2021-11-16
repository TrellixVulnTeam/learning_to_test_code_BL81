


def split_and_join(string):
    return string.replace(" ", "-")

def split_and_join_two(string):
    string_to_list = string.split(" ") # convert string to list
    return "-".join(string_to_list)

if __name__ == "__main__":
    string = "this is a string" # output: "this-is-a-string"
    print(split_and_join(string))
    print(split_and_join_two(string))