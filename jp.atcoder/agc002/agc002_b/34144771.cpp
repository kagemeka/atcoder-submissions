#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<int> cnt(n, 1);
  vector<int> possible(n, false);
  possible[0] = true;
  for(int i = 0; i < m; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    cnt[v]++;
    cnt[u]--;
    if(!possible[u]) continue;
    possible[v] = true;
    if(cnt[u] == 0) possible[u] = false;
  }
  int s = 0;
  for(int i = 0; i < n; i++) s += possible[i];
  cout << s << endl;
}
