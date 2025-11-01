#Substitution ciphers and Transposition Cipher.
import math

# Normalize text (only alphabets, uppercase)
def normalize(text):
    return ''.join([c.upper() for c in text if c.isalpha()])

# Substitution Cipher (Caesar)
def caesar_encrypt(plain, shift=3):
    return ''.join(chr((ord(c)-65+shift) % 26 + 65) for c in plain)

def caesar_decrypt(cipher, shift=3):
    return ''.join(chr((ord(c)-65-shift) % 26 + 65) for c in cipher)

# Show matrix (for visualization)
def display_matrix(text, key, pad='X'):
    ncols = len(key)
    nrows = math.ceil(len(text) / ncols)
    grid = [['' for _ in range(ncols)] for _ in range(nrows)]
    it = iter(text)
    for r in range(nrows):
        for c in range(ncols):
            try:
                grid[r][c] = next(it)
            except StopIteration:
                grid[r][c] = pad
    
    print("\nMatrix Representation (Rows x Cols):")
    print("Key: ", " ".join(key))
    for row in grid:
        print(" ".join(row))
    return grid

# Columnar Transposition
def columnar_encrypt(text, key, pad='X'):
    ncols = len(key)
    nrows = math.ceil(len(text) / ncols)
    grid = [['' for _ in range(ncols)] for _ in range(nrows)]
    it = iter(text)
    for r in range(nrows):
        for c in range(ncols):
            try:
                grid[r][c] = next(it)
            except StopIteration:
                grid[r][c] = pad
    order = sorted(range(ncols), key=lambda i: (key[i], i))
    cipher = []
    for col in order:
        for row in range(nrows):
            cipher.append(grid[row][col])
    return ''.join(cipher)

def columnar_decrypt(cipher, key, pad='X'):
    ncols = len(key)
    nrows = math.ceil(len(cipher) / ncols)
    order = sorted(range(ncols), key=lambda i: (key[i], i))
    grid = [['' for _ in range(ncols)] for _ in range(nrows)]
    pos = 0
    for col in order:
        for row in range(nrows):
            grid[row][col] = cipher[pos]
            pos += 1
    text = ''.join(grid[r][c] for r in range(nrows) for c in range(ncols))
    return text.rstrip(pad), grid

# Product Cipher: Encryption
def product_encrypt(plaintext, shift, key, pad='X'):
    p = normalize(plaintext)
    sub = caesar_encrypt(p, shift)
    print("\nAfter Substitution (Caesar +{}): {}".format(shift, sub))
    display_matrix(sub, key, pad)
    cipher = columnar_encrypt(sub, key, pad)
    return sub, cipher

# Product Cipher: Decryption
def product_decrypt(ciphertext, shift, key, pad='X'):
    sub, grid = columnar_decrypt(ciphertext, key, pad)
    print("\nMatrix Recovered (Decryption Step):")
    print("Key: ", " ".join(key))
    for row in grid:
        print(" ".join(row))
    recovered = caesar_decrypt(sub, shift)
    return sub, recovered

# Main Program
if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter shift value (integer): "))
    key = input("Enter transposition key (string): ").upper()

    print("\n--- ENCRYPTION ---")
    norm = normalize(plaintext)
    print("Normalized: ", norm)
    sub, cipher = product_encrypt(plaintext, shift, key)
    print("Final Ciphertext (Product Cipher):", cipher)

    print("\n--- DECRYPTION ---")
    recovered_sub, recovered_plain = product_decrypt(cipher, shift, key)
    print("Recovered substituted text:", recovered_sub)
    print("Decrypted Plaintext:", recovered_plain)
