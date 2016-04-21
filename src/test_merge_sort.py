"""Test merge sort."""


def test_merge_sort():
    """Assert that it works for tox."""
    from merge_sort import merge_sort
    merge_return_val = [56, 93, 7, 11]
    merge_sort(merge_return_val)
    assert merge_return_val == [7, 11, 56, 93]
