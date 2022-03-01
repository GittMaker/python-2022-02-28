from sum_negative_numbers import sum_negative_numbers

def test_with_4_negative_numbers():
    numbers = [1, 2, -1, -2, -3, 4, -6]
    assert sum_negative_numbers(numbers) == 4


def test_with_0_negative_numbers():
    numbers = [1, 2, 4, 6]
    assert sum_negative_numbers(numbers) == 0

def test_with_only_negative_numbers():
    numbers = [-1, -2, -3, -4, -6]
    assert sum_negative_numbers(numbers) == len(numbers)

def test_with_empty_list():
    numbers = []
    assert sum_negative_numbers(numbers) == 0

