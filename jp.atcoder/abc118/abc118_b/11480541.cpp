#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;
  int res = (1 << m) - 1;
  for (int i = 0; i < n; i++) {
    int k;
    cin >> k;
    int tmp = 0;
    for (int j = 0; j < k; j++) {
      int a;
      cin >> a;
      tmp |= 1 << (a - 1);
    }
    res &= tmp;
  }
  int cnt = 0;
  for (int i = 0; i < m; i++) {
    cnt += res >> i & 1;
  }
  cout << cnt << '\n';
  return 0;
}
