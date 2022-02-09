#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  unordered_set<char> one = {'o', 'k', 'u'};

  string s;
  cin >> s;
  int n;
  while (!s.empty()) {
    n = s.size();
    if (one.find(s[n-1]) != one.end()) {
      s = s.substr(0, n-1);
      continue;
    }
    if (n >= 2 && s.substr(n-2) == "ch") {
      s = s.substr(0, n-2);
      continue;
    }
    cout << "NO" << '\n';
    return 0;
  }
  cout << "YES" << '\n';
  return 0;
}
