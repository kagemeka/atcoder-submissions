#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<vector<int>> b(n);
  for(int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    b[x - 1].push_back(y);
  }
  priority_queue<int> que;
  int s = 0;
  for(int k = 0; k < n; k++) {
    for(auto& x: b[k]) que.push(x);
    s += que.top();
    que.pop();
    cout << s << '\n';
  }
}
