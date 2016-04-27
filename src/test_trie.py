"""Test file for Trie."""
import pytest

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



