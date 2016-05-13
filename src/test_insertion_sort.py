"""Test insertion sort."""
import pytest


def test_insertion_sort():
    """Assert that it works for tox."""
    from insertion_sort import insertion_sort
    insertion_return_val = [56, 93, 7, 11]
    insertion_sort(insertion_return_val)
    assert insertion_return_val == [7, 11, 56, 93]


def test_string_in_list():
    """Assert error is raised with string input."""
    from insertion_sort import insertion_sort
    with pytest.raises(TypeError):
        insertion_sort([1, 45, 'a', 5])


def test_empty_list():
    """Assert empty list is None."""
    from insertion_sort import insertion_sort
    alist = []
    insertion_sort(alist)
    assert alist == []


def test_same_items_in_list():
    """Assert list remins the same."""
    from insertion_sort import insertion_sort
    alist = [1, 1, 1, 1]
    insertion_sort(alist)
    assert alist == [1, 1, 1, 1]


def test_revers_order_list():
    """Assert reversed list is sorted."""
    from insertion_sort import insertion_sort
    alist = [5, 4, 3, 2, 1]
    insertion_sort(alist)
    assert alist == [1, 2, 3, 4, 5]

def test_stability():
    """Testing stablility."""
    from insertion_sort import insertion_sort_stability_proof
    list_of_tuples = [('a', 1), ('b', 50), ('c', 10), ('d', 10)]
    assert insertion_sort_stability_proof(list_of_tuples) == [('a', 1), ('c', 10), ('d', 10), ('b', 50)]
