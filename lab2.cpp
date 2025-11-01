//playcipher
#include <iostream>
#include <cstring>
using namespace std;

char matrix[5][5];

// Function to prepare the key and fill the matrix
void generateMatrix(char key[]) {
    bool used[26] = {false};
    used['J' - 'A'] = true; // J is merged with I
    int row = 0, col = 0;

    // Place key into matrix
    for (int i = 0; key[i] != '\0'; i++) {
        char c = toupper(key[i]);
        if (c < 'A' || c > 'Z') continue;
        if (c == 'J') c = 'I';
        if (!used[c - 'A']) {
            matrix[row][col++] = c;
            used[c - 'A'] = true;
            if (col == 5) { col = 0; row++; }
        }
    }

    // Fill remaining letters
    for (char c = 'A'; c <= 'Z'; c++) {
        if (!used[c - 'A']) {
            matrix[row][col++] = c;
            used[c - 'A'] = true;
            if (col == 5) { col = 0; row++; }
        }
    }
}

// Find position of a letter
void findPos(char c, int &r, int &cpos) {
    if (c == 'J') c = 'I';
    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
            if (matrix[i][j] == c) {
                r = i; cpos = j;
                return;
            }
}

// Prepare digraphs (pairs)
int makeDigraphs(char text[], char digraphs[][2]) {
    char prepared[100];
    int len = 0;

    // Clean and replace J -> I
    for (int i = 0; text[i] != '\0'; i++) {
        char c = toupper(text[i]);
        if (c < 'A' || c > 'Z') continue;
        if (c == 'J') c = 'I';
        prepared[len++] = c;
    }
    prepared[len] = '\0';

    // Make digraphs
    int count = 0;
    for (int i = 0; i < len; i++) {
        char first = prepared[i];
        char second;
        if (i + 1 < len) {
            second = prepared[i + 1];
            if (first == second) {
                second = 'X';
            } else {
                i++;
            }
        } else {
            second = 'X';
        }
        digraphs[count][0] = first;
        digraphs[count][1] = second;
        count++;
    }
    return count;
}

// Encrypt
void encrypt(char digraphs[][2], int count, char result[]) {
    int idx = 0;
    for (int i = 0; i < count; i++) {
        int r1, c1, r2, c2;
        findPos(digraphs[i][0], r1, c1);
        findPos(digraphs[i][1], r2, c2);

        if (r1 == r2) { // same row
            result[idx++] = matrix[r1][(c1 + 1) % 5];
            result[idx++] = matrix[r2][(c2 + 1) % 5];
        }
        else if (c1 == c2) { // same column
            result[idx++] = matrix[(r1 + 1) % 5][c1];
            result[idx++] = matrix[(r2 + 1) % 5][c2];
        }
        else { // rectangle
            result[idx++] = matrix[r1][c2];
            result[idx++] = matrix[r2][c1];
        }
    }
    result[idx] = '\0';
}

// Decrypt
void decrypt(char digraphs[][2], int count, char result[]) {
    int idx = 0;
    for (int i = 0; i < count; i++) {
        int r1, c1, r2, c2;
        findPos(digraphs[i][0], r1, c1);
        findPos(digraphs[i][1], r2, c2);

        if (r1 == r2) { // same row
            result[idx++] = matrix[r1][(c1 + 4) % 5];
            result[idx++] = matrix[r2][(c2 + 4) % 5];
        }
        else if (c1 == c2) { // same column
            result[idx++] = matrix[(r1 + 4) % 5][c1];
            result[idx++] = matrix[(r2 + 4) % 5][c2];
        }
        else { // rectangle
            result[idx++] = matrix[r1][c2];
            result[idx++] = matrix[r2][c1];
        }
    }
    result[idx] = '\0';
}

int main() {
    char plaintext[100], key[100];
    cout << "Enter plaintext: ";
    cin.getline(plaintext, 100);
    cout << "Enter key: ";
    cin.getline(key, 100);

    // 1. Generate matrix
    generateMatrix(key);

    cout << "\nPlayfair 5x5 Matrix:\n";
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++)
            cout << matrix[i][j] << " ";
        cout << endl;
    }

    // 2. Make digraphs
    char digraphs[50][2];
    int count = makeDigraphs(plaintext, digraphs);

    cout << "\nDigraphs: ";
    for (int i = 0; i < count; i++)
        cout << digraphs[i][0] << digraphs[i][1] << " ";
    cout << endl;

    // 3. Encrypt
    char cipher[100];
    encrypt(digraphs, count, cipher);
    cout << "\nEncrypted text: " << cipher << endl;

    // 4. Decrypt
    char cipherDigraphs[50][2];
    int ccount = makeDigraphs(cipher, cipherDigraphs);
    char decrypted[100];
    decrypt(cipherDigraphs, ccount, decrypted);
    cout << "Decrypted text: " << decrypted << endl;
    return 0;
}
