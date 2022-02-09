#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  string s, t;
  cin >> s >> t;
  int n = s.size();
  vector<bitset<26>> g1(26);
  vector<bitset<26>> g2(26);
  for (int i = 0; i < n; i++) {
    int a, b;
    a = s[i] - 'a';
    b = t[i] - 'a';
    g1[a].set(b);
    g2[b].set(a);
  }
  string ans = "Yes";
  for (int i = 0; i < 26; i++) {
    if (g1[i].count() >= 2 || g2[i].count() >= 2) {
      ans = "No";
      break;
    }
  }
  cout << ans << '\n';
  return 0;
}
