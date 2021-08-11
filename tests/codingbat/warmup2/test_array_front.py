from scripts.codingbat.warmup2 import array_front

def test_array_front():
    assert array_front.array_front([1, 2, 9, 3, 4]) == True
    assert array_front.array_front([1, 2, 3, 4, 9]) == False
    assert array_front.array_front([1, 2, 3, 4, 5]) == False
