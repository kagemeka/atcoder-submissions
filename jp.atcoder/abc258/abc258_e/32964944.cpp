#include <bits/stdc++.h>

using namespace std;

// able to compute at most 2^k th from any node in O(k) time.
auto functional_graph_doubling_table(const vector<int>& f, int k)
    -> vector<vector<int>> {
  int n = f.size();
  vector<vector<int>> a(k + 1);
  a[0] = f;
  for (int i = 0; i < k; i++) {
    vector<int> b(n);
    for (int j = 0; j < n; j++) {
      b[j] = a[i][a[i][j]];
    }
    a[i + 1] = b;
  }
  return a;
}

class functional_graph_kth_from_any {
  vector<vector<int>> table;

public:
  // k <= 2^exp
  functional_graph_kth_from_any(const vector<int>& f, long max_exp)
      : table(functional_graph_doubling_table(f, max_exp)) {}

  auto operator()(int src, long k) -> int {
    int i = src;
    for (int j = 0; j < (int)table.size(); j++) {
      if (~k >> j & 1) continue;
      i = table[j][i];
    }
    return i;
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
  long p = x / s * n;
  x %= s;
  vector<long> cnt(n, p);

  s = 0;
  vector<int> f(n);
  for (int i = 0, r = 0; i < n; i++) {
    while (s < x) s += w[r++];
    cnt[i] += r - i;
    f[i] = r % n;
    s -= w[i];
  }

  auto g = functional_graph_kth_from_any(f, 40);

  while (q--) {
    long k;
    cin >> k;
    cout << cnt[g(0, k - 1)] << endl;
  }
}
