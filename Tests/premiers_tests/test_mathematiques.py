from mathematiques import double

def test_double_0():
  assert double(0) == 0

def test_double_1():
  assert double(4) == 0b1001

def je_ne_suis_pas_execute():
  print("coucou !")

def test_double_2():
  assert double(9) == 18

je_ne_suis_pas_execute()
test_double_0()
test_double_1()
test_double_2()