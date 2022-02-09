#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, k; cin >> n >> k;
  vector<int> x(n);
  for (int i = 0; i < n; i++) cin >> x[i];
  int res = 1001001001;
  for (int i = 0; i < n - k + 1; i++) {
    int j = i + k - 1;
    int d;
    if (x[i] < 0) {
      d = (x[j] <= 0) ? -x[i] : min(-x[i], x[j]) * 2 + max(-x[i], x[j]);
    } else {
      d = x[j];
    }
    res = min(res, d);
  }
  cout << res << '\n';
  return 0;
}
