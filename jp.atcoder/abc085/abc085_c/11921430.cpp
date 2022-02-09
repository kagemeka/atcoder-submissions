#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, y; cin >> n >> y;
  y /= 1000; y -= n;
  for (int i = 0; i <= n; i++) {
    if (9 * i > y) break;
    if ((y - 9 * i) % 4) continue;
    int j = (y - 9 * i) / 4;
    if (i + j > n) continue;
    int k = n - i - j;
    printf("%d %d %d\n", i, j, k);
    return 0;
  }
  cout << "-1 -1 -1" << '\n';
  return 0;
}
