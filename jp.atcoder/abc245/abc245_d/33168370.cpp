#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<int> a(n + 1);
  vector<int> c(n + m + 1);
  vector<int> b(m + 1);
  for(int i = 0; i < n + 1; i++) cin >> a[i];
  for(int i = 0; i < n + m + 1; i++) cin >> c[i];
  for(int i = m; i >= 0; i--) {
    int k = c[i + n] / a[n];
    b[i] = k;
    for(int j = 0; j < n + 1; j++) { c[i + j] -= k * a[j]; }
  }
  for(int i = 0; i < m + 1; i++) { cout << b[i] << " \n"[i == m]; }
}
