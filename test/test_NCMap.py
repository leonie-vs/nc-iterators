from src.NCMap import NCMap
import pytest

def test_iter_returns_reference_to_enumerate_instance():

    def demo_mul_5(item):
        return item * 5
    
    list = [3]
    
    nm = NCMap(demo_mul_5, list)

    assert nm is iter(nm)


def test_next_should_call_funct_with_single_item():

    def demo_mul_5(item):
        return item * 5
    
    list = [3]
    
    nm = NCMap(demo_mul_5, list)

    assert next(nm) == 15


def test_next_should_call_funct_with_multiple_item():

    def demo_mul_5(item):
        return item * 5
    
    list = [3,4]
    
    nm = NCMap(demo_mul_5, list)

    assert next(nm) == 15
    assert next(nm) == 20

def test_next_should_raise_stop_iteration():
    def demo_mul_5(item):
        return item * 5
    
    list = [3,4]
    
    nm = NCMap(demo_mul_5, list)

    assert next(nm) == 15
    assert next(nm) == 20

    with pytest.raises(StopIteration):
        next(nm)


