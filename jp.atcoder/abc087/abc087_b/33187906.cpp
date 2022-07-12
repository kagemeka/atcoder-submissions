#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int a, b, c, s;
  cin >> a >> b >> c >> s;
  s /= 50;
  int cnt = 0;
  for(int i = 0; i <= a; i++) {
    for(int j = 0; j <= b; j++) {
      for(int k = 0; k <= c; k++) {
        int v = 10 * i + 2 * j + k;
        cnt += v == s;
      }
    }
  }
  cout << cnt << endl;
}
