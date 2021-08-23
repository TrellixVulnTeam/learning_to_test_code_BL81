"""

The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.


squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True
"""


# is_summer = True
# temp = 70
# # cond1 = (60 <= temp <= 90) if not is_summer else (60 <= temp <= 100)
# # print(cond1)

# if is_summer:
#     print(f"Its summer and can play: {60 <= temp <= 100}")
# else:
#     print(f"its not summer but can play: {60 <= temp <= 90}")


temp = 70
is_summer = False

def squirrel_play(temp, is_summer):
    if is_summer:
        return (60 <= temp <= 100)
    else:
        return (60 <= temp <= 90)
    

print(squirrel_play(temp, is_summer))

