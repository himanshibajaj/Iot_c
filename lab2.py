# Playfair Cipher Implementation in Python
# ----------------------------------------
# Educational version (for lab demonstration)

def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()
    
    # Add key letters
    for char in key:
        if char.isalpha() and char not in used:
            matrix.append(char)
            used.add(char)

    # Add remaining letters (A-Z without J)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)
            used.add(char)

    # Convert to 5x5 matrix
    playfair = [matrix[i:i+5] for i in range(0, 25, 5)]
    return playfair

def find_pos(matrix, ch):
    if ch == 'J': 
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j
    return None, None

def make_digraphs(text):
    text = text.upper().replace("J", "I")
    clean_text = ''.join([c for c in text if c.isalpha()])
    
    digraphs = []
    i = 0
    while i < len(clean_text):
        first = clean_text[i]
        if i + 1 < len(clean_text):
            second = clean_text[i + 1]
            if first == second:
                second = 'X'
                i += 1
            else:
                i += 2
        else:
            second = 'X'
            i += 1
        digraphs.append((first, second))
    return digraphs

def encrypt_pair(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)

    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def decrypt_pair(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)

    if r1 == r2:
        return matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
    elif c1 == c2:
        return matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def encrypt(text, matrix):
    digraphs = make_digraphs(text)
    cipher = ''.join([encrypt_pair(matrix, a, b) for a, b in digraphs])
    return cipher, digraphs

def decrypt(cipher, matrix):
    digraphs = make_digraphs(cipher)
    plain = ''.join([decrypt_pair(matrix, a, b) for a, b in digraphs])
    return plain

# Main program
if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    matrix = generate_matrix(key)
    print("\nPlayfair 5x5 Matrix:")
    for row in matrix:
        print(' '.join(row))

    cipher, digraphs = encrypt(plaintext, matrix)

    print("\nDigraphs:", ' '.join([''.join(d) for d in digraphs]))
    print("\nEncrypted text:", cipher)
    decrypted = decrypt(cipher, matrix)
    print("Decrypted text:", decrypted)

