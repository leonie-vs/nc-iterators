from src.enumerator import NCEnumerate
import pytest

def test_iter_returns_reference_to_enumerate_instance():
    e = NCEnumerate(['a', 'b', 'c', 'd'])

    assert e is iter(e)

def test_next_return_item_with_enumerate():
    e = NCEnumerate(['a', 'b', 'c'])
    # try:
    assert next(e) == (0,'a')
    assert next(e) == (1, 'b')
    assert next(e) == (2, 'c')
    #     # assert next(e)
    # except IndexError:
    #      print('Item out of index')
    
def test_next_should_through_error():
    e = NCEnumerate(['a'])

    assert next(e) == (0,'a')

    with pytest.raises(StopIteration):
        next(e)

def test_next_iterate_single_time():
    e = NCEnumerate(['a', 'b', 'c'])

    enumerated_list = []

    for i in e:
        enumerated_list.append(i)

    assert enumerated_list == [(0,'a'), (1, 'b'), (2, 'c')]

    for i in e:
        enumerated_list.append(i)

    assert enumerated_list == [(0,'a'), (1, 'b'), (2, 'c')]