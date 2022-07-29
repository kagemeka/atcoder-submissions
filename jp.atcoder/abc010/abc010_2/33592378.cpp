#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  int cnt = 0;
  while(n--) {
    int x;
    cin >> x;
    while(x % 3 == 2 || (x & 1) == 0) {
      x--;
      cnt++;
    }
  }
  cout << cnt << endl;
}
