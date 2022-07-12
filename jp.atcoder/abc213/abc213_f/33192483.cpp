#include <bits/stdc++.h>
using namespace std;
#define loop while(1)
#define repeat(t) for(int __ = 0; __ < t; ++__)
#define range(i, n) for(int i = 0; i < n; ++i)
#define range_rev(i, n) for(int i = n - 1; i >= 0; --i)
#define iter(x, a) for(auto const& x: a)
template<typename T> using vec = vector<T>;
auto sa_is(vec<int> a) -> vec<int> {
  int mn = *min_element(a.begin(), a.end());
  int n = a.size();
  range(i, n) a[i] = a[i] - mn + 1;
  a.push_back(0);
  ++n;
  int m = *max_element(a.begin(), a.end()) + 1;
  vec<bool> is_s(n, true), is_lms(n);
  vec<int> lms;
  lms.reserve(n);
  range_rev(i, n - 1) {
    is_s[i] = a[i] != a[i + 1] ? a[i] < a[i + 1] : is_s[i + 1];
    is_lms[i + 1] = !is_s[i] && is_s[i + 1];
    if(is_lms[i + 1]) lms.push_back(i + 1);
  }
  reverse(lms.begin(), lms.end());
  vector<int> arg_l(m + 1), arg_r(m);
  iter(x, a) {
    arg_r[x]++;
    arg_l[x + 1]++;
  }
  range(i, m - 1) {
    arg_l[i + 1] += arg_l[i];
    arg_r[i + 1] += arg_r[i];
  }
  auto induce = [&]() -> vec<int> {
    vec<int> sa(n, -1);
    auto arg = arg_r;
    range_rev(i, lms.size()) sa[--arg[a[lms[i]]]] = lms[i];
    arg = arg_l;
    range(j, n) {
      int i = sa[j] - 1;
      if(i >= 0 && !is_s[i]) sa[arg[a[i]]++] = i;
    }
    arg = arg_r;
    range_rev(j, n) {
      int i = sa[j] - 1;
      if(i >= 0 && is_s[i]) sa[--arg[a[i]]] = i;
    }
    return sa;
  };
  vec<int> sa = induce(), lms_idx, rank(n, -1);
  lms_idx.reserve(n);
  iter(i, sa) if(is_lms[i]) lms_idx.push_back(i);
  int l = lms_idx.size();
  int r = 0;
  rank[n - 1] = r;
  range(i, l - 1) {
    int j = lms_idx[i], k = lms_idx[i + 1];
    range(d, n) {
      if(a[j + d] != a[k + d]) {
        ++r;
        break;
      }
      if(d > 0 && is_lms[j + d]) {
        r += !is_lms[k + d];
        break;
      }
    }
    rank[k] = r;
  }
  rank.erase(
    remove_if(rank.begin(), rank.end(), [](int x) { return x < 0; }), rank.end()
  );
  vec<int> lms_order;
  if(r == l - 1) {
    lms_order.resize(l);
    range(i, l) lms_order[rank[i]] = i;
  } else {
    lms_order = sa_is(rank);
  }
  range(i, l) lms_idx[i] = lms[lms_order[i]];
  swap(lms, lms_idx);
  sa = induce();
  return {sa.begin() + 1, sa.end()};
}
auto lcp_array(vector<int> a, vector<int> sa) -> vector<int> {
  int n = a.size();
  assert(n > 0 && (int)sa.size() == n);
  vector<int> rank(n), lcp(n - 1);
  for(int i = 0; i < n; i++) rank[sa[i]] = i;
  int h = 0;
  for(int i = 0; i < n; i++) {
    if(h > 0) --h;
    int r = rank[i];
    if(r == n - 1) continue;
    int j = sa[r + 1];
    while(max(i, j) + h < n && a[i + h] == a[j + h]) ++h;
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
  vector<int> sa = sa_is(a);
  vector<int> lcp = lcp_array(a, sa);
  vector<long> res(n);
  iota(res.rbegin(), res.rend(), 1);
  function<void()> count = [&]() -> void {
    using P = pair<int, int>;
    long s = 0;
    stack<P> st;
    for(int i = 0; i < n - 1; i++) {
      int l = 1, h = lcp[i];
      while(!st.empty() && st.top().first >= h) {
        P x = st.top();
        st.pop();
        l += x.second;
        s -= x.first * (long)x.second;
      }
      s += h * (long)l;
      res[sa[i + 1]] += s;
      st.emplace(h, l);
    }
  };
  repeat(2) {
    count();
    reverse(sa.begin(), sa.end());
    reverse(lcp.begin(), lcp.end());
  }
  for(auto& x: res) cout << x << '\n';
}
