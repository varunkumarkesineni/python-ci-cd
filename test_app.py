
from app import add

def test_add():
    assert add(10, 20) == 30

def test_add_zero():
    assert add(5, 0) == 5
