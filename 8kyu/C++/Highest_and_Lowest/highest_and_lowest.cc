#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

string notepad(string numbers) {
   int temp;
   string output = "";
   stringstream iss(numbers);
   vector<int> arr;

   while ( iss >> temp ) {
      arr.push_back(temp);
   }

   sort(arr.begin(), arr.end());
   
   output = to_string(arr.back()) + ' ' + to_string(arr.front());
   return output;
}

int main() {
   string numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4";
   cout << notepad(numbers) << endl;
   return 0;
}