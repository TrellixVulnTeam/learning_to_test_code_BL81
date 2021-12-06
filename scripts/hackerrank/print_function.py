

# NOTE: NO STRING METHODS
# input: 5
# output: 12345

def print_function_with_string_methods(n):
    output = ""
    for i in range(1, n+1):
        output += str(i)
    return(output)    
    
def print_function(n):
    output = [str(i) for i in range(1, n+1)]
    return("".join(output))
    
if __name__ == "__main__":
    print(print_function_with_string_methods(5))
    print(print_function(5))