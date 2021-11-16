

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

def mutate_string2(string, position, character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    return string

if __name__ == "__main__":
    string = "abracadabra"
    print(mutate_string(string, 2, "z"))
    print(mutate_string2(string, 2, "z"))
    print(mutate_string(string, 2, "z") == mutate_string2(string, 2, "z"))

