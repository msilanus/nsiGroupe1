import sys
sys.path.append('/home/marco/PycharmProjects/tp-de-programmation-msilanus/Bloc1/Tests/utilisation')
from mon_dichotomie import dichotomie


def test_tableau_vide():
    assert False == dichotomie(2,[])

def test_element_dans_tableau_au_milieu():
    assert True == dichotomie(5,[1,2,3,4,5,6,7,8,9])

def test_element_dans_tableau_avant_milieu():
    assert True == dichotomie(2,[1,2,3,4,5,6,7,8,9])

def test_element_dans_tableau_apres_milieu():
    assert True == dichotomie(7,[1,2,3,4,5,6,7,8,9])