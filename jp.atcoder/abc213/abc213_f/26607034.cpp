#include <iostream>




#include <vector>
#include <algorithm>
#include <functional>
#include <bits/stdc++.h>

std::vector<int> sa_is(std::vector<int> a) {
  int mn = *std::min_element(a.begin(), a.end());
  int n = a.size();
  for (int i = 0; i < n; i++) a[i] = a[i] - mn + 1;
  a.push_back(0);
  ++n;
  int m = *std::max_element(a.begin(), a.end()) + 1;
  std::vector<bool> is_s(n, true), is_lms(n);
  std::vector<int> lms; lms.reserve(n);
  for (int i = n - 1; i > 0; i--) {
    is_s[i - 1] = a[i - 1] == a[i] ? is_s[i] : a[i - 1] < a[i];
    is_lms[i] = !is_s[i - 1] && is_s[i];
    if (is_lms[i]) lms.push_back(i);
  }
  std::reverse(lms.begin(), lms.end());
  std::vector<int> bucket(m);
  for (const int &x : a) bucket[x]++;

  std::function<std::vector<int>()> induce = [&]() -> std::vector<int> {
    std::vector<int> sa(n, -1);
    std::vector<int> sa_idx(m);
    std::copy(bucket.begin(), bucket.end(), sa_idx.begin());
    for (int i = 0; i < m - 1; i++) sa_idx[i + 1] += sa_idx[i];
    for (int i = lms.size() - 1; i > -1; i--) sa[--sa_idx[a[lms[i]]]] = lms[i];

    std::copy(bucket.begin(), bucket.end(), sa_idx.begin());
    int s = 0;
    for (int i = 0; i < m; i++) { sa_idx[i] += s; std::swap(s, sa_idx[i]); }
    for (int j = 0; j < n; j++) {
      int i = sa[j] - 1;
      if (i >= 0 && !is_s[i]) sa[sa_idx[a[i]]++] = i;
    }

    std::copy(bucket.begin(), bucket.end(), sa_idx.begin());
    for (int i = 0; i < m - 1; i++) sa_idx[i + 1] += sa_idx[i];
    for (int j = n - 1; j > -1; j--) {
      int i = sa[j] - 1;
      if (i >= 0 && is_s[i]) sa[--sa_idx[a[i]]] = i;
    }
    return sa;
  };

  std::vector<int> sa = induce(), lms_idx, rank(n, -1);
  lms_idx.reserve(n);
  for (const int &i : sa) if (is_lms[i]) lms_idx.push_back(i);
  int l = lms_idx.size();
  int r = 0; rank[n - 1] = r;
  for (int i = 0; i < l - 1; i++) {
    int j = lms_idx[i], k = lms_idx[i + 1];
    for (int d = 0; d < n; d++) {
      bool j_is_lms = is_lms[j + d], k_is_lms = is_lms[k + d];
      if (a[j + d] != a[k + d] || j_is_lms ^ k_is_lms) { ++r; break; }
      if (d > 0 && j_is_lms | k_is_lms) break;
    }
    rank[k] = r;
  }
  rank.erase(
    std::remove_if(rank.begin(), rank.end(), [](int x){ return x < 0; }),
    rank.end()
  );
  std::vector<int> lms_order;
  if (r == l - 1) {
    lms_order.resize(l);
    for (int i = 0; i < l; i++) lms_order[rank[i]] = i;
  } else {
    lms_order = sa_is(rank);
  }
  std::vector<int> buf(l);
  for (int i = 0; i < l; i++) buf[i] = lms[lms_order[i]];
  swap(lms, buf);
  sa = induce();
  return std::vector<int>(sa.begin() + 1, sa.end());
}


#include <vector>
#include <cassert>


std::vector<int> lcp_array_kasai(std::vector<int> a, std::vector<int> sa) {
  int n = a.size();
  assert(n > 0 && sa.size() == n);
  std::vector<int> rank(n), lcp(n - 1);
  for (int i = 0; i < n; i++) rank[sa[i]] = i;
  int h = 0;
  for (int i = 0; i < n; i++) {
    if (h > 0) --h;
    int r = rank[i];
    if (r == n - 1) continue;
    int j = sa[r + 1];
    while (i + h < n && j + h < n && a[i + h] == a[j + h]) ++h;
    lcp[r] = h;
  }
  return lcp;
}


#include <functional>
#include <stack>

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  int n;
  std::string s;
  std::cin >> n >> s;
  std::vector<int> a(n);
  for (int i = 0; i < n; i++) a[i] = s[i] - 'a';
  std::vector<int> sa = sa_is(a);
  std::vector<int> lcp = lcp_array_kasai(a, sa);

  std::vector<long long> res(n);
  std::iota(res.rbegin(), res.rend(), 1);
  std::function<void()> count = [&]() -> void {
    using P = std::pair<int, int>;
    long long s = 0;
    std::stack<P> st;
    for (int i = 0; i < n - 1; i++) {
      int l = 1, h = lcp[i];
      while (!st.empty() && st.top().first >= h) {
        P x = st.top(); st.pop();
        l += x.second;
        s -= x.first * (long long)x.second;
      }
      s += h * (long long)l;
      res[sa[i + 1]] += s;
      st.emplace(h, l);
    }
  };
  for (int i = 0; i < 2; i++) {
    count();
    std::reverse(sa.begin(), sa.end());
    std::reverse(lcp.begin(), lcp.end());
  }
  for (const long long &x : res) std::cout << x << '\n';
}
