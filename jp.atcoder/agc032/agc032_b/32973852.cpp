#include <bits/stdc++.h>

using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;

  cout << n * (n - 1) / 2 - n / 2 << endl;
  int m = 1 + n / 2 * 2;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
      if (i + j == m - 2) continue;
      cout << i + 1 << ' ' << j + 1 << endl;
    }
  }
}
