def dichotomie(element, tableau):
    if len(tableau) < 1:
        return False

    if element == tableau[len(tableau) // 2]:
        return True
    elif element < tableau[len(tableau) // 2]:
        return dichotomie(element, tableau[:len(tableau) // 2])
    else:
        return dichotomie(element, tableau[len(tableau) // 2 + 1:])    

    
def test_vide():
    assert False == dichotomie(7, [])    

def test_un_element_pas_dedant():
    assert False == dichotomie(7, [1])    

def test_un_element_dedant():
    assert True == dichotomie(7, [7])    
    
def test_element_milieu():
    assert True == dichotomie(7, [2, 7, 12])    

def test_element_pas_milieu_dessous_ok():
    assert True == dichotomie(2, [2, 7, 12])    
    
def test_element_pas_milieu_dessus_ok():
    assert True == dichotomie(12, [2, 7, 12])    

def test_element_pas_milieu_dessus_pas_ok():
    assert False == dichotomie(0, [2, 7, 12])    

def test_element_pair_dessous_ok():
    assert True == dichotomie(2, [2, 12])    
    
def test_element_pas_milieu_dessus_ok():
    assert True == dichotomie(12, [2, 12])    

def test_element_pas_milieu_dessus_pas_ok():
    assert False == dichotomie(0, [2, 12])    

def test_gros():
    assert True == dichotomie(18, list(range(20)))
    assert False == dichotomie(-3, list(range(20)))
    
