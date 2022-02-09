#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, y; cin >> n >> y;
  y /= 1000;
  for (int i = 0; i <= n; i++) {
    if (10 * i > y) break;
    for (int j = 0; j <= n - i; j++) {
      int k = n - i - j;
      if (10 * i + 5 * j + k == y) {
        printf("%d %d %d\n", i, j, k);
        return 0;
      }
    }
  }
  cout << "-1 -1 -1" << '\n';
  return 0;
}
