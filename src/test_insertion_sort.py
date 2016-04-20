"""Test insertion sort."""


def test_insertion_sort():
    """Assert that it works for tox."""
    from insertion_sort import insertion_sort
    insertion_return_val = [56, 93, 7, 11]
    insertion_sort(insertion_return_val)
    assert insertion_return_val == [7, 11, 56, 93]
