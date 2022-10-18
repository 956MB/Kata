#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int slice(vector<int> const &n, int l, int r, int last) {
    auto left_first = n.cbegin(), left_last = n.cbegin() + r;
    auto right_first = n.cbegin() + r + 1, right_last = n.cbegin() + last;

    vector<int> lvec(left_first, left_last);
    vector<int> rvec(right_first, right_last);
    
    int lvec_sum = accumulate(lvec.begin(), lvec.end(), 0);
    int rvec_sum = accumulate(rvec.begin(), rvec.end(), 0);
    
    if (lvec_sum == rvec_sum) {
        return r;
    }
    return -1;
}

int walk(const vector<int> numbers) {
    int l, r = 0, last = numbers.size();
    for (int i = 0; i < numbers.size(); i++) {
        int compare = slice(numbers, l, r, last);
        if (compare == -1) {
            r += 1;
        } else {
            return compare;
        }
    }
    return -1;
}

int main() {
    vector<int> numbers { 10,-80,10,10,15,35,20 };
    cout << walk(numbers) << endl;
    return 0;
}