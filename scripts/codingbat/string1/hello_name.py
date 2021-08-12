"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'"""

# read instructions carefuly even on the easy ones! Like exclaimation point!
def hello_name(name):
    return "Hello {}!".format(name)

print(hello_name("Bob"))