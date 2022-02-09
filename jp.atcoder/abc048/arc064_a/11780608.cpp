#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, x;
  cin >> n >> x;
  int a;
  long long cnt = 0;
  int lim = x;
  for (int i = 0; i < n; i++) {
    cin >> a;
    if (a > lim) {
      cnt += a - lim;
      lim = x - lim;
    } else {
      lim = x - a;
    }
  }
  cout << cnt << '\n';
  return 0;
}
