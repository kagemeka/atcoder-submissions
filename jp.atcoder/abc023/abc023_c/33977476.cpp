#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int h, w, k;
  cin >> h >> w >> k;
  int n;
  cin >> n;
  using pi = pair<int, int>;
  vector<pi> yx(n);
  vector<int> cy(h), cx(w);
  for(int i = 0; i < n; i++) {
    int y, x;
    cin >> y >> x;
    y--;
    x--;
    yx[i] = {y, x};
    cy[y]++;
    cx[x]++;
  }
  vector<int> ccy(max(w, k) + 1), ccx(max(h, k) + 1);
  for(int i = 0; i < h; i++) { ccy[cy[i]]++; }
  for(int i = 0; i < w; i++) { ccx[cx[i]]++; }
  long s = 0;
  for(int i = 0; i <= k; i++) { s += (long)ccy[i] * ccx[k - i]; }
  for(auto& [y, x]: yx) {
    int c = cy[y] + cx[x];
    if(c == k) { s--; }
    if(c == k + 1) { s++; }
  }
  cout << s << endl;
}
