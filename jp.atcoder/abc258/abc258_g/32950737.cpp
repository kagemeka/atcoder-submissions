#include <bits/stdc++.h>

auto main() -> int {
  using namespace std;
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  constexpr int K = 3000;
  vector<bitset<K>> a(K);

  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      char e;
      cin >> e;
      if (e == '1') a[i].set(j);
    }
  }

  long res = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
      if (!a[i].test(j)) continue;
      res += (a[i] & a[j]).count();
    }
  }
  cout << res / 3 << endl;
}
