import pytest


@pytest.mark.run()
def test_MethodA():
    print("This is Method A")


@pytest.mark.run()
def test_MethodB():
    print("This is Method B")


@pytest.mark.run()
def test_MethodC():
    print("This is Method C")
    assert False
