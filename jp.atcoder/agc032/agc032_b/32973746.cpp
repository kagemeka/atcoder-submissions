#include <bits/stdc++.h>

using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;

  assert(n & 1);

  cout << n * (n - 1) / 2 - n / 2 << endl;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
      if (i + j == n - 2) continue;
      cout << i + 1 << ' ' << j + 1 << endl;
    }
  }
}
