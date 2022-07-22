#include <bits/stdc++.h>
using namespace std;
template<typename A> auto morris_pratt(const A& a) -> vector<int> {
  int n = a.size();
  vector<int> lb(n); // longest border
  for(int i = 1, d = 0; i < n; i++) {
    while(d != 0 && a[d] != a[i]) d = lb[d - 1];
    d += a[d] == a[i];
    lb[i] = d;
  }
  return lb;
}
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  cin >> s;
  auto lb = morris_pratt(s);
  int n = s.size();
  for(int i = n - 2; i >= 0; i--) {
    if(i - lb[i] < lb[i]) {
      cout << (i - lb[i] + 1) * 2 << endl;
      return 0;
    }
  }
}
