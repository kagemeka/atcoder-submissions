#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  int U = 1e5;
  vector<int> cnt(U + 1);
  for (auto &x : a) {
    cnt[x]++;
    if (x > 0) cnt[x-1]++;
    if (x < U) cnt[x+1]++;
  }
  int res = 0;
  for (int i = 0; i < U + 1; i++) res = max(res, cnt[i]);
  cout << res << '\n';
  return 0;
}
