from scripts.tutorials.snippets.iterator_class import ListIterator
import unittest
import pytest

class Test(unittest.TestCase):

    def test_next(self):
        a_list = [1, 2, 3, 4]
        obj = ListIterator(a_list)
        for idx, _ in enumerate(a_list):
            assert a_list[idx] == obj.__next__()
    
    def test_raise_stop_iteration_exception(self):
        a_list = [1, 2, 3, 4]
        obj = ListIterator(a_list)
        for idx, _ in enumerate(a_list):
            if idx != len(a_list):
                assert a_list[idx] == obj.__next__()
            else:
                self.assertRaises(StopIteration, obj.__next__(), a_list[idx])
