#Vigenère Cipher
def char_to_num(c):
    return ord(c.upper()) - ord('A')

def num_to_char(n):
    return chr((n % 26) + ord('A'))

# Repeat key to match length of plaintext
def generate_key(text, key):
    new_key = ""
    j = 0
    for ch in text:
        if ch.isalpha():
            new_key += key[j % len(key)]
            j += 1
        else:
            new_key += ch
    return new_key

# Encryption
def encrypt(text, key):
    cipher = ""
    print("\n--- Encryption Steps ---")
    for i in range(len(text)):
        if text[i].isalpha():
            p = char_to_num(text[i])
            k = char_to_num(key[i])
            c = (p + k) % 26
            print(f"{text[i]}({p}) + {key[i]}({k}) = {c} -> {num_to_char(c)}")
            cipher += num_to_char(c)
        else:
            cipher += text[i]
    return cipher

# Decryption
def decrypt(cipher, key):
    plain = ""
    print("\n--- Decryption Steps ---")
    for i in range(len(cipher)):
        if cipher[i].isalpha():
            c = char_to_num(cipher[i])
            k = char_to_num(key[i])
            p = (c - k + 26) % 26
            print(f"{cipher[i]}({c}) - {key[i]}({k}) = {p} -> {num_to_char(p)}")
            plain += num_to_char(p)
        else:
            plain += cipher[i]
    return plain

# Main program
plaintext = input("Enter Plaintext: ").upper()
key = input("Enter Key: ").upper()

new_key = generate_key(plaintext, key)
print("\nGenerated Key (repeated):", new_key)

cipher = encrypt(plaintext, new_key)
print("\nCipher Text:", cipher)

decrypted = decrypt(cipher, new_key)
print("\nDecrypted Text:", decrypted)
