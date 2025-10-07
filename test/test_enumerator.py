from src.enumerator import NCEnumerate


def test_iter_returns_reference_to_enumerate_instance():
    e = NCEnumerate(['a', 'b', 'c', 'd'])

    assert e is iter(e)
