#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, w;
  cin >> n >> w;

  const int k = 1 << 18;

  vector<long> a(k);
  for (int i = 0; i < n; i++) {
    int s, t, p;
    cin >> s >> t >> p;
    a[s] += p;
    a[t] -= p;
  }
  for (int i = 0; i < k - 1; i++) {
    a[i + 1] += a[i];
  }
  for (int i = 0; i < k; i++) {
    if (a[i] > w) {
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
}
