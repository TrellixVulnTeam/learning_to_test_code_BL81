
def fizzBuzz(n: int):
    output = []
    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            #print("FizzBuzz")
            output.append("FizzBuzz")
        elif i % 3 == 0:
            #print("Fizz")
            output.append("Fizz")
        elif i % 5 == 0:
            #print("Buzz")
            output.append("Buzz")
        else:
            #print(i)
            output.append(i)
    return output

if __name__ == "__main__":
    fizzBuzz(15)