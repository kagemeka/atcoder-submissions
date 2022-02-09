#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, d, k;
  cin >> n >> d >> k;
  vector<vector<int>> lr(d);
  for (int i = 0; i < d; i++) {
    int l, r;
    cin >> l >> r;
    lr[i] = {l, r};
  }
  vector<vector<int>> st(k, vector<int>(0));
  for (int i = 0; i < k; i++) {
    int s, t;
    cin >> s >> t;
    st[i] = {s, t};
  }
  vector<int> res(k);

  for (int i = 0; i < d; i++) {
    int l = lr[i][0], r = lr[i][1];
    for (int j = 0; j < k; j++) {
      int s = st[j][0], t = st[j][1];
      if (s == t) continue;
      if (s < l || s > r) continue;
      if (t < l) {
        st[j][0] = l;
      } else if (t > r) {
        st[j][0] = r;
      } else {
        st[j][0] = t;
        res[j] = i + 1;
      }
    }
  }
  for (int i = 0; i < k; i++) {
    cout << res[i] << '\n';
  }
  return 0;
}
