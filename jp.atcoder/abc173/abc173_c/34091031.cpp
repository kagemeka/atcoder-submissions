#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w, k;
  cin >> h >> w >> k;
  vector<string> grid(h);
  for(int i = 0; i < h; i++) cin >> grid[i];
  int cnt = 0;
  auto f = [&](int s, int t) -> bool {
    vector<int> ys, xs;
    for(int i = 0; i < h; i++) {
      if(s >> i & 1) ys.push_back(i);
    }
    for(int j = 0; j < w; j++) {
      if(t >> j & 1) xs.push_back(j);
    }
    int cnt = 0;
    for(auto& y: ys) {
      for(auto& x: xs) { cnt += grid[y][x] == '#'; }
    }
    return cnt == k;
  };
  for(int s = 0; s < 1 << h; s++) {
    for(int t = 0; t < 1 << w; t++) { cnt += f(s, t); }
  }
  cout << cnt << endl;
}
