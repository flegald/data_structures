"""Test quick sort."""
import pytest


def test_quick_sort():
    """Assert that it works for tox."""
    from quick_sort import quick_sort
    quick_return_val = [56, 93, 7, 11]
    assert quick_sort(quick_return_val) == [7, 11, 56, 93]


def test_string_in_list():
    """Assert error is raised with string input."""
    from quick_sort import quick_sort
    with pytest.raises(TypeError):
        quick_sort([1, 45, 'a', 5])


def test_empty_list():
    """Assert empty list is None."""
    from quick_sort import quick_sort
    alist = []
    quick_sort(alist)
    assert quick_sort(alist) == []


def test_same_items_in_list():
    """Assert list remins the same."""
    from quick_sort import quick_sort
    alist = [1, 1, 1, 1]
    quick_sort(alist)
    assert quick_sort(alist) == [1, 1, 1, 1]


def test_revers_order_list():
    """Assert reversed list is sorted."""
    from quick_sort import quick_sort
    alist = [5, 4, 3, 2, 1]
    quick_sort(alist)
    assert quick_sort(alist) == [1, 2, 3, 4, 5]