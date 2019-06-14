from decode_variable import *
from pathlib import Path

table_decode = build_decoding_table(variable_table)
table_encode = fixed_table()
table_decode_fixe = build_decoding_table(fixed_table())
#print(table_decode_fixe)

#Ouvrir en lecture
file = open("chiffre_variable.txt","r")

#Ouvrir en écriture "a" écrit à la suite du fichier
#Ouvrir en écriture "w" écrase le fichier s'il existe déjà

decoded_file = Path("chiffre_variable_decoder.txt")
decoded_file = open("chiffre_variable_decoder.txt","w")
encoded_file = open("les_miserables_chiffre_fixe.txt","w")



for line in file:
    line=line.strip("\n")
    line_decoded = variable_decode(line,table_decode)+"\n"     # le \n est ajouté ici : trop tôt
    line_encoded = encode_fixe(line_decoded,table_encode)+"\n" # il est décodé donc transfomé en espace

    decoded_file.write(line_decoded)
    encoded_file.write(line_encoded) #avec un espace en trop à la fin de chaque ligne !

file.close()
decoded_file.close()
encoded_file.close()

file_enfin = Path("chiffre_fixe_decoder.txt")
file_enfin = open("chiffre_fixe_decoder.txt","w")


file_fixe = open("les_miserables_chiffre_fixe.txt","r")
#tout_dans_une_ligne=""
for line in file_fixe:
    line=line.strip("\n")
    line_decoded_fixe = decode(line, table_decode_fixe) + "\n"
    file_enfin.write(line_decoded_fixe)

file.close()
file_enfin.close()

print('Fin')