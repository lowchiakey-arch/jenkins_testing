from calculator import add

def test_add_positive_numbers():
    result = add(5, 7)
    assert result == 12

def test_add_negative_numbers():
    result = add(-1, -3)
    assert result == -4

def test_add_zero():
    result = add(10, 0)
    assert result == 10

def test_minus_zero():
    result = minus(10, 0)
    assert result == 10
