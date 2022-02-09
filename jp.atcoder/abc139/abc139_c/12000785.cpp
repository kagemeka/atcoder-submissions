#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> h(n + 1); h[n] = 1001001001;
  for (int i = 0; i < n; i++) cin >> h[i];
  int prev = 0;
  int res = 0;
  int cnt = 0;
  for (int i = 0; i < n + 1; i++) {
    if (h[i] > prev) {
      res = max(res, cnt);
      cnt = 0;
    } else {
      cnt++;
    }
    prev = h[i];
  }
  cout << res << '\n';
  return 0;
}
