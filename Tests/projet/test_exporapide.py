from exporapide import expo_rapide


def test_expo_rapide_de_1():
    assert 123 == expo_rapide(123,1)

def test_expo_rapide_paire():
    assert 16 == expo_rapide(4,2)

def test_expo_rapide_impair():
    assert 8 == expo_rapide(2,3)

def test_expo_rapide_n_vaux_0():
    assert 1 == expo_rapide(2, 0)

def test_expo_rapide_x_vaux_0():
    assert 0 == expo_rapide(0, 2)