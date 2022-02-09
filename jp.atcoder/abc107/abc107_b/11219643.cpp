#include <bits/stdc++.h>
using namespace std;

int main() {
  int h, w;
  cin >> h >> w;
  vector<string> grid(h);
  for (int i = 0; i < h; i++) {
    cin >> grid[i];
  }

  vector<string> res(0);
  for (int i = 0; i < h; i++) {
    bool flag = false;
    for (int j = 0; j < w; j++) {
      if (grid[i][j] == '#') {
        flag = true;
        break;
      }
    }
    if (flag) {
      res.push_back(grid[i]);
    }
  }
  h = res.size();

  vector<string> res2(0);
  for (int j = 0; j < w; j++) {
    bool flag = false;
    for (int i = 0; i < h; i++) {
      if (res[i][j] == '#') {
        flag = true;
        break;
      }
    }
    if (flag) {
      string t = "";
      for (int i = 0; i < h; i++) {
        t += res[i][j];
      }
      res2.push_back(t);
    }
  }
  w = res2.size();

  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      cout << res2[j][i];
    }
    cout << endl;
  }
  return 0;
}
