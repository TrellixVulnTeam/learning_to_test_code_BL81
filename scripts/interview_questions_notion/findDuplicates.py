# find duplicates in an array
nums = [1, 2, 2, 3]
duplicates = []
seen = []


for i in range(len(nums)):
    if nums[i] in seen:
        duplicates.append(nums[i])
    seen.append(nums[i])
    
print(f"duplicates: {duplicates}")