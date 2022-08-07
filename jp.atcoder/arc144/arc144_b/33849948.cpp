#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, a, b;
  cin >> n >> a >> b;
  vector<int> v(n);
  for(int i = 0; i < n; i++) cin >> v[i];
  auto possible = [&](int x) -> bool {
    long c = 0;
    for(auto& y: v) {
      if(y >= x) c += (y - x) / b;
      else c -= (x - y + a - 1) / a;
    }
    return c >= 0;
  };
  int ok = 0, ng = 1 << 30;
  while(ng - ok > 1) {
    int x = (ng + ok) >> 1;
    if(possible(x)) ok = x;
    else ng = x;
  }
  cout << ok << endl;
}
