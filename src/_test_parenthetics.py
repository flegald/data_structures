# -*- coding: utf-8 -*-
"""Test module for parenthetics."""
import pytest


WORDS = [
        [')', -1],
        ['))', -1],
        ['())', -1],
        ['()', 0],
        ['(()', 1],
        ['((', 1],
        ['(', 1],
        ['(sdghgjgh)', 0],
        ]


@pytest.mark.parametrize('WORDS', WORDS)
def test_parenthetics(WORDS):
    """Test parenthetics method."""
    from parenthetics import parenthetics
    assert parenthetics(WORDS[0]) is WORDS[1]
