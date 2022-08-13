#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> h(n), s(n);
  for(int i = 0; i < n; i++) cin >> h[i] >> s[i];
  auto f = [&](long x) -> bool {
    vector<long> t(n);
    for(int i = 0; i < n; i++) t[i] = (x - h[i]) / s[i];
    sort(t.begin(), t.end());
    for(int i = 0; i < n; i++) {
      if(t[i] < i) return false;
    }
    return true;
  };
  long ng = *max_element(h.begin(), h.end()) - 1;
  long ok = 1l << 50;
  while(ok - ng > 1) {
    long x = (ok + ng) >> 1;
    if(f(x)) ok = x;
    else ng = x;
  }
  cout << ok << endl;
}
