# RSA Encryption and Decryption with User Input
# ---------------------------------------------
# Educational implementation for lab demonstration

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that gcd(e, phi) = 1
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    # Compute modular inverse of e (private exponent)
    d = pow(e, -1, phi)

    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    cipher = [(pow(ord(ch), e, n)) for ch in message]
    return cipher

def decrypt(cipher, private_key):
    d, n = private_key
    plain = [chr(pow(num, d, n)) for num in cipher]
    return ''.join(plain)

# Main Program
if __name__ == "__main__":
    print("=== RSA Cryptosystem ===\n")

    # Step 1: Take input from user
    p = int(input("Enter first prime number (p): "))
    q = int(input("Enter second prime number (q): "))
    message = input("Enter the message to encrypt: ")

    # Step 2: Generate keys
    public_key, private_key = generate_keys(p, q)

    print("\nPublic Key :", public_key)
    print("Private Key:", private_key)

    # Step 3: Encryption
    cipher = encrypt(message, public_key)

    # Step 4: Decryption
    decrypted = decrypt(cipher, private_key)

    print("\nOriginal Message:", message)
    print("Encrypted Message:", cipher)
    print("Decrypted Message:", decrypted)

    print("\n=== Code Execution Successful ===")
