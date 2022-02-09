#include <bits/stdc++.h>
using namespace std;

int main() {
  char c; cin >> c;
  string vowel = "aeiou";
  string ans = "consonant";
  for (int i = 0; i < 5; i++) {
    if (vowel.at(i) == c) {
      ans = "vowel";
    }
  }
  cout << ans << endl;
}
