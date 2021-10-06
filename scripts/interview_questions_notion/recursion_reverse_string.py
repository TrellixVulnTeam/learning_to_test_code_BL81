# reverse a string recursively: notion

def recursive_reverse(s):
    if len(s) == 0:
        return s
    
    else:
        result = recursive_reverse(s[1:]) + s[0]
        return result

s = "kevin"
print(recursive_reverse(s))