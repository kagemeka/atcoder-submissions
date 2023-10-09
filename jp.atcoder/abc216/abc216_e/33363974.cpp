#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  // binary search minimum fun.
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  auto possible = [&](int x) -> bool {
    long cnt = 0;
    for(int i = 0; i < n; i++) { cnt += max(0, a[i] - x + 1); }
    return cnt <= k;
  };
  long ng = 0, ok = 1l << 31;
  while(ok - ng > 1) {
    int x = (ng + ok) >> 1;
    if(possible(x)) ok = x;
    else ng = x;
  }
  long res = 0;
  long cnt = 0;
  for(int i = 0; i < n; i++) {
    long c = max(0l, a[i] - (long)ok + 1);
    cnt += c;
    res += ((long)a[i] + ok) * c >> 1;
  }
  res += ((long)ok - 1) * (k - cnt);
  cout << res << endl;
}
