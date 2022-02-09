#include <bits/stdc++.h>
using namespace std;

int main() {
  string vowel = "aeiou";
  char c;
  cin >> c;
  for (int i = 0; i < 5; i++) {
    if (c == vowel.at(i)) {
      cout << "vowel" << endl;
      return 0;
    }
  }
  cout << "consonant" << endl;
  return 0;
}
