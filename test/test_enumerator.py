from src.enumerator import NCEnumerate
import pytest

def test_iter_returns_reference_to_enumerate_instance():
    e = NCEnumerate(['a', 'b', 'c', 'd'])

    assert e is iter(e)

def test_next_returns_item_with_enumerate():
    e = NCEnumerate(['a', 'b', 'c'])
    assert next(e) == (0,'a')
    assert next(e) == (1, 'b')
    assert next(e) == (2, 'c')
    
def test_next_raises_error():
    e = NCEnumerate(['a'])

    assert next(e) == (0,'a')

    with pytest.raises(StopIteration):
        next(e)

def test_next_iterates_single_time():
    e = NCEnumerate(['a', 'b', 'c'])

    enumerated_list = []

    for i in e:
        enumerated_list.append(i)

    assert enumerated_list == [(0,'a'), (1, 'b'), (2, 'c')]

    for i in e:
        enumerated_list.append(i)

    assert enumerated_list == [(0,'a'), (1, 'b'), (2, 'c')]