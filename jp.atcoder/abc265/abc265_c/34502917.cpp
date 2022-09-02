#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  vector<string> g(h);
  for(int i = 0; i < h; i++) cin >> g[i];
  int y = 0, x = 0;
  vector<vector<bool>> visited(h, vector<bool>(w));
  visited[0][0] = true;
  auto on_grid = [&](int i, int j) -> bool {
    return 0 <= i && i < h && 0 <= j && j < w;
  };
  while(true) {
    char c = g[y][x];
    int i = y, j = x;
    if(c == 'U') i--;
    if(c == 'D') i++;
    if(c == 'L') j--;
    if(c == 'R') j++;
    if(!on_grid(i, j)) {
      cout << y + 1 << ' ' << x + 1 << endl;
      return 0;
    }
    if(visited[i][j]) {
      cout << -1 << endl;
      return 0;
    }
    y = i, x = j;
    visited[y][x] = true;
  }
}
