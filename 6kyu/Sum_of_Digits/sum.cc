#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

int sum(int n) {
    int out = 0;
    int temp;

    while(log10(n) >= 1) {
        string str = to_string(n);
        for(unsigned int i = 0; i < str.length(); i++) {
            stringstream chr;
            chr << str[i];
            chr >> temp;
            out += temp;
        }
        n = out;
        out = 0;
    }
    return n;
}

int main() {
    int input = 930208672;
    cout << sum(input) << endl;
    return 0;
}