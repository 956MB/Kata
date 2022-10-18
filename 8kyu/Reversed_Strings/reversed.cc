# include <string>
# include <iostream>

using namespace std;

string reverseString(string str) {
	for (int i=0; i<str.length() / 2; i++) {
		swap(str[i], str[str.length() - i - 1]);
	}
	return str;
}

int main() {
	string str = "hello";
	cout << reverseString(str) << endl;
	return 0;
}
