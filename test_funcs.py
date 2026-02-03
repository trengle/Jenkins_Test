import funcs

def test_add():
    assert funcs.add(2, 3) == 5

def test_subtract():
    assert funcs.subtract(2, 3) == -1

def test_multiply():
    assert funcs.multiply(2, 3) == 6

def test_divide():
    assert funcs.divide(10, 5) == 2