#include <bits/stdc++.h>
using namespace std;

unordered_set<char> vowel = {'a', 'e', 'i', 'o', 'u'};

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string w;
  cin >> w;
  string res = "";

  for (char &c: w) {
    if (vowel.find(c) != vowel.end()) {
      continue;
    }
    res += c;
  }
  cout << res << endl;
  return 0;
}
