#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w;
  cin >> h >> w;
  vector<string> s(h);
  for (int i = 0; i < h; i++) cin >> s[i];
  int inf = 1 << 30;
  auto rotate = [](vector<vector<int>> a) {
    int h = a.size();
    int w = a[0].size();
    vector<vector<int>> b(w, vector<int>(h));
    for(int i = 0; i < h; i++)
      for(int j = 0; j < w; j++) b[j][i] = a[i][j];
    reverse(b.begin(), b.end());
    return b;
  };
  vector<vector<int>> a(h + 2, vector<int>(w + 2, 0));
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      if(s[i][j] == '.') a[i + 1][j + 1] = inf;
    }
  }
  vector<vector<int>> d(h + 2, vector<int>(w + 2, 0));
  auto f = [&](vector<vector<int>> a) {
    int h = a.size();
    int w = a[0].size();
    for(int i = 0; i < h - 1; i++)
      for(int j = 0; j < w; j++) {
        a[i + 1][j] = min(a[i + 1][j], a[i][j] + 1);
      }
    return a;
  };
  for(int k = 0; k < 4; k++) {
    auto b = a;
    for(int t = 0; t < k; t++) { b = rotate(b); }
    b = f(b);
    for(int t = 0; t < 4 - k; t++) { b = rotate(b); }
    for(int i = 0; i < h + 2; i++)
      for(int j = 0; j < w + 2; j++) d[i][j] += b[i][j];
  }
  int mx = 0;
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      mx = max(mx, d[i + 1][j + 1] - 3);
      // cout << d[i + 1][j + 1] << " \n"[j == w - 1];
    }
  }
  cout << mx << endl;
}
