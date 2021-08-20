
"""
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
"""
# Success --> is_weekend = True and greater than 40 cigars
# Success --> is_weekend = False and between 40 and 60 cigars (inclusive)


is_weekend = True
cigars = 30

# if not is_weekend and (40 <= cigars <= 60):
#     print("True")
# elif is_weekend and (cigars >= 40):
#     print("True")
# else:
#     print("False")



def cigar_party(cigars, is_weekend):
    if not is_weekend and (40 <= cigars <= 60):
        return True
    elif is_weekend and (cigars >= 40):
        return True
    else:
        return False

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))

"""
Coding Bat Solution:
def cigar_party(cigars, is_wekeend):
    if is_weekend:
        return (cigars >= 40)
    else:
        return (40 <= cigars <= 60)

print(cigar_party(30, False))
print(cigar_party(50, False))
print(cigar_party(70, True))
"""