#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  int n2 = 1 << n;
  vector<int> a(n2);
  for(int i = 0; i < n2; i++) cin >> a[i];
  vector<int> que(n2);
  iota(que.begin(), que.end(), 0);
  for(int i = 0; i < (int)que.size() - 1; i += 2) {
    int x = que[i], y = que[i + 1];
    que.push_back(a[x] > a[y] ? x : y);
  }
  cout << que[que.size() - 3] + 1 << endl;
}
