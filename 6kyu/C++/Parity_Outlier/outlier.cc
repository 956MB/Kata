#include <iostream>
#include <vector>

using namespace std;

int find(const vector<int> arr) {
    int odd = 0;
    int even = 0;

    for(int i = 0; i < arr.size(); i++) {
        if (even == 2) {
            break;
        } else if (odd == 2) {
            break;
        }

        if (arr[i] % 2 == 0) {
            even++;
        } else {
            odd++;
        }
    }

    if (odd > even) {
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] % 2 == 0) {
                return arr[i];
            }
        }
    } else {
        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] % 2 != 0) {
                return arr[i];
            }
        }
    }
}

int main() {
    vector<int> numbers {2, 3, 4};
    cout << find(numbers) << endl;
    return 0;
}