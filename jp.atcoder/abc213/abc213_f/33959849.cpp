#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for(int i = 0; i < n; ++i)
auto suffix_array(vector<int> const& s) -> vector<int> {
  int n = s.size();
  vector<long> a(n);
  rep(i, n) a[i] = s[i];
  vector<int> sa(n);
  iota(sa.begin(), sa.end(), 0);
  int d = 1;
  while(true) {
    rep(i, n) a[i] = a[i] << 30 | (i + d < n ? 1 + a[i + d] : 0);
    sort(sa.begin(), sa.end(), [&](int i, int j) { return a[i] < a[j]; });
    d <<= 1;
    if(d >= n) break;
    int rank = 0;
    long prev = a[sa[0]];
    for(auto& i: sa) {
      if(a[i] > prev) {
        rank++;
        prev = a[i];
      }
      a[i] = rank;
    }
    if(rank == n) break;
  }
  return sa;
}
auto lcp_array(vector<int> const& a, vector<int> const& sa) -> vector<int> {
  int n = a.size();
  assert(n > 0 && (int)sa.size() == n);
  vector<int> rank(n), lcp(n - 1);
  rep(i, n) rank[sa[i]] = i;
  int h = 0;
  rep(i, n) {
    if(h > 0) --h;
    int r = rank[i];
    if(r == n - 1) continue;
    for(int j = sa[r + 1]; max(i, j) + h < n && a[i + h] == a[j + h]; ++h)
      ;
    lcp[r] = h;
  }
  return lcp;
}
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  string s;
  cin >> n >> s;
  vector<int> a(n);
  for(int i = 0; i < n; i++) a[i] = s[i] - 'a';
  vector<int> sa = suffix_array(a);
  vector<int> lcp = lcp_array(a, sa);
  vector<long> res(n);
  iota(res.rbegin(), res.rend(), 1);
  rep(t, 2) {
    stack<pair<int, int>> st;
    long s = 0;
    for(int i = 0; i < n - 1; i++) {
      int l = 1, h = lcp[i];
      while(!st.empty() && st.top().second >= h) {
        auto [x, y] = st.top();
        st.pop();
        l += x;
        s -= (long)x * y;
      }
      st.emplace(l, h);
      s += (long)l * h;
      res[sa[i + 1]] += s;
    }
    reverse(sa.begin(), sa.end());
    reverse(lcp.begin(), lcp.end());
  }
  for(auto& x: res) cout << x << '\n';
}
