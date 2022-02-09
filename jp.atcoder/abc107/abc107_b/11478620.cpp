#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int h, w;
  cin >> h >> w;
  vector<vector<char>> res(h, vector<char>(w));
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      cin >> res[i][j];
    }
  }
  int k = 0;
  for (int i = 0; i < h; i++) {
    bool flag = false;
    for (int j = 0; j < w; j++) {
      if (res[i][j] == '#') {
        flag = true;
        break;
      }
    }
    if (flag) {
      for (int j = 0; j < w; j++) {
        res[k][j] = res[i][j];
      }
      k++;
    }
  }
  h = k;
  k = 0;
  for (int j = 0; j < w; j++) {
    bool flag = false;
    for (int i = 0; i < h; i++) {
      if (res[i][j] == '#') {
        flag = true;
        break;
      }
    }
    if (flag) {
      for (int i = 0; i < h; i++) {
        res[i][k] = res[i][j];
      }
      k++;
    }
  }
  w = k;
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      cout << res[i][j];
    }
    cout << '\n';
  }
  return 0;
}
