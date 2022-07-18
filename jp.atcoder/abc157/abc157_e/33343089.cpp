#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  // lowercases are only 26 kinds.
  int n;
  string s;
  int q;
  cin >> n >> s >> q;
  // f(r) - f(l - 1)
  // ordered set, fenwick, segtree.
  vector<int> a(n);
  for(int i = 0; i < n; i++) a[i] = s[i] - 'a';
  int const k = 26;
  vector<set<int>> indices(k);
  for(int i = 0; i < n; i++) { indices[a[i]].insert(i); }
  while(q--) {
    int t;
    cin >> t;
    if(t == 1) {
      int i;
      char c;
      cin >> i >> c;
      i--;
      int j = c - 'a';
      indices[a[i]].erase(i);
      a[i] = j;
      indices[j].insert(i);
    } else {
      int l, r;
      cin >> l >> r;
      l--;
      r--;
      int cnt = 0;
      for(int i = 0; i < k; i++) {
        cnt += indices[i].upper_bound(r) != indices[i].upper_bound(l - 1);
      }
      cout << cnt << endl;
    }
  }
}
