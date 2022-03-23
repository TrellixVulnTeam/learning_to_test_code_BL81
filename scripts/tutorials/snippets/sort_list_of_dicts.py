# 3-20-22
# Cool snippet that does the following:
# Takes a list of dictionaries and then uses the sort() built in python function and lambda expressions to sort the list of dictionaries by a certain key in the dictionary. 

country = [
    {"country" : "USA", "population" : 200000},
    {"country" : "Canada", "population" : 10000},
    {"country" : "Switzerland", "population" : 3000}
]

# reminder: list sorts in place and doesnt return anything
country.sort(reverse=True, key=lambda e: len(e['country']))

for c in country:
    print(c)