#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, k; cin >> n >> k;
  vector<int> h(n);
  for (int i = 0; i < n; i++) cin >> h[i];
  sort(h.begin(), h.end());
  int res = 1001001001;
  for (int i = 0; i < n - k + 1; i++) {
    res = min(res, h[i+k-1] - h[i]);
  }
  cout << res << '\n';
  return 0;
}
