#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k, m;
  cin >> n >> k >> m;
  int s = 0;
  for (int i = 0; i < n - 1; i++) {
    int a;
    cin >> a;
    s += a;
  }
  int res = max(m*n - s, 0);
  if (res > k) res = -1;
  cout << res << '\n';
  return 0;
}
