#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> cap(n), weight(n), p(n);
  for(int i = 0; i < n; i++) cin >> cap[i];
  for(int i = 0; i < n; i++) cin >> weight[i];
  for(int i = 0; i < n; i++) cin >> p[i];
  // in order of cap
  // p[i] != i & weight[p[i]] >= cap[i] -> impossible
  // weight[p[i]] < cap[i] & weight[i] < cap[arg[i]] -> possible
  vector<int> arg(n);
  for(int i = 0; i < n; i++) {
    p[i]--;
    arg[p[i]] = i;
  }
  vector<int> order(n);
  iota(order.begin(), order.end(), 0);
  sort(order.begin(), order.end(), [&](int i, int j) {
    return cap[i] < cap[j];
  });
  vector<pair<int, int>> res;
  for(auto& i: order) {
    int& j = p[i];
    if(i == j) continue;
    int& k = arg[i];
    if(weight[j] >= cap[i] || weight[i] >= cap[k]) {
      cout << -1 << endl;
      return 0;
    }
    res.emplace_back(i, k);
    p[k] = p[i];
    arg[p[i]] = k;
    p[i] = i;
    arg[i] = i;
  }
  int m = res.size();
  cout << m << endl;
  for(auto& [i, j]: res) { cout << i + 1 << ' ' << j + 1 << '\n'; }
}
