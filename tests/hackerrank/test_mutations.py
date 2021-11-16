from scripts.hackerrank.mutations import mutate_string, mutate_string2


class Test:

    def test_mutate_string(self):
        string = "abracadabra"
        assert len(string) == len(mutate_string(string, len(string)-1, "z"))

    def test_mutate_string2(self):
        string = "abracadabra"
        assert len(string) == len(mutate_string2(string, len(string)-1, "z"))