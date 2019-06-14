from struct import pack

def float_to_bin(f):

    bytes = pack('!f', f)
    binary = ""
    for byte in bytes:
        binary += "{:{fill}8b}".format(byte,fill='0')

    return binary


print(f'{float_to_bin(-2**127)}')
