#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  vector<string> g(h);
  for(int i = 0; i < h; i++) cin >> g[i];
  auto on_grid = [&](int i, int j) -> bool {
    return 0 <= i && i < h && 0 <= j && j < w;
  };
  vector<vector<bool>> visited(h, vector<bool>(w));
  visited[0][0] = true;
  int i = 0, j = 0;
  while(true) {
    int ny, nx;
    if(g[i][j] == 'U') {
      ny = i - 1, nx = j;
    } else if(g[i][j] == 'D') {
      ny = i + 1, nx = j;
    } else if(g[i][j] == 'L') {
      ny = i, nx = j - 1;
    } else {
      ny = i, nx = j + 1;
    }
    if(!on_grid(ny, nx)) break;
    if(visited[ny][nx]) {
      cout << -1 << endl;
      return 0;
    }
    i = ny, j = nx;
  }
  cout << i + 1 << ' ' << j + 1 << endl;
}
