#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  function<void(vector<int>&)> dfs;
  dfs = [&](vector<int>& a) {
    int l = a.size();
    if(l == n) {
      for(int i = 0; i < n; i++) { cout << a[i] << " \n"[i == n - 1]; }
      return;
    }
    int x = l == 0 ? 0 : a[l - 1];
    for(int y = x + 1; y <= m; y++) {
      a.push_back(y);
      dfs(a);
      a.pop_back();
    }
  };
  vector<int> a{};
  dfs(a);
}
