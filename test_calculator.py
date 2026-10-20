import calculator

def test_add():
    assert calculator.add(5, 3) == 8

def test_subtract():
    assert calculator.subtract(5, 3) == 2

def test_multiply():
    assert calculator.multiply(5, 3) == 15