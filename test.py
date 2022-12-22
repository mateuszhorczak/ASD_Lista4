# Program do testowania poprawnosci konwersji BinToTxt i TxtToBin
# Nie wykorzystywany w programie, na pamiatke xd

def from_binary_convert_to_string(word):
    int_word = int(word, base = 2)
    str_word = int_word.to_bytes((int_word.bit_length() + 7) // 8, 'big').decode()
    return str_word

def from_string_covert_to_binary(word):
    print("The original string is : " + str(word))
    res = ''.join(format(i, '08b') for i in bytearray(word, encoding='utf-8'))
    print("The string after binary conversion : " + str(res))


from_string_covert_to_binary('Szymanski')
bin_data = '010100110111101001111001011011010110000101101110011100110110101101101001'
print("The original binary string is      : " + bin_data)
print("The string after conversion: " + from_binary_convert_to_string(bin_data))
