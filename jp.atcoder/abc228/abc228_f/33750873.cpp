#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int h, w, dy0, dx0, dy1, dx1;
  cin >> h >> w >> dy0 >> dx0 >> dy1 >> dx1;
  vector<vector<int>> a(h, vector<int>(w));
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) { cin >> a[i][j]; }
  }
  vector<vector<long>> s(h + 1, vector<long>(w + 1));
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) { s[i + 1][j + 1] = a[i][j]; }
  }
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w + 1; j++) { s[i + 1][j] += s[i][j]; }
  }
  for(int j = 0; j < w; j++) {
    for(int i = 0; i < h + 1; i++) { s[i][j + 1] += s[i][j]; }
  }
  dy1 = min(dy1, dy0);
  dx1 = min(dx1, dx0);
  vector<vector<long>> sa(h, vector<long>(w)), sb(h, vector<long>(w));
  for(int i = 0; i < h - dy0 + 1; i++) {
    for(int j = 0; j < w - dx0 + 1; j++) {
      sa[i][j] = s[i + dy0][j + dx0] - s[i + dy0][j] - s[i][j + dx0] + s[i][j];
    }
  }
  for(int i = 0; i < h - dy1 + 1; i++) {
    for(int j = 0; j < w - dx1 + 1; j++) {
      sb[i][j] = s[i + dy1][j + dx1] - s[i + dy1][j] - s[i][j + dx1] + s[i][j];
    }
  }
  int yk = dy0 - dy1 + 1;
  int xk = dx0 - dx1 + 1;
  vector<vector<long>> mx(h, vector<long>(w));
  for(int i = 0; i < h; i++) {
    deque<long> que;
    for(int j = 0; j < w; j++) {
      if(que.size() && que.front() + xk == j) que.pop_front();
      while(que.size() && sb[i][que.back()] <= sb[i][j]) que.pop_back();
      que.push_back(j);
      long x = sb[i][que.front()];
      if(j >= xk - 1) { mx[i][j + 1 - xk] = x; }
    }
  }
  for(int j = 0; j < w; j++) {
    deque<long> que;
    for(int i = 0; i < h; i++) {
      if(que.size() && que.front() + yk == i) que.pop_front();
      while(que.size() && mx[que.back()][j] <= mx[i][j]) que.pop_back();
      que.push_back(i);
      long x = mx[que.front()][j];
      if(i >= yk - 1) { mx[i + 1 - yk][j] = x; }
    }
  }
  long res = 0;
  for(int i = 0; i < h - dy0 + 1; i++) {
    for(int j = 0; j < w - dx0 + 1; j++) {
      res = max(res, sa[i][j] - mx[i][j]);
    }
  }
  cout << res << endl;
}
