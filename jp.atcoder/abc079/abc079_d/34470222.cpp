#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  vector<vector<int>> g(10, vector<int>(10));
  for(int i = 0; i < 10; i++) {
    for(int j = 0; j < 10; j++) { cin >> g[i][j]; }
  }
  for(int k = 0; k < 10; k++) {
    for(int i = 0; i < 10; i++) {
      for(int j = 0; j < 10; j++) { g[i][j] = min(g[i][j], g[i][k] + g[k][j]); }
    }
  }
  int s = 0;
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      int x;
      cin >> x;
      if(x == -1) continue;
      s += g[x][1];
    }
  }
  cout << s << endl;
}
