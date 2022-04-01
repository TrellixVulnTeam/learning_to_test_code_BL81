# Making my own iterable
# KZ 3-23-22

class ListIterator:
    def __init__(self, array) -> None:
        self.array = array
        self.index = 0

    def __iter__(self):
        return self

    # def __next__(self):
    #     if self.array[self.index] == None:
    #         raise StopIteration
    #     else:
    #         item_required = self.array[self.index]
    #         self.index += 1
    #         return item_required
    """
    -Remove unnecessary else after guard condition (remove-unnecessary-else)
    -Use x is None rather than x == None (none-compare)
    """
    def __next__(self):
        if self.array[self.index] is None:
            raise StopIteration
        item_required = self.array[self.index]
        self.index += 1
        return item_required
        