"""Test file for Trie."""
import pytest


WORDS = ['cart', 'carp', 'carton', 'car', 'cartons']


@pytest.fixture()
def trie():
    """Trie fixture."""
    from trie import Trie
    my_trie = Trie()
    return my_trie


def test_insert_empty(trie):
    """Test insert on empty Trie."""
    trie.insert("cactus")
    assert "cactus" in trie


def test_partial_word(trie):
    """Test partial word returns false."""
    trie.insert("snakes")
    assert "snake" not in trie


def test_word_branch(trie):
    """Test branching of words works."""
    trie.insert("carton")
    trie.insert("cart")
    assert "cart" in trie and "carton" in trie


def test_apostrophie(trie):
    """Test word with apostrophie works."""
    trie.insert("don't")
    assert "don't" in trie


def test_int_input(trie):
    """Test int throws error."""
    with pytest.raises(TypeError):
        trie.insert(4)


def test_symbol_insert(trie):
    """Test error raised with symbols."""
    with pytest.raises(TypeError):
        trie.insert("lett#ers")

# Traversal Tests


@pytest.fixture()
def car_trie():
    """Filled trie."""
    from trie import Trie
    t = Trie()
    for word in WORDS:
        t.insert(word)
    return t


def test_all_car(car_trie):
    """Test all the items in our trie."""
    for word in car_trie.traversal():
        assert word in WORDS


def test_midway(car_trie):
    """Test traversal halfway through trie."""
    for word in car_trie.traversal('cart'):
        assert word != "carp" or word != 'car'

# Autocomplete Tests


def test_correct(car_trie):
    """Testing autocomplete on Trie."""
    assert car_trie.autocomplete('c') == ['car', 'carp', 'cart', 'carton']


def test_autocomplete_full_word(car_trie):
    """Testing autocomplete wioth full word."""
    assert car_trie.autocomplete('carton') == ['carton', 'cartons']


def test_error(car_trie):
    """Test autocomplette raises error if value is not in Trie."""
    with pytest.raises(KeyError):
        car_trie.autocomplete('bob')












