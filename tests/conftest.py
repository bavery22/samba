import pytest

def pytest_addoption(parser):
    parser.addoption("--testimage", action="store", default="crops/samba",
                     help="image to test")

@pytest.fixture
def testimage(request):
    return request.config.getoption("--testimage")
