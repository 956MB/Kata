#include <iostream>
#include <vector>

using namespace std;

void printMatrix(vector<vector<int>> const &v) {
    for(int x = 0; x < v.size() ; x++) {
        for(int y = 0; y < x + 1; y++) {
            cout << v[x][y];
        }
        cout << endl;
    }
}

vector<vector<int>> two(int n) {
    vector<vector<int>> output;
    for (int i = 0; i < n; i++) {
        vector<int> vect;
        for (int x = 0; x < i + 1; x++) {
            vect.push_back(1);
        }
        output.push_back(vect);
    }
    cout << output.size() << endl;
    return output;
}

int main() {
    int target = 4;
    vector<vector<int>> t = two(target);
    printMatrix(t);
    return 0;
}