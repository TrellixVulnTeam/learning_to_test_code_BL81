"""
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.


left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
"""

str1 = "Hello"

def left2(str, rotate_num):
  return str[rotate_num:] + str[:rotate_num]

def left2_refactor(str1: str, rotate_num: int, *args) -> str:
  left_chunk_before = str1[:rotate_num]
  right_chunk_before = str1[rotate_num:]
  return right_chunk_before + left_chunk_before

