#include <bits/stdc++.h>
using namespace std;

set<char> vowel = {'a', 'e', 'i', 'o', 'u'};

int main() {
  string w;
  cin >> w;
  string res = "";

  for (char c: w) {
    if (vowel.find(c) != vowel.end()) {
      continue;
    }
    res += c;
  }
  cout << res << endl;
  return 0;
}
