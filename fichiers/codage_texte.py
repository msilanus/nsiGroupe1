variable_table = {'a':'1010','b':'0010011','c':'01001','d':'01110','e':'110','f':'0111100','g':'0111110','h':'0010010','i':'1000','j':'011111110','k':'011111111001','l':'0001','m':'00101','n':'1001','o':'0000','p':'01000','q':'0111101','r':'0101','s':'1011','t':'0110','u':'0011','v':'001000','w':'011111111000','x':'01111110','y':'0111111111','z':'01111111101',' ':'111'}


def increment():
    fixed_tabe = {}
    for i in range(0,26):
        lettre = chr(i+97)
        code = "{0:{fill}5b}".format(i,fill='0')
        fixed_tabe[lettre]=code
    fixed_tabe[' ']='11010'
    print(fixed_tabe)
    return fixed_tabe


def encode(message, table):
    message_encode = ""
    for lettre in message:
        try:
            message_encode += table[lettre]
        except:
            message_encode += table[" "]
    return message_encode


def decode(message_coder,table):
    message = ""
    for i in range(0,len(message_coder),5):
        message += table[message_coder[i:i+5]]
    return message

def build_decoding_table(table):
    decode_table = {}
    for key,value in table.items():
        decode_table[value] = key
    return decode_table

def variable_decode(message_coder: str, table: dict) -> str:
    """Décode le chiffré donné en argument selon le codage variable"""
    #print(table)
    #print(f'A décoder : {message_coder}')
    message = ''
    i = 0
    code = ''
    while i < len(message_coder):
        code += message_coder[i]
        #print(code)
        if code in table.keys():
            message += table[code]
            #print(f'==> {table[code]}')
            code = ''
        i += 1
    return message

assert  encode('ozedw',increment()) == encode("decode",variable_table)

print(f"Message encoder fixe : pas pousser mémé dans les orties' => {encode('pas pousser mémé dans les orties',increment())}")

print(f'Message encoder variable : information => {encode("information",variable_table)}')

print(build_decoding_table(increment()))

print(f'Decodage : {decode("0111100000100101101001111011101010010010100100010010001110100110011010011001101011010000110000001101100101101001011001001001011010011101000110011010000010010010",build_decoding_table(increment()))}')

print(f'Decodage : {variable_decode("100010010111100000001010010110100110100000001001",build_decoding_table(variable_table))}')

print(f'Decodage erreur sur caractère 2 : {variable_decode("110010010111100000001010010110100110100000001001",build_decoding_table(variable_table))}')

print(f'Decodage erreur sur caractère 3 : {variable_decode("101010010111100000001010010110100110100000001001",build_decoding_table(variable_table))}')

print(f'Decodage erreur sur caractère 12 : {variable_decode("100010010110100000001010010110100110100000001001",build_decoding_table(variable_table))}')