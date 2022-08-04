#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  vector<int> t(n + 1), y(n + 1);
  t[0] = 1;
  for(int i = 0; i < n; i++) cin >> t[i + 1] >> y[i + 1];
  long const inf = 1l << 60;
  long mx = -inf;
  long s = 0;
  priority_queue<int> que;
  for(int i = n; i >= 0; i--) {
    while(k < 0 && que.size()) {
      int v = que.top();
      s += v;
      k++;
      que.pop();
    }
    if(k < 0) break;
    if(t[i] == 1) {
      mx = max(mx, y[i] + s);
      k--;
    } else {
      if(y[i] < 0) {
        k--;
        que.emplace(y[i]);
      } else {
        s += y[i];
      }
    }
  }
  cout << mx << endl;
}
