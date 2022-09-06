#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int h, w, n;
  cin >> h >> w >> n;
  map<pair<int, int>, int> cnt;
  for(int i = 0; i < n; i++) {
    int y, x;
    cin >> y >> x;
    for(int dy = -1; dy < 2; dy++) {
      for(int dx = -1; dx < 2; dx++) {
        int ny = y + dy;
        int nx = x + dx;
        if(!(1 < ny && ny < h && 1 < nx && nx < w)) continue;
        cnt[{ny, nx}]++;
      }
    }
  }
  vector<long> res(10);
  res[0] = (long)(h - 2) * (w - 2);
  for(auto& [_, x]: cnt) res[x]++;
  for(int i = 1; i < 10; i++) res[0] -= res[i];
  for(auto& c: res) cout << c << endl;
}
