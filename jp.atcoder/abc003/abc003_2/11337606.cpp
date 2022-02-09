#include <bits/stdc++.h>
using namespace std;

set<char> atcoder = {'a', 't', 'c', 'o', 'd', 'e', 'r'};

int main() {
  string s, t;
  cin >> s >> t;

  int n = s.size();
  string ans = "You can win";
  for (int i = 0; i < n; i++) {
    char c = s[i];
    char d = t[i];
    if (c == d) continue;
    if (c == '@' && atcoder.find(d) != atcoder.end()) continue;
    if (d == '@' && atcoder.find(c) != atcoder.end()) continue;
    ans = "You will lose";
    break;
  }
  cout << ans << endl;
  return 0;
}
