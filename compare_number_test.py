from compare_number import is_larger_than_15

def test_larger_with_big_number():
    # Given
    # When
    result = is_larger_than_15(100)
    # Then
    assert result == True


def test_larger_with_big_number_short():
    assert is_larger_than_15(100)

def test_larger_with_small_number():
    assert not is_larger_than_15(7)

def test_larger_with_negative_number():
    assert not is_larger_than_15(-999999)
