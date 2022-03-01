from lists import transform

def test_normal():
    list = [1,2,3]
    assert transform(list) == [2,4,6]
