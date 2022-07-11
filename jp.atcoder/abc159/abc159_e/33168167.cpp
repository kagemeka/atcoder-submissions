#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int h, w, v;
  cin >> h >> w >> v;
  vector<string> a(h);
  for(int i = 0; i < h; i++) cin >> a[i];
  int const inf = 1 << 30;
  int mn = inf;
  for(int s = 0; s < 1 << (h - 1); s++) {
    vector<int> borders = {0};
    int cnt = 0;
    for(int i = 0; i < h - 1; i++) {
      if(~s >> i & 1) continue;
      borders.push_back(i + 1);
      cnt++;
    }
    borders.push_back(h);
    bool inf_flg = false;
    int n = borders.size();
    vector<int> tmp(n - 1, 0);
    for(int j = 0; j < w; j++) {
      vector<int> values(n - 1, 0);
      bool ng = false;
      for(int i = 0; i < n - 1; i++) {
        int lo = borders[i], hi = borders[i + 1];
        for(int k = lo; k < hi; k++) { values[i] += a[k][j] - '0'; }
        inf_flg |= values[i] > v;
        if(tmp[i] + values[i] > v) {
          ng = true;
          // break;
        }
      }
      if(!ng) {
        for(int i = 0; i < n - 1; i++) { tmp[i] += values[i]; }
        continue;
      };
      cnt++;
      swap(tmp, values);
    }
    if(!inf_flg) mn = min(mn, cnt);
  }
  cout << mn << endl;
}
