#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> p(n), q(n);
  for(int i = 0; i < n; i++) cin >> p[i];
  for(int i = 0; i < n; i++) cin >> q[i];
  for(int i = 0; i < n; i++) {
    p[i]--;
    q[i]--;
  }
  auto permutation_rank = [&](vector<int> p) -> int {
    int n = p.size();
    int s = (1 << n) - 1;
    int fact = 1;
    int rank = 0;
    for(int i = 0; i < n; i++) {
      int j = p[n - i - 1];
      rank += (j - __builtin_popcount(s & ((1 << j) - 1))) * fact;
      s &= ~(1 << j);
      fact *= (i + 1);
    }
    return rank;
  };
  cout << abs(permutation_rank(p) - permutation_rank(q)) << endl;
}
