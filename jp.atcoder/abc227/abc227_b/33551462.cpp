#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  auto f = [&](int a, int b) -> int { return 4 * a * b + 3 * (a + b); };
  int const k = 1 << 10;
  vector<bool> possible(k);
  for(int a = 1; a < 1 << 8; a++) {
    for(int b = a; b < 1 << 8; b++) {
      int v = f(a, b);
      if(v >= k) break;
      possible[v] = true;
    }
  }
  int n;
  cin >> n;
  int cnt = 0;
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    cnt += !possible[x];
  }
  cout << cnt << endl;
}
