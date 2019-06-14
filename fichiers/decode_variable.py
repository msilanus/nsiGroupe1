variable_table = {'a':'1010','b':'0010011','c':'01001','d':'01110','e':'110','f':'0111100','g':'0111110','h':'0010010','i':'1000','j':'011111110','k':'011111111001','l':'0001','m':'00101','n':'1001','o':'0000','p':'01000','q':'0111101','r':'0101','s':'1011','t':'0110','u':'0011','v':'001000','w':'011111111000','x':'01111110','y':'0111111111','z':'01111111101',' ':'111'}


def encode(message, table):
    message_encode = ""
    for lettre in message:
        try:
            message_encode += table[lettre]
        except:
            message_encode += table[" "]
    return message_encode


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

def encode_fixe(message, table):
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

def fixed_table():
    table = {}
    for i in range(0,26):
        lettre = chr(i+97)
        code = "{0:{fill}5b}".format(i,fill='0')
        table[lettre]=code
    table[' ']='11010'
    return table
