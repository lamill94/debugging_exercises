def encode(text, key): # text = 'theswiftfoxjumpedoverthelazydog', key = 'secretkey'
    cipher = make_cipher(key) # ['s', 'e', 'c', 'r', 't', 'k', 'y', 'a', 'b', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'z']

    ciphertext_chars = []
    for i in text: # theswiftfoxjumpedoverthelazydog - range of i is 0 - 30
        ciphered_char = chr(65 + cipher.index(i)) # first loop gets the index of 't' in cipher which is 4 -> chr(65 + 4) -> chr(69) = E
        ciphertext_chars.append(ciphered_char) # ['E', 'M', 'B', 'A', 'X', 'N', 'K', 'E', 'K', 'S', 'Y', 'O', 'V', 'Q', 'T', 'B', 'J', 'S', 'W', 'B', 'D', 'E', 'M', 'B', 'P', 'H', 'Z', 'G', 'J', 'S', 'L']
    
    return "".join(ciphertext_chars) # EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL

# Changed 65 - ord(i) to ord(i) - 65 to fix each plain_char and thus the plaintext_chars

def decode(encrypted, key): # encrypted = 'EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', key = 'secretkey'
    cipher = make_cipher(key) # ['s', 'e', 'c', 'r', 't', 'k', 'y', 'a', 'b', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'z']

    plaintext_chars = []
    for i in encrypted: # EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL - range of i is 0 - 30
        plain_char = cipher[ord(i) - 65] # first loop is cipher[ord(E) - 65] -> cipher[69 - 65] -> cipher[4] = t
        plaintext_chars.append(plain_char) # ['t', 'h', 'e', 's', 'w', 'i', 'f', 't', 'f', 'o', 'x', 'j', 'u', 'm', 'p', 'e', 'd', 'o', 'v', 'e', 'r', 't', 'h', 'e', 'l', 'a', 'z', 'y', 'd', 'o', 'g']
    
    return "".join(plaintext_chars) # theswiftfoxjumpedoverthelazydog

# Changed 98 to 97 and 1 to 0 to fix the alphabet list:

def make_cipher(key): # key = "secretkey"
    alphabet = [chr(i + 97) for i in range(0, 26)] # [List of a - z]
    cipher_with_duplicates = list(key) + alphabet # [s, e, c, r, e, t, k, e, y], [List of a-z]

    cipher = []
    for i in range(0, len(cipher_with_duplicates)): # len is 34 so range is 0 - 34
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    
    return cipher # duplicates letters have been removed  - ['s', 'e', 'c', 'r', 't', 'k', 'y', 'a', 'b', 'd', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'u', 'v', 'w', 'x', 'z']

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")@
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")

