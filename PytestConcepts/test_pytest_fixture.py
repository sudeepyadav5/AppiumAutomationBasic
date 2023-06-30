import pytest


@pytest.fixture()
def setup():
    print("Print Once Before every Method")
    yield
    print("Print Once After every Method")


def testMethodDemo(setup):
    print("Print Demo Method")
