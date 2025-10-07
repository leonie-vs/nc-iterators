from src.enumerator import NCEnumerate

def test_iter_returns_reference_to_enumerate_instance():
    e = NCEnumerate(['a', 'b', 'c', 'd'])

    assert e is iter(e)

def test_next_return_item_with_enumerate():
    e = NCEnumerate(['a', 'b', 'c'])
    try:
        assert next(e) == (0,'a')
        assert next(e) == (1, 'b')
        assert next(e) == (2, 'c')
        assert next(e)
    except IndexError:
         print('Item out of index')
    
