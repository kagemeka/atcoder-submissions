#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, d;
  cin >> n >> m >> d;
  vector<int> a(n);
  iota(a.begin(), a.end(), 0);
  vector<int> b(m);
  for(int i = 0; i < m; i++) cin >> b[i];
  reverse(b.begin(), b.end());
  for(auto& i: b) {
    i--;
    swap(a[i], a[i + 1]);
  }
  vector<vector<int>> cycles;
  vector<int> idx_in_cycle(n), cycle_id(n, -1);
  for(int i: a) {
    if(cycle_id[i] != -1) continue;
    int id = cycles.size();
    vector<int> cycle;
    for(int j = 0; j < n; j++) {
      if(cycle_id[i] != -1) break;
      cycle_id[i] = id;
      cycle.push_back(i);
      idx_in_cycle[i] = j;
      i = a[i];
    }
    cycles.push_back(cycle);
  }
  auto get_kth = [&](int i, long k) -> int {
    auto& cycle = cycles[cycle_id[i]];
    int l = cycle.size();
    k = (idx_in_cycle[i] + k) % l;
    return cycle[k];
  };
  for(int i = 0; i < n; i++) { cout << get_kth(i, d) + 1 << endl; }
}
