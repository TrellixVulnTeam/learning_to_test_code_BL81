


def is_leap(year):
    leap = False
    # leap year if divisible by 4 evenly
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        elif year % 100 != 0:
            leap = True
    return leap
    
def is_leap2(year):  
    leap = False  
    if year % 4 == 0 and year % 100 == 0:
        leap = year % 400 == 0
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    return leap

def is_leap3(year):
    """Like this answer the best"""
    leap = False
    if year % 4 == 0:
        leap = year % 400 == 0 if year % 100 == 0 else True
    return leap

def is_leap4(year):
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)
    

if __name__ == "__main__":
    print(is_leap(1940))
    print(is_leap2(1940))
    print(is_leap3(1940))
    print(is_leap4(1940))