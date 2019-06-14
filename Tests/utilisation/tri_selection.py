def selection(tab):
    for i in range(len(tab) - 1):
        min_index = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[min_index]:
                min_index = j

        tab[i], tab[min_index] = tab[i], tab[min_index]


def test_unique_element():
    tab = [1]
    
    selection(tab)
    assert [1] == tab
    
    
def test_deja_trie():
    tab = list(range(10))
    
    selection(tab)
    assert list(range(10)) == tab
    
def test_trie_a_l_envers():
    tab = list(range(10))
    tab.reverse()

    selection(tab)
    assert list(range(10)) == tab
    
def test_trie():
    tab = [1, 3, 2, 6, 4, 5]
    
    selection(tab)
    assert [1, 2, 3, 4, 5, 6] == tab