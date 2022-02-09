#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  unordered_set<char> cand = {'A', 'C', 'G', 'T'};
  string s;
  cin >> s;
  s += '$';
  int n = s.size();
  int cnt = 0;
  int res = 0;
  for (int i = 0; i < n; i++) {
    if (cand.find(s[i]) != cand.end()) cnt++;
    else {res = max(res, cnt); cnt = 0;}
  }
  cout << res << '\n';
  return 0;
}
