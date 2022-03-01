from lists import sum

def test_with_positives():
    numbers = [1,2,3,4,5,6,7,8,9]
    assert sum(numbers) == 45


def test_with_negatives():
    numbers = [-1,-2,-3,-4,-5,-6,-7,-8,-9]
    assert sum(numbers) == -45


def test_with_empty_list():
    numbers = []
    assert sum(numbers) == 0

