def decipher(ciphertext, shift):
    deciphered_text = ""

    for char in ciphertext:
        if char.isalpha():  # Check if the character is an alphabet letter
            is_upper = char.isupper()
            char = char.lower()

            # Decipher the letter by shifting it in the opposite direction
            deciphered_char = chr((ord(char) - shift - ord("a")) % 26 + ord("a"))

            if is_upper:
                deciphered_char = deciphered_char.upper()

            deciphered_text += deciphered_char
        else:
            deciphered_text += char

    return deciphered_text
