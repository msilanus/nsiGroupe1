import sys
sys.path.append('/home/marco/PycharmProjects/tp-de-programmation-msilanus/Bloc1/Tests/utilisation')
from tri_selection import selection

def test_unique_element():
    tab = [1]

    selection(tab)
    assert [1] == tab


def test_deja_trie():
    tab = list(range(20))

    selection(tab)
    assert list(range(20)) == tab


def test_trie_a_l_envers():
    tab = list(range(20))
    tab.reverse()

    selection(tab)
    assert list(range(20)) == tab


def test_trie():
    tab = [1, 3, 2, 6, 4, 5]

    selection(tab)
    assert [1, 2, 3, 4, 5, 6] == tab