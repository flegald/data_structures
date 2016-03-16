#  _*_ cogind:utf-8 _*_
"""Check parentheses test."""
import pytest

TEST_STRINGS = {
    ("(grape nuts)", 0),
    ("te(st stri)ng", 0),
    ("(())(())()()(())((()))", 0),
    ("(((((((((())))))))))", 0),
    ("(Mr Bumpy(2.0)", 1),
    ("(((()))", 1),
    ("sp(ace)G()()((se)", 1),
    ("(Code (school)", 1),
    ("(((()))))", -1),
    (")()()(", -1),
    ("Spe)ak easy", -1),
}


@pytest.mark.parametrize("fn, result", TEST_STRINGS)
def test_check_parens(fn, result):
    """Test check_parens function."""
    from check_parensDavid import check_parens
    assert check_parens(fn) == result
