#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  reverse(s.begin(), s.end());
  int n = s.size();
  vector<int> r(n + 1);
  int const m = 2019;
  int p = 1;
  for(int i = 0; i < n; i++) {
    int d = s[i] - '0';
    r[i + 1] = (r[i] + d * p) % m;
    p = p * 10 % m;
  }
  vector<int> cnt(m);
  long tot = 0;
  for(int i = 0; i <= n; i++) {
    int x = r[i];
    tot += cnt[x]++;
  }
  cout << tot << endl;
}
