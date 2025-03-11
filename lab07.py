def vigenere_head(alphabet):
    return list(' ') + list(alphabet)

def vigenere_sq(alphabet):
    alphabet = list(alphabet)
    sq_list = [vigenere_head(alphabet)]
    for i in range(len(alphabet)):
        sq_list.append(list(alphabet[i]) + alphabet[i:] + alphabet[:i])
    return sq_list

def vigenere_sq_print(sq_list):
    for i, row in enumerate(sq_list):
        print(f"| {' | '.join(row)} |")
        if i == 0:
            print(f'{'|---'*len(row)}|')

def letter_to_index(letter, alphabet):
    return alphabet.upper().find(letter.upper())

def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index].lower()

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return index_to_letter(
        (letter_to_index(plaintext_letter, alphabet) +
        letter_to_index(key_letter, alphabet)) % len(alphabet), alphabet)

def non_vigenere_index(key_letter, cipher_text, alphabet):
    return index_to_letter(
        (letter_to_index(cipher_text, alphabet) -
         letter_to_index(key_letter, alphabet)) % len(alphabet), alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = []
    counter = 0
    for c in plaintext:
        if c == ' ':
            cipher_text.append(' ')
        elif c in alphabet:
            cipher_text.append(vigenere_index(key[counter % len(key)], c, alphabet))
            counter += 1
    return ''.join(cipher_text)

def decrypt_vigenere(key, cipher_text, alphabet):
    plaintext = []
    counter = 0
    for c in cipher_text:
        if c == ' ':
            plaintext.append(' ')
        elif c in alphabet:
            plaintext.append(non_vigenere_index(key[counter % len(key)], c, alphabet))
            counter += 1
    return ''.join(plaintext)

key = "BlUESMURF"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
message = "One small step for man, one giant leap for mankind."
#vigenere_sq_print(
    #vigenere_sq(alphabet))
#print(vigenere_head(alphabet))
#print(vigenere_index('b', 'b', alphabet))
#print(encrypt_vigenere(key, message, alphabet))
ct = encrypt_vigenere(key, message, alphabet)
print(ct)
print(decrypt_vigenere(key, ct, alphabet))