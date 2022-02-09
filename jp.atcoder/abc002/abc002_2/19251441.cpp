#include <bits/stdc++.h>
using namespace std;


string remove_chars(
  const string& s,
  const set<char>& chars
) {
  string t = "";
  for (const char& c : s) {
    if (chars.count(c)) {
      continue;
    }
    t += c;
  }
  return t;
}


void solve() {
  string w;
  cin >> w;
  set<char> vowels = {
    'a', 'e', 'i', 'o', 'u'};
  w = remove_chars(w, vowels);
  cout << w << '\n';
}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t = 1;
  while (t--) {
    solve();
  }

  return 0;
}
