#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> preorder(n), inorder(n);
  for(int i = 0; i < n; i++) cin >> preorder[i];
  for(int i = 0; i < n; i++) cin >> inorder[i];
  vector<int> inrank(n);
  for(int i = 0; i < n; i++) {
    preorder[i]--;
    inrank[--inorder[i]] = i;
  }
  if(preorder[0] != 0) {
    cout << -1 << endl;
    return 0;
  }
  vector<int> l_child(n, -1), r_child(n, -1);
  function<bool(int, int, int)> dfs;
  dfs = [&](int l, int r, int i) -> bool {
    int u = preorder[i];
    int j = inrank[u];
    if(!(l <= j && j < r)) return false;
    if(j > l) {
      if(!dfs(l, j, i + 1)) return false;
      l_child[u] = preorder[i + 1];
    }
    if(j + 1 < r) {
      if(!dfs(j + 1, r, i + 1 + j - l)) return false;
      r_child[u] = preorder[i + 1 + j - l];
    }
    return true;
  };
  if(!dfs(0, n, 0)) {
    cout << -1 << endl;
    return 0;
  }
  for(int i = 0; i < n; i++) {
    cout << l_child[i] + 1 << ' ' << r_child[i] + 1 << endl;
  }
}
