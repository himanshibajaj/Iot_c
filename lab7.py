# Experiment: Cryptographic Hash Functions and HMAC
# Aim: To understand and implement collision-resistant hash functions using HMAC
#hmac_experiment.py
import hashlib
import hmac

# Function to demonstrate hash functions
def hash_demo(message):
    print("\n--- HASH FUNCTION DEMONSTRATION ---")
    print("Original Message:", message)
   
    # SHA-256 Hash
    sha256_hash = hashlib.sha256(message.encode()).hexdigest()
    print("\nSHA-256 Hash:")
    print(sha256_hash)
   
    # SHA-512 Hash
    sha512_hash = hashlib.sha512(message.encode()).hexdigest()
    print("\nSHA-512 Hash:")
    print(sha512_hash)
   
    return sha256_hash, sha512_hash

# Function to demonstrate HMAC
def hmac_demo(message, key):
    print("\n--- HMAC DEMONSTRATION ---")
    print("Message:", message)
    print("Secret Key:", key)
   
    key_bytes = key.encode()
    message_bytes = message.encode()
   
    # Using SHA256 for HMAC
    hmac_sha256 = hmac.new(key_bytes, message_bytes, hashlib.sha256).hexdigest()
    print("\nHMAC using SHA-256:")
    print(hmac_sha256)
   
    # Using SHA512 for HMAC
    hmac_sha512 = hmac.new(key_bytes, message_bytes, hashlib.sha512).hexdigest()
    print("\nHMAC using SHA-512:")
    print(hmac_sha512)
   
    return hmac_sha256, hmac_sha512

# Main program
if __name__ == "__main__":
    print("==== Cryptographic Hash Functions and HMAC Implementation ====")
    message = input("Enter the message: ")
    key = input("Enter the secret key for HMAC: ")
   
    # Demonstrate Hash Functions
    hash_demo(message)
   
    # Demonstrate HMAC
    hmac_demo(message, key)
   
    print("\nExperiment Completed Successfully ")

