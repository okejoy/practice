from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(text_input, shift_amount, direction_value):
    end_text = " "
    if direction_value == "decode":
        shift_amount *= -1
    for char in text_input:
        # modifying it to allow symbols and numbers
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction_value}d text is {end_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # this is used when the shift number entered is large
    # the modulos operator gives us the remainder and the remainder is the one
    # used to get the shift number
    if shift > 26:
        shift = shift % 26
    else:
        shift = shift
    ceaser(text_input=text, shift_amount=shift, direction_value=direction)
    approval = input("Type 'yes' if you would lie to continue. Else type 'no' to quit \n")
    if approval == 'no':
        print("Goodbye")
        should_continue = False
