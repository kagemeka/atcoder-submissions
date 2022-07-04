#include <bits/stdc++.h>

using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];

  int s = 1000;
  for (int i = 0; i < n - 1; i++) {
    if (a[i + 1] > a[i]) {
      s += s / a[i] * (a[i + 1] - a[i]);
    }
  }
  cout << s << endl;
}
