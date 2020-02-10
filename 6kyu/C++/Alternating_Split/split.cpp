// Simple Encryption #1 - Alternating Split
// https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/cpp

#include <iostream>
#include <string>

using namespace std;

string encrypt(string text, int n) {
    if (text.empty()) return "";
    string even;
    string odd;
    int m;

    text.size() % 2 == 0 ? m = 0 : m = 1;
    cout << "Start: \"" << text << "\" Size: " << text.size() << " M: " << m << endl;
    
    for (int x = 0; x < n; x++) {
        for (int i = 0; i < text.size()-m; i += 2) {
            odd += text[i];
            even += text[i+1];
            cout << i << ": " << text[i] << " " << i+2 << ": " << text[i+1] << endl;
        }
        cout << "Even: \"" << even << "\"" << " Odd: \"" << odd << "\"" << endl;
        m == 1 ? text = even + odd + text.back() : text = even + odd;
        even.clear(), odd.clear();
        cout << "\"" << text << "\"\n" << endl;
    }

    return text;
}

string decrypt(string encryptedText, int n) {
    if (encryptedText.empty()) {
        return encryptedText;
    } else if(n == 0) {
        return encryptedText;
    }
    string left;
    string right;
    string out;
    cout << "Start: \"" << encryptedText << "\" Size: " << encryptedText.size() << endl;

    for (int x = 0; x < n; x++) {
        left = encryptedText.substr(0, encryptedText.length()/2);
        right = encryptedText.substr(encryptedText.length()/2);
        cout << left.length()  << " : left : " << left << endl;
        cout << right.length()  << " : right : " << right << endl;
        for (int i = 0; i < left.size(); i++) {
            out += right[i];
            out += left[i];
            cout << right[i] << " : " << left[i] << endl;
        }
        right.size() > left.size() ? out += right.back() : right ;
        cout << "Out: \"" << out << "\"\n" << endl;
        encryptedText = out;
        out.clear();
    }

    return encryptedText;
}

int main() {
    string t = "hsi  etTi sats!";
    //string t = "This is a test!";
    int n = 1;
    //int n = 3;
    string crypt = decrypt(t, n);
    //string en = encrypt(t, n);

    cout << "Return: \"" << crypt << "\""<< endl;
    return 0;
}
