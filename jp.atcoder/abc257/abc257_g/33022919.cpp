#include <bits/stdc++.h>
using namespace std;

template<typename A> auto morris_pratt(const A& a) -> vector<int> {
  int n = a.size();
  vector<int> lb(n);
  int d = 0;
  for(int i = 1; i < n; i++) {
    while(d != 0 && a[d] != a[i]) d = lb[d - 1];
    d += a[d] == a[i];
    lb[i] = d;
  }
  return lb;
}

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  string s, t;
  cin >> s >> t;
  int n = s.size(), m = t.size();

  auto lb = morris_pratt(s + '$' + t);
  int i = m;
  int k = 0;
  while(i > 0) {
    int d = lb[n + i];
    if(!d) {
      cout << -1 << endl;
      return 0;
    }
    i -= d;
    k += 1;
  }
  cout << k << endl;
}