arr = [1, 2, 2, 3, 4]

seen = []
duplicates = []

for element in arr:
    if element in seen:
        duplicates.append(element)
    seen.append(element)

print(f"seen: {seen}")
print(f"duplicates: {duplicates}")

print(5/2)
print(5//2)