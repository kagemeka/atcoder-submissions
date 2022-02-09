#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> x(n);
  vector<int> y(n);
  vector<int> h(n);
  for (int i = 0; i < n; i++) cin >> x[i] >> y[i] >> h[i];

  int x0, y0, h0;
  for (int i = 0; i < n; i++) {
    if (h[i]) {
      x0 = x[i];
      y0 = y[i];
      h0 = h[i];
      break;
    }
  }
  vector<vector<int>> cand;
  for (int cx = 0; cx < 101; cx++) {
    for (int cy = 0; cy < 101; cy++) {
      int ch = h0 + abs(cx - x0) + abs(cy - y0);
      bool flag = true;
      for (int i = 0; i < n; i++) {
        if (max(ch - abs(x[i] - cx) - abs(y[i] - cy), 0) != h[i]) {
          flag = false;
          break;
        }
      }
      if (flag) {
        cand.push_back({ch, cx, cy});
      }
    }
  }
  sort(cand.begin(), cand.end(), greater<vector<int>>());
  printf("%d %d %d\n", cand[0][1], cand[0][2], cand[0][0]);
  return 0;
}
