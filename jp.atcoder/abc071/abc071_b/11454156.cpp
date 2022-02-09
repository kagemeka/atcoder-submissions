#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  unordered_set<char> used;
  for (char &c : s) used.insert(c);

  for (int i = 0; i < 26; i++) {
    char c = i + 97;
    if (used.find(c) == used.end()) {
      cout << c << '\n';
      return 0;
    }
  }
  cout << "None" << '\n';
  return 0;
}
