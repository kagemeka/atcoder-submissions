#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  string s;
  string t;
  cin >> s >> t;
  int n = s.size();

  vector<int> next_tmp(26, -1);
  for(int i = n - 1; i > -1; i--) { next_tmp[s[i] - 'a'] = i; }
  vector<vector<int>> next(n, vector<int>(26));
  for(int i = n - 1; i > -1; i--) {
    next[i] = next_tmp;
    next_tmp[s[i] - 'a'] = i;
  }

  long i = -1;
  for(auto& c: t) {
    int j = (i + n) % n;
    int ni = next[j][c - 'a'];
    if(ni == -1) {
      cout << -1 << endl;
      return 0;
    }
    i += (ni - j) + n * (ni <= j);
  }
  cout << i + 1 << endl;
}