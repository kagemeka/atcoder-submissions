#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, a, b;
  cin >> n >> a >> b;
  vector<int> c(n);
  for(int i = 0; i < n; i++) cin >> c[i];
  auto possible = [&](int x) -> bool {
    int ca = 0, cb = 0;
    for(auto& y: c) {
      if(y <= x) {
        ca += ((x - y + a - 1) / a);
      } else {
        cb += (y - x) / b;
      }
    }
    return ca <= cb;
  };
  int ok = 0, ng = 1 << 30;
  while(ng - ok > 1) {
    int x = (ok + ng) >> 1;
    if(possible(x)) ok = x;
    else ng = x;
  }
  cout << ok << endl;
}
