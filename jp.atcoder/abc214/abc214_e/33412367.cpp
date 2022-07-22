#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int t;
  cin >> t;
  auto f = [&]() -> bool {
    int n;
    cin >> n;
    using p = pair<int, int>;
    vector<p> lr(n);
    for(int i = 0; i < n; i++) cin >> lr[i].first >> lr[i].second;
    sort(lr.begin(), lr.end());
    int x = 0;
    int i = 0;
    priority_queue<int, vector<int>, greater<>> que;
    while(i < n || que.size()) {
      if(!que.size()) x = lr[i].first;
      while(i < n && lr[i].first == x) {
        que.push(lr[i].second);
        i++;
      }
      if(que.top() < x) { return false; }
      que.pop();
      x++;
    }
    return true;
  };
  while(t--) { cout << (f() ? "Yes" : "No") << endl; }
}
