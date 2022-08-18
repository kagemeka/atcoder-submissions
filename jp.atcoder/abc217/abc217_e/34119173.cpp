#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int q;
  cin >> q;
  priority_queue<int, vector<int>, greater<>> hq;
  queue<int> que;
  while(q--) {
    int t;
    cin >> t;
    if(t == 1) {
      int x;
      cin >> x;
      que.push(x);
    }
    if(t == 2) {
      int y;
      if(hq.empty()) {
        y = que.front();
        que.pop();
      } else {
        y = hq.top();
        hq.pop();
      }
      cout << y << '\n';
    }
    if(t == 3) {
      while(que.size()) {
        hq.push(que.front());
        que.pop();
      }
    }
  }
}
