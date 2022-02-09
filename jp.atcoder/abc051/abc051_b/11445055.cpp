#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int k, s;
  cin >> k >> s;

  int cnt = 0;
  int r;
  for (int i = 0; i <= k; i++) {
    r = s - i;
    if (0 <= r && r <= k) {
      cnt += r + 1;
    } else if (k < r && r <= 2*k) {
      cnt += k - (r - k) + 1;
    }
  }
  cout << cnt << '\n';
  return 0;
}
