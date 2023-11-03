from ..modules.codeoutput import sorting

def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5

def test_result():
    assert sorting() == [1, 2, 4, 5, 6, 9, 10]