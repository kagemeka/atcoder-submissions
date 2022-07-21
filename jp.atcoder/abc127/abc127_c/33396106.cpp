#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<int> a(n + 1);
  for(int i = 0; i < m; i++) {
    int l, r;
    cin >> l >> r;
    l--;
    r--;
    a[l]++;
    a[r + 1]--;
  }
  int cnt = 0;
  for(int i = 0; i < n; i++) {
    a[i + 1] += a[i];
    cnt += (a[i] == m);
  }
  cout << cnt << endl;
}
