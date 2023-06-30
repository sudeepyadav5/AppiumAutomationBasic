import pytest

def test_methodA():
    print("This is Method A")

def test_methodB():
    print("This is Method B")

@pytest.mark.skip
def test_methodC():
    print("This is Method C")

def test_methodD():
    print("This is Method D")
    assert False