# -*- coding: utf-8 -*-
"""Module to test parenthetics of string input."""


def parenthetics(input_str):
    """Method to test for unmatched parenthesis."""
    counter = 0
    while counter >= 0:
        for i in input_str:
            if i is ')':
                counter -= 1
            elif i is '(':
                counter += 1
    if counter > 0:
        counter = 1
    return counter
