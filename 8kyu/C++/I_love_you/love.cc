#include <iostream>
using namespace std;

string nb_petals(int n) {
	string sayings[6] = {"I love you", "a little", "a lot", "pasionately", "madly", "not at all"};
	while (n > 6) {
		n -= 6;
	}
	return sayings[n-1];
}

int main() {
	int petals = 8;
	cout << nb_petals(petals) << endl;
	return 0;
}
