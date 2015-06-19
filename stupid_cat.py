
from hypothesis import given, assume, Settings
from hypothesis.strategies import integers

@given(integers(), integers(), settings=Settings(max_examples=5000))
def test_stupid_cat(cat=3, dog=4):
    assert cat * dog == 12


