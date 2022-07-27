#include <bits/stdc++.h>
using namespace std;
struct fenwick {
  vector<long> data;
  fenwick(int size): data(size + 1) {}
  auto size() -> int { return data.size() - 1; }
  auto add(int i, long x) {
    for(i++; i <= size(); i += i & -i) data[i] += x;
  }
  auto get(int i) -> long {
    long v = 0;
    for(; i > 0; i -= i & -i) v += data[i];
    return v;
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m, q;
  cin >> n >> m >> q;
  using tup = tuple<int, int, int, int>;
  vector<tup> queries(q);
  for(int l = 0; l < q; l++) {
    int t, i, j, k = l;
    cin >> t >> i >> j;
    if(t == 1) cin >> k;
    queries[l] = {t, i, j, k};
  }
  reverse(queries.begin(), queries.end());
  fenwick fw(m);
  vector<long> res(q, -1);
  vector<vector<tuple<int, int, long>>> st(n); // (query i, col, offset)
  for(auto& [t, i, j, k]: queries) {
    if(t == 3) {
      i--;
      j--;
      // push (k, j, offset)
      long offset = fw.get(j + 1);
      st[i].emplace_back(k, j, offset);
    }
    if(t == 1) {
      i--;
      j--;
      fw.add(i, k);
      fw.add(j + 1, -k);
    }
    if(t == 2) {
      i--;
      long x = j;
      while(st[i].size()) {
        auto [qi, j, offset] = st[i].back();
        st[i].pop_back();
        res[qi] = x + fw.get(j + 1) - offset;
      }
    }
  }
  for(int i = 0; i < n; i++) {
    long x = 0;
    while(st[i].size()) {
      auto [qi, j, offset] = st[i].back();
      st[i].pop_back();
      res[qi] = x + fw.get(j + 1) - offset;
    }
  }
  for(auto& x: res) {
    if(x == -1) continue;
    cout << x << endl;
  }
}
