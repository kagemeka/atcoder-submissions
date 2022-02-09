#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, s, t, w;
  cin >> n >> s >> t >> w;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  int cnt = (s <= w && w <= t) ? 1 : 0;
  for (auto &dw : a) {
    w += dw;
    if (s <= w && w <= t) cnt++;
  }
  cout << cnt << endl;
  return 0;
}
