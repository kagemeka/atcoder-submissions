#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, k;
  cin >> n >> k;
  int r = k;
  vector<queue<int>> que(k);
  vector<bool> ok(1 << 20);
  for(int i = 0; i < n; i++) {
    for(int j = 0; j < k; j++) {
      int x;
      cin >> x;
      que[j].push(x);
    }
    vector<int> res;
    for(int j = 0; j < k; j++) {
      while(que[j].size() && r - (n - 1 - i) * j > 0) {
        int x = que[j].front();
        que[j].pop();
        if(!ok[x]) {
          r--;
          res.push_back(x);
        }
        ok[x] = true;
      }
    }
    int m = res.size();
    for(int j = 0; j < m; j++) { cout << res[j] << " "; }
    cout << endl;
  }
}
