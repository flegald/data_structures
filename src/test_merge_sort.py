"""Test merge sort."""
import pytest


def test_merge_sort():
    """Assert that it works for tox."""
    from merge_sort import merge_sort
    merge_return_val = [56, 93, 7, 11]
    merge_sort(merge_return_val)
    assert merge_return_val == [7, 11, 56, 93]


def test_string_in_list():
    """Assert error is raised with string input."""
    from merge_sort import merge_sort
    with pytest.raises(TypeError):
        merge_sort([1, 45, 'a', 5])


def test_empty_list():
    """Assert empty list is None."""
    from merge_sort import merge_sort
    alist = []
    merge_sort(alist)
    assert alist == []


def test_same_items_in_list():
    """Assert list remins the same."""
    from merge_sort import merge_sort
    alist = [1, 1, 1, 1]
    merge_sort(alist)
    assert alist == [1, 1, 1, 1]


def test_revers_order_list():
    """Assert reversed list is sorted."""
    from merge_sort import merge_sort
    alist = [5, 4, 3, 2, 1]
    merge_sort(alist)
    assert alist == [1, 2, 3, 4, 5]
