#include <bits/stdc++.h>

using namespace std;

class functional_graph_kth_from {
  vector<int> path;
  int cycle_size;
  int cycle_start_idx;

public:
  functional_graph_kth_from(const vector<int>& f, int src) {
    int n = f.size();
    vector<int> order(n, -1);

    for (int i = src, j = 0;; j++) {
      if (order[i] != -1) {
        cycle_size = j - order[i];
        cycle_start_idx = order[i];
        break;
      }
      order[i] = j;
      path.push_back(i);
      i = f[i];
    }
  }

  auto operator()(long k) -> const int& {
    if (k >= cycle_start_idx)
      k = (cycle_start_idx - k) % cycle_size + cycle_start_idx;
    return path[k];
  }
};

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, q, x;
  cin >> n >> q >> x;

  vector<long> w(n);
  for (auto& x : w) cin >> x;

  long s = 0;
  for (int i = 0; i < n; i++) {
    s += w[i];
    w.push_back(w[i]);
  }
  long p = x / s;
  x %= s;
  vector<long> cnt(n, p);

  s = 0;
  vector<int> f(n);
  for (int i = 0, r = 0; i < n; i++) {
    while (s < x) {
      s += w[r];
      r++;
    }
    cnt[i] += r - i;
    f[i] = r % n;
    s -= w[i];
  }

  auto g = functional_graph_kth_from(f, 0);

  while (q--) {
    long k;
    cin >> k;
    cout << cnt[g(k - 1)] << endl;
  }
}
