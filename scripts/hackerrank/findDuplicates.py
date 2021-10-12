arr = [1, 2, 2, 3, 4]

seen = []
duplicates = []

for element in arr:
    if element in seen:
        duplicates.append(element)
    seen.append(element)

print(f"seen: {seen}")
print(f"duplicates: {duplicates}")

def findDuplicates(arr: list) -> int:
    seen = []
    duplicates = []
    for element in arr:
        if element in seen:
            duplicates.append(element)
        seen.append(element)
    return int(duplicates[0])




# print(5/2)
# print(5//2)