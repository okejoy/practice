
# a code responsible for encryption ad decryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text_inputted, shift_number):
    cipher_text = " "
    for letter in text_inputted:
        position = alphabet.index(letter)
        new_position = position + shift_number
        cipher_text += alphabet[new_position]
    print(f"The encoded text is {cipher_text}")


def decrypt(text_input, shift_number):
    cipher_text = " "
    for letter in text_input:
        position = alphabet.index(letter)
        shift_amount = position - shift_number
        cipher_text += alphabet[shift_amount]
    print(f"The decoded text is {cipher_text}")


if direction == 'encode':
    encrypt(shift_number=shift, text_inputted=text)
elif direction == 'decode':
    decrypt(shift_number=shift, text_input=text)
