// Two Sum
// https://www.codewars.com/kata/52c31f8e6605bcc646000082/cpp

#include <iostream>
#include <vector>

using namespace std;

string print(vector<int> const &v) {
    cout << "{";
    for (auto i: v) {
        cout << i << ", ";
    }
    cout << "}";
    return "\n";
}

pair<size_t, size_t> two(const vector<int> &numbers, int target) {
    cout << "Arr: "<< print(numbers);
    cout << "Target: " << target << "\n\n";
    for (int x = 0; x < numbers.size() - 1; x++) {
        for (int y = x + 1; y < numbers.size(); y++) {
            if (numbers[x] + numbers[y] == target) {
                cout << "Found: (" << numbers[x] << ", " << numbers[y] << ")" << endl;
                return make_pair(x, y);
            }
        }
    }
    cout << "No \"Two Sum\" found:" << endl;
    return make_pair(0, 0);
}

int main() {
    vector<int> numbers {2, 2, 3};
    int target = 4;
    pair<int, int> t = two(numbers, target);

    cout << "Indexes: (" << t.first << ", " << t.second << ")" << endl;
    return 0;
}
