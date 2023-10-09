#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  vector<int> h(n);
  for(int i = 0; i < n; i++) cin >> h[i];

  vector<int> l(n), r(n);
  for(int i = 1; i < n; i++) {
    l[i] = (h[i - 1] < h[i]) * (l[i - 1] + 1);
    r[n - i - 1] = (h[n - i - 1] > h[n - i]) * (r[n - i] + 1);
  }

  int mx = 0;
  for(int i = 0; i < n; i++) mx = max(mx, l[i] + r[i] + 1);
  cout << mx << endl;
}
