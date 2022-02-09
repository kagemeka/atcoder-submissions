#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, x;
  cin >> n >> x;
  int a;
  int res = 0;
  for (int i = 0; i < n; i++) {
    cin >> a;
    if (x >> i & 1) res += a;
  }
  cout << res << '\n';
  return 0;
}
