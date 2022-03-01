from lists import szures

def test_normal():
    list = [1,-1,1,-2]
    assert szures(list) == [-1, -2]


def test_duplicate():
    list = [1, -1, 1, -2, -2]
    assert szures(list) == [-1, -2]