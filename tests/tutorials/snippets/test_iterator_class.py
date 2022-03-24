from scripts.tutorials.snippets.iterator_class import ListIterator


class Test:

    def test_next(self):
        a_list = [1, 2, 3, 4]
        obj = ListIterator(a_list)
        for idx, _ in enumerate(a_list):
            assert a_list[idx] == obj.__next__()
    
    def test_raise_stop_iteration_exception(self):
        pass