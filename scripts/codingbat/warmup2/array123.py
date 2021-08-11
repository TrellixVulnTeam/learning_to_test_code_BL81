
def array123(nums):
  sequence = [1, 2, 3]
  seqIdx = 0

  for i in range(len(nums)):
    if seqIdx < len(sequence) and nums[i] == sequence[seqIdx]:
      seqIdx += 1
  
  if seqIdx == len(sequence):
    return True
  else:
    return False

print(array123([1, 1, 2, 3, 1]))

"""def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10] 
sequence =  [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))"""