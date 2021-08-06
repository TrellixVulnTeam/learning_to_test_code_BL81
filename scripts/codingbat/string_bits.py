def return_string(str):
    return str

def string_bits(str):
    output_string = ""
    for i in range(0, len(str), 2):
        output_string += str[i]
    return output_string

def string_bits_refactor1(str):
    return "".join(str[i] for i in range(0, len(str), 2))