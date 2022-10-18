#include <iostream>
#include <string>
// #include <vector>

using namespace std;

bool notepad(string str) {
   int x = 0;
   int o = 0;

   for (int i = 0; i < str.length(); i++) {
      if (tolower(str[i]) == 'x') {
         x += 1;
      } else if (tolower(str[i]) == 'o') {
         o += 1;
      }
   }

   return x == o;
}

int main() {
   string input = "ooxXm";
   cout << notepad(input) << endl;
   return 0;
}