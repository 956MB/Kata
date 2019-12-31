#include <iostream>
#include <string>
// #include <vector>

using namespace std;

string notepad(string s) {
   string letter;
   string store;
   string out;
   int inc = 1;

   for (int i = 0; i < s.length(); i++) {
      letter = s[i];
      for (int n = 0; n < inc; n++) {
         store += letter;
      }
      if (i <= s.length() - 2) {
         out += store + '-';
      } else {
         out += store;
      }
      inc += 1;
      store = "";
   }

   out[0] = toupper(out[0]);

   for (int i = 1; i < out.length(); i++) {
      if (out[i - 1] == '-') {
         out[i] = toupper(out[i]);
      } else {
         out[i] = tolower(out[i]);
      }
   }

   return out;
}

int main() {
   string input = "cwAt";
   cout << notepad(input) << endl;
   return 0;
}