#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, k;
  cin >> n >> k;
  int mx = (n - 1) * (n - 2) / 2;
  if(k > mx) {
    cout << -1 << endl;
    return 0;
  }
  k = mx - k;

  int m = n - 1 + k;

  cout << m << endl;
  for(int i = 0; i < n - 1; i++) { cout << i + 1 << ' ' << n << endl; }

  for(int i = 0;; i++) {
    for(int j = 0; j < i && k > 0; j++, k--) {
      cout << i + 1 << ' ' << j + 1 << endl;
    }
    if(k == 0) break;
  }
}
