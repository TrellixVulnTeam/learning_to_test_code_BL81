# https://www.programiz.com/python-programming/iterator
# Notes on Iterators from Programiz
# Iterator is ....
#  1. object that can be iterated upon
#  2. implements __iter__() and __next__() special methods (collectively called the "iterator protocol")

from typing import List

# define list (my_list is an iterable..remember: iterable is object that can return iterator)
my_list = [4, 7, 0, 3]

# create an iterator object from that iterable
my_iter = iter(my_list)

# iterate through it using next()
print(next(my_iter))
print(next(my_iter))

# next(obj) is the same as obj.__next__()
print(my_iter.__next__())
print(my_iter.__next__())

# This will raise error, no items left
# print(next(my_iter))

# for loop can iterate over any iterable
for m in my_iter:
    print(m)

# ^^ that is actually...
iterable = "hello"
# print("__iter__" in dir(iterable)) # True

# create an iterator object from an iterable
iter_obj = iter(iterable)
# print(iterable.__next__()) # h

# infinite loop
while True:
    try:
        # get the next item
        element = iter_obj.__next__()
        
        # do something with element
        print(f'element: {element}')

    except StopIteration:
        # if StopIteration is raised, break from loop
        break

# Summary: So bascially under the hood..a for loop creates an iterator object from an iterable by doing a iter_obj = iter(iterable)...and then an infinite while loop just gets the next value in iter_obj using the next() function until the StopIteration exception is raised...where we break and the program ends to "gracefully exit" when the program runs out of values

class SimpleIterator:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.iterable = iter(self.nums)

    def get_next(self):
        return self.iterable.__next__()

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    si = SimpleIterator(nums)
    print(si.iterable)
    print(si.get_next())

