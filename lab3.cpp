#include <iostream>
#include <string>
using namespace std;

// Function to convert a character to number (A=0, B=1, ..., Z=25)
int charToNum(char c) {
    return toupper(c) - 'A';
}

// Function to convert number back to character
char numToChar(int n) {
    return char((n % 26) + 'A');
}

// Function to repeat the key to match plaintext length
string generateKey(string text, string key) {
    int n = text.size();
    string newKey = "";
    for (int i = 0, j = 0; i < n; i++) {
        if (isalpha(text[i])) {
            newKey += key[j % key.size()];
            j++;
        } else {
            newKey += text[i]; // keep spaces/punctuation same
        }
    }
    return newKey;
}

// Encryption
string encrypt(string text, string key) {
    string cipher = "";
    cout << "\n--- Encryption Steps ---\n";
    for (int i = 0; i < text.size(); i++) {
        if (isalpha(text[i])) {
            int p = charToNum(text[i]);
            int k = charToNum(key[i]);
            int c = (p + k) % 26;

            cout << text[i] << "(" << p << ") + " << key[i] << "(" << k << ") = "
                 << c << " -> " << numToChar(c) << endl;

            cipher += numToChar(c);
        } else {
            cipher += text[i]; // spaces or symbols unchanged
        }
    }
    return cipher;
}

// Decryption
string decrypt(string cipher, string key) {
    string plain = "";
    cout << "\n--- Decryption Steps ---\n";
    for (int i = 0; i < cipher.size(); i++) {
        if (isalpha(cipher[i])) {
            int c = charToNum(cipher[i]);
            int k = charToNum(key[i]);
            int p = (c - k + 26) % 26;

            cout << cipher[i] << "(" << c << ") - " << key[i] << "(" << k << ") = "
                 << p << " -> " << numToChar(p) << endl;

            plain += numToChar(p);
        } else {
            plain += cipher[i];
        }
    }
    return plain;
}

int main() {
    string plaintext, key;

    cout << "Enter Plaintext: ";
    getline(cin, plaintext);

    cout << "Enter Key: ";
    getline(cin, key);

    // Convert both to uppercase (for uniformity)
    for (auto &c : plaintext) c = toupper(c);
    for (auto &c : key) c = toupper(c);

    // Generate repeated key
    string newKey = generateKey(plaintext, key);
    cout << "\nGenerated Key (repeated): " << newKey << endl;

    // Encrypt
    string cipher = encrypt(plaintext, newKey);
    cout << "\nCipher Text: " << cipher << endl;

    // Decrypt
    string decrypted = decrypt(cipher, newKey);
    cout << "\nDecrypted Text: " << decrypted << endl;

    return 0;
}
