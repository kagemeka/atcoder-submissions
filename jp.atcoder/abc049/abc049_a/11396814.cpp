#include <bits/stdc++.h>
using namespace std;

set<char> vowel = {'a', 'e', 'i', 'o', 'u'};

int main() {
  char c;
  cin >> c;
  string ans = (vowel.find(c) != vowel.end()) ? "vowel" : "consonant";
  cout << ans << endl;
  return 0;
}
