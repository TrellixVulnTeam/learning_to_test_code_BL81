"""
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".


make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
"""
word = "Yay"
out = "<<>>"
middle = len(out) // 2
outlist = list(out)

start, end = outlist[:middle], outlist[middle:]
print(start, end)

combined_as_list = start + list(word) + end
print(combined_as_list)

combined_as_string = "".join(i for i in combined_as_list)
print(combined_as_string)

def make_out_word(out, word):
    middle = len(out) // 2
    outlist = list(out)

    start, end = outlist[:middle], outlist[middle:]
    combined_as_list = start + list(word) + end
    return "".join(combined_as_list)

print(make_out_word(word, out))