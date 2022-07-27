#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  // in all k-consecutive subsequence,
  // positive abs miniumum as while
  // or
  // negative abs minimum as black
  int n, k;
  cin >> n >> k;
  vector<int> a(n), b(n);
  long s = 0;
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    if(x > 0) {
      s += x;
      a[i] = x;
    } else {
      b[i] = -x;
    }
  }
  long const inf = 1l << 60;
  auto f = [&](vector<int> const& a) -> long {
    vector<long> s(n + 1);
    for(int i = 0; i < n; i++) s[i + 1] = s[i] + a[i];
    long mn = inf;
    for(int i = 0; i < n - k + 1; i++) { mn = min(mn, s[i + k] - s[i]); }
    return mn;
  };
  cout << s - min(f(a), f(b)) << endl;
}
