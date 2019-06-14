import unicodedata


def sans_accent(texte):
    texte_normalise = unicodedata.normalize('NFD', texte)
    texte_ascii = texte_normalise.encode('ascii','ignore')
    texte_sans_accent =texte_ascii.decode('utf-8')

    return texte_sans_accent


def majuscules_sans_accent(texte):
    return sans_accent(texte).upper()


def test_sans_accent():
    s = "éçà ü ?"
    assert sans_accent(s) == "eca u ?"


def test_majuscule_sans_accent():
    s = "éçà ü ?"
    assert majuscules_sans_accent(s) == "ECA U ?"

