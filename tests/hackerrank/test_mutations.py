

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

def mutate_string2(string, position, character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    return string

def test_mutate_string():
    string = "abracadabra"
    assert len(string) == len(mutate_string(string, len(string)-1, "z"))

def test_mutate_string2():
    string = "abracadabra"
    assert len(string) == len(mutate_string2(string, len(string)-1, "z"))

string = "abracadabra"
print(mutate_string(string, 2, "z"))
print(mutate_string2(string, 2, "z"))
print(mutate_string(string, 2, "z") == mutate_string2(string, 2, "z"))
test_mutate_string()
