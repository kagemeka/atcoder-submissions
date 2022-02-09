#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, s, t;
  cin >> n >> s >> t;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  int w = 0;
  int cnt = 0;
  for (auto &dw : a) {
    w += dw;
    if (s <= w && w <= t) cnt++;
  }
  cout << cnt << endl;
  return 0;
}
