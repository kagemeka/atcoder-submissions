#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, t, a, h;
  cin >> n >> t >> a;
  t *= 1000;
  a *= 1000;
  int tmp;
  int d = 1001001;
  int j;
  for (int i = 0; i < n; i++) {
    cin >> h;
    tmp = t - h * 6;
    int diff = abs(a - tmp);
    if (diff < d) {
      j = i + 1;
      d = diff;
    }
  }
  cout << j << '\n';
  return 0;
}
