def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet.index(letter.lower())

def rotate_character(char, rot):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char not in alphabet_lower and char not in alphabet_upper:
        return char
    position_char = alphabet_position(char) + rot
    if position_char >= 26:
        position_char = position_char - 26
    if char == char.upper():
        return alphabet_upper[position_char]
    elif char == char.lower():
        return alphabet_lower[position_char]

def encrypt(text, rot):
    rot_text = ""
    for letter in text:
        rot_text += rotate_character(letter, rot)
    return rot_text
