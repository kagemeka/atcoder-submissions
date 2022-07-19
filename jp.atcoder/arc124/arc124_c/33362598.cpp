#include <bits/stdc++.h>
using namespace std;
template<typename A> auto unique(A a) -> A {
  sort(a.begin(), a.end());
  a.erase(std::unique(a.begin(), a.end()), a.end());
  return a;
}
auto main() -> int {
  int n;
  cin >> n;
  using p = pair<int, int>;
  vector<p> que{
    {0, 0}
  };
  while(n--) {
    int x, y;
    cin >> x >> y;
    vector<p> next_que;
    for(auto& [a, b]: que) {
      next_que.emplace_back(gcd(a, x), gcd(b, y));
      next_que.emplace_back(gcd(b, x), gcd(a, y));
    }
    que = unique(next_que);
  }
  long mx = 1;
  for(auto& [x, y]: que) { mx = max(mx, lcm((long)x, (long)y)); }
  cout << mx << endl;
}