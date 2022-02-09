#include <bits/stdc++.h>
using namespace std;


int main() {
  int n, m;
  cin >> n >> m;
  vector<set<int>> g(n);
  for (int i = 0; i < m; i++) {
    int x, y;
    cin >> x >> y;
    x--; y--;
    g[x].insert(y);
    g[y].insert(x);
  }

  int res = 1;
  for (int i = 0; i < (1 << n); i++) {
    vector<int> group(0);
    for (int j = 0; j < n; j++) {
      if (i >> j & 1) group.push_back(j);
    }
    int k = group.size();
    bool flag = false;
    for (int a = 0; a < k - 1; a++) {
      for (int b = a + 1; b < k; b++) {
        int &x = group[a];
        int &y = group[b];
        if (g[x].find(y) != g[x].end()) continue;
        flag = true;
        break;
      }
      if (flag) break;
    }
    if (!flag) res = max(res, k);
  }
  cout << res << endl;
  return 0;
}
