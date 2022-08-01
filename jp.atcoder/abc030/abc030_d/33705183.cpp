#include <bits/stdc++.h>
using namespace std;
class functional_graph_kth_from {
public:
  vector<int> path;
  int cycle_size;
  int cycle_start_idx;
  functional_graph_kth_from(vector<int> const& f, int src) {
    int n = f.size();
    vector<int> order(n, -1);
    for(int i = src, j = 0;; j++) {
      if(order[i] != -1) {
        cycle_size = j - order[i];
        cycle_start_idx = order[i];
        break;
      }
      order[i] = j;
      path.push_back(i);
      i = f[i];
    }
  }
  auto operator()(long k) -> int const& {
    if(k >= cycle_start_idx)
      k = (k - cycle_start_idx) % cycle_size + cycle_start_idx;
    return path[k];
  }
};
auto main() -> int {
  int n, a;
  string k;
  cin >> n >> a >> k;
  a--;
  vector<int> f(n);
  for(int i = 0; i < n; i++) {
    cin >> f[i];
    f[i]--;
  }
  auto g = functional_graph_kth_from(f, a);
  int res;
  if(k.size() < 10) {
    res = g(stoi(k));
  } else {
    int i = -g.cycle_start_idx;
    int l = g.cycle_size;
    reverse(k.begin(), k.end());
    int p = 1;
    for(auto& c: k) {
      int d = c - '0';
      i += d * p;
      i %= l;
      p *= 10;
      p %= l;
    }
    i += l;
    i %= l;
    res = g(i + g.cycle_start_idx);
  }
  cout << res + 1 << endl;
}
