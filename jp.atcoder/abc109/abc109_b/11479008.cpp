#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string ans = "Yes";
  int n;
  cin >> n;
  unordered_set<string> used;
  string s;
  cin >> s;
  used.insert(s);
  string t = s;
  for (int i = 1; i < n; i++) {
    cin >> s;
    if (s[0] != t[t.size()-1] || used.find(s) != used.end()) {
      ans = "No";
    }
    used.insert(s);
    t = s;
  }
  cout << ans << '\n';
  return 0;
}
