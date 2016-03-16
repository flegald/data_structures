#  _*_ cogind:utf-8 _*_
"""Check parentheses."""


def check_parens(string):
    """Check for mathcing parentheses."""
    test_list = []
    idx = 0
    while idx < len(string):
        marker = string[idx]
        if marker == "(":
            test_list.append(marker)
        elif marker == ")":
            if len(test_list) == 0:
                return -1
            else:
                test_list.pop()
        idx += 1
    if len(test_list) == 0:
        return 0
    else:
        return 1
