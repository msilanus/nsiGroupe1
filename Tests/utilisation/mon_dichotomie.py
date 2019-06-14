def dichotomie(nombre,tableau):
    '''

    :param nombre: int
    :param tableau: tableau d'entiers triés
    :return: true or false
    '''
    if len(tableau)<1:
        return False
    milieu = len(tableau) // 2
    print('=',tableau[milieu])

    if nombre == tableau[milieu]:
        return True

    if nombre < tableau[milieu]:
        return dichotomie(nombre,tableau[:milieu])

    if nombre > tableau[len(tableau) // 2]:
        return dichotomie(nombre,tableau[milieu+1:])


def test_tableau_vide():
    assert False == dichotomie(2,[])

def test_element_dans_tableau_au_milieu():
    assert True == dichotomie(5,[1,2,3,4,5,6,7,8,9])

def test_element_dans_tableau_avant_milieu():
    assert True == dichotomie(2,[1,2,3,4,5,6,7,8,9])

def test_element_dans_tableau_apres_milieu():
    assert True == dichotomie(7,[1,2,3,4,5,6,7,8,9])

print(dichotomie(4,list(range(50))))