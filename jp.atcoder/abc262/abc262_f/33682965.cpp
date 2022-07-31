#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, k;
  cin >> n >> k;
  vector<int> p(n);
  for(int i = 0; i < n; i++) {
    cin >> p[i];
    p[i]--;
  }
  vector<int> idx(n);
  for(int i = 0; i < n; i++) idx[p[i]] = i;
  int i0 = -1;
  int mn = n;
  for(int x = 0; x < n; x++) {
    if(x > mn) continue;
    int l = idx[x];
    int r = n - idx[x];
    if(min(l, r) > k) continue;
    i0 = idx[x];
    mn = x;
  }
  // cout << i0 << ' ' << mn << endl;
  auto solve0 = [&]() {
    // remove all left pattern
    vector<int> st0;
    int r = k - i0;
    if(r < 0) { return st0; }
    for(int i = i0; i < n; i++) {
      int x = p[i];
      while(st0.size() > 1 && r > 0 && st0.back() > x) {
        r--;
        st0.pop_back();
      }
      st0.push_back(x);
    }
    return st0;
  };
  auto st0 = solve0();
  // for(int i = 0; i < (int)st0.size(); i++) {
  //   cout << st0[i] << " \n"[i == (int)st0.size() - 1];
  // }
  auto solve1 = [&]() {
    // rotate right and itself to front and remove some of right pattern.
    vector<int> st1;
    int r = k - (n - i0);
    vector<bool> in_right(n);
    if(r < 0) { return st1; }
    for(int i = i0; i < n; i++) {
      int x = p[i];
      in_right[x] = true;
      while(st1.size() > 1 && st1.back() > x) { st1.pop_back(); }
      st1.push_back(x);
    }
    for(int i = 0; i < i0; i++) {
      int x = p[i];
      while(st1.size() > 1 && st1.back() > x) {
        if(in_right[st1.back()]) {
          st1.pop_back();
          continue;
        }
        if(r == 0) break;
        r--;
        st1.pop_back();
      }
      st1.push_back(x);
    }
    return st1;
  };
  auto st1 = solve1();
  // for(int i = 0; i < (int)st1.size(); i++) {
  //   cout << st1[i] << " \n"[i == (int)st1.size() - 1];
  // }
  // compare res0 and res1
  int n0 = st0.size(), n1 = st1.size();
  assert(n0 || n1);
  auto smaller = [&]() -> vector<int> {
    if(!n0) return st1;
    if(!n1) return st0;
    for(int i = 0; i < min(n0, n1); i++) {
      int x = st0[i];
      int y = st1[i];
      if(x < y) return st0;
      if(x > y) return st1;
    }
    if(n0 <= n1) return st0;
    return st1;
  };
  auto res = smaller();
  n = res.size();
  for(int i = 0; i < n; i++) { cout << res[i] + 1 << " \n"[i == n - 1]; }
}
