def two_complement(value : int, nb_bits : int):
    """Return the two's complement of value with nb_bits bits"""

    assert -(2**(nb_bits-1)) <= value < 2**(nb_bits-1), "Value "+str(value) + " should have been between " + str(-2**(nb_bits-1)) + " and " + str(2**(nb_bits-1)-1)

    return ("{0:{fill}" + str(nb_bits) + "b}").format(value%(2**nb_bits),fill='0')

print(f'-3 en binaire : {two_complement(-3,16)}')
print(f'-15 en binaire : {two_complement(-15,16)}')
print(f'-256 en binaire : {two_complement(-256,16)}')
print(f'-1024 en binaire : {two_complement(-1024,16)}')

n1 = -15
n2 = 16
somme = n1+n2
print('')

print("{0:{fill}3d}".format(n1,fill=0), f': {two_complement(n1,16)}')
print("{0:{fill}3d}".format(n2,fill=0), f': {two_complement(n2,16)}')
print('----------------------')

print("{0:{fill}3d}".format(somme,fill=0), f': {two_complement(somme,16)}')


