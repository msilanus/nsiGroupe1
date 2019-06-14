import sys
sys.path.append('/home/marco/PycharmProjects/tp-de-programmation-msilanus/Bloc1/Tests/utilisation')
from cesar import *

def test_code_cesar():
    assert code_cesar('E') == {'A': 'E', 'B': 'F', 'C': 'G', 'D': 'H', 'E': 'I', 'F': 'J', 'G': 'K', 'H': 'L', 'I': 'M', 'J': 'N', 'K': 'O', 'L': 'P', 'M': 'Q', 'N': 'R', 'O': 'S', 'P': 'T', 'Q': 'U', 'R': 'V', 'S': 'W', 'T': 'X', 'U': 'Y', 'V': 'Z', 'W': 'A', 'X': 'B', 'Y': 'C', 'Z': 'D'}


def test_code_cesar_reverse():
    assert code_cesar_reverse('E') == {'E': 'A', 'F': 'B', 'G': 'C', 'H': 'D', 'I': 'E', 'J': 'F', 'K': 'G', 'L': 'H', 'M': 'I', 'N': 'J', 'O': 'K', 'P': 'L', 'Q': 'M', 'R': 'N', 'S': 'O', 'T': 'P', 'U': 'Q', 'V': 'R', 'W': 'S', 'X': 'T', 'Y': 'U', 'Z': 'V', 'A': 'W', 'B': 'X', 'C': 'Y', 'D': 'Z'}


def test_encode_cesar():
    assert encode_cesar('E', "LE VENDREDI C'EST ALGORITHMIE") == "PI ZIRHVIHM G'IWX EPKSVMXLQMI"


def test_decode_cesar():
    assert decode_cesar('E', "PI ZIRHVIHM G'IWX EPKSVMXLQMI") == "LE VENDREDI C'EST ALGORITHMIE"


def test_code_lettres():
    assert code_lettres('A', 'E') == 'E'
    assert code_lettres('X', 'V') == 'Y'