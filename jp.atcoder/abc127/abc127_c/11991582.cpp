#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m; cin >> n >> m;
  int l0 = 1, r0 = n;
  for (int i = 0; i < m; i++) {
    int l, r;
    cin >> l >> r;
    l0 = max(l, l0);
    r0 = min(r0, r);
  }
  cout << max(0, r0 - l0 + 1) << '\n';
  return 0;
}
