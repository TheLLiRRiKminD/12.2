from utils import arrs
import pytest


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, -1) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, 4) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], 10) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -10) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, 10) == [2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, -10) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 2, None) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], -10, -8) == [1, 2]
    assert arrs.my_slice("Hello, world!", 2, -2) == "llo, worl"
    assert arrs.my_slice((1, 2, 3, 4, 5), 1, 4) == (2, 3, 4)
    assert arrs.my_slice([1, 2, 3, 4, 5], 2, 5) == [3, 4, 5]
    assert arrs.my_slice({1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}, 2, 5) == [3, 4, 5]
    with pytest.raises(TypeError):
        arrs.my_slice(12345, 1, 4)