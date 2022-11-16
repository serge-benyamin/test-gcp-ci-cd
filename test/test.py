import sys
sys.path.append('..')
from src.dummy_app import square

def test_square():
    assert square(2)==4
