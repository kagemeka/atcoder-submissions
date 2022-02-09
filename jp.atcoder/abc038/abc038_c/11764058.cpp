#include <bits/stdc++.h>
using namespace std;

map<vector<int>, long long> comb;
long long choose(int n, int r) {
  if (r > n || r < 0) return 0;
  if (r == 0) return 1;
  if (comb.find({n, r}) != comb.end()) return comb[{n, r}];
  comb[{n, r}] = choose(n - 1, r) + choose(n - 1, r - 1);
  return comb[{n, r}];
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<int> a(n + 1);
  for (int i = 0; i < n; i++) cin >> a[i];
  a[n] = 0;

  long long res = 0;
  int cnt = 0;
  int prev = 1001001001;
  for (int &x : a) {
    if (x <= prev) {
      res += choose(cnt, 2) + cnt;
      cnt = 1;
    } else {
      cnt++;
    }
    prev = x;
  }
  cout << res << '\n';
  return 0;
}
